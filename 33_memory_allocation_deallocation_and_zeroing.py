#!/usr/bin/env python3
"""
================================================================================
LESSON 33: MEMORY ALLOCATION, 1ST TOUCH VS. 2ND TOUCH ZEROING, AND DEALLOCATION
================================================================================

When working with high-performance I/O, data pipelines, and large buffer operations,
understanding WHERE memory latency comes from is critical.

A memory allocation is NOT a single monolithic operation. It consists of distinct phases:

1. Virtual Address Allocation (`malloc` / `mmap`):
   - The OS kernel or runtime allocator reserves a range of virtual address space.
   - Fast and lightweight (O(1), microseconds) because no physical RAM is allocated yet
     (Linux "Demand Paging" / lazy allocation).

2. 1st Touch Zeroing (Cold Physical Page Allocation & Kernel Security Wipe):
   - For security and process isolation, the OS kernel must provide zero-filled pages.
   - When memory is first written to, the CPU triggers a "minor page fault" (trap to Ring 0).
   - The kernel allocates a physical 4 KB frame, zeroes it out, and maps it into the page table.
   - This phase accounts for 90% to 99% of total allocation latency.

3. 2nd Touch Zeroing (Warm In-Memory Overwrite):
   - When rewriting to an already-allocated buffer, zero page faults occur.
   - Execution stays 100% in user space (Ring 3) without kernel traps.
   - The speed is bounded purely by CPU cache (L1/L2/L3) and DRAM write bus bandwidth.
   - Up to 2x to 8x faster than 1st touch!

4. Deallocation (`free` / `munmap` / Python `del`):
   - The virtual mapping is dismantled and physical pages are returned to the OS or allocator pool.
   - In Python, small objects (<= 512B) return to `PyMalloc` pools; large buffers call OS `free()` / `munmap()`.

--------------------------------------------------------------------------------
KEY CONCEPTS DEMONSTRATED IN THIS LESSON:
--------------------------------------------------------------------------------
1. C-Level Isolation (`ctypes`):
   - Measuring raw `malloc()`, 1st touch `memset()`, 2nd touch `memset()`, and `free()`.
2. Kernel Page Faults (`resource.getrusage`):
   - Tracking `ru_minflt` (minor page faults) during 1st touch vs. 0 faults during 2nd touch.
3. Python Buffer Lifecycle:
   - Comparing `bytearray(sz)` creation vs. in-place overwrite vs. `del` deallocation.
4. Multi-Size Scalability Table (128 KB to 64 MB):
   - Comparing 1st touch vs. 2nd touch across CPU L1/L2/L3 caches and DRAM memory bus limits.
"""

import gc
import mmap
import resource
import time
import ctypes
from typing import Dict, List, Tuple

# Load standard C library functions for raw hardware profiling
libc = ctypes.CDLL(None)
libc.malloc.restype = ctypes.c_void_p
libc.malloc.argtypes = [ctypes.c_size_t]
libc.free.argtypes = [ctypes.c_void_p]
libc.memset.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_size_t]


# ================================================================================
# PART 1: RAW C-LEVEL ISOLATION (MALLOC vs. 1ST TOUCH vs. 2ND TOUCH vs. FREE)
# ================================================================================

def demonstrate_c_level_breakdown(sz: int = 64 * 1024 * 1024):
    """
    Measures raw C-level malloc, 1st touch memset (cold), 2nd touch memset (warm),
    and free latency on a large buffer. Strips away Python object creation and GC overhead.
    """
    print("\n" + "=" * 80)
    print(f"PART 1: C-LEVEL ISOLATION BREAKDOWN ({sz // (1024 * 1024)} MB BUFFER)")
    print("=" * 80)

    # 1. Virtual Allocation (malloc)
    t0 = time.perf_counter_ns()
    ptr = libc.malloc(sz)
    t_alloc_ms = (time.perf_counter_ns() - t0) / 1e6

    # 2. 1st Touch Zeroing (memset on cold memory -> triggers kernel page faults)
    t0 = time.perf_counter_ns()
    libc.memset(ptr, 0, sz)
    t_1st_touch_ms = (time.perf_counter_ns() - t0) / 1e6

    # 3. 2nd Touch Zeroing (memset on warm memory -> 0 page faults, pure memory bus write)
    t0 = time.perf_counter_ns()
    libc.memset(ptr, 0, sz)
    t_2nd_touch_ms = (time.perf_counter_ns() - t0) / 1e6

    # 4. Deallocation (free)
    t0 = time.perf_counter_ns()
    libc.free(ptr)
    t_free_ms = (time.perf_counter_ns() - t0) / 1e6

    total_cold_ms = t_alloc_ms + t_1st_touch_ms + t_free_ms
    speedup = t_1st_touch_ms / max(t_2nd_touch_ms, 0.0001)
    bw_1st = (sz / (1024 ** 3)) / (t_1st_touch_ms / 1000) if t_1st_touch_ms > 0 else 0
    bw_2nd = (sz / (1024 ** 3)) / (t_2nd_touch_ms / 1000) if t_2nd_touch_ms > 0 else 0

    print(f"1. Virtual Allocation (`malloc`):        {t_alloc_ms:>8.4f} ms ({t_alloc_ms / total_cold_ms * 100:>5.1f}%) -> Fast virtual reservation")
    print(f"2. 1st Touch Zeroing  (`memset` cold):   {t_1st_touch_ms:>8.4f} ms ({t_1st_touch_ms / total_cold_ms * 100:>5.1f}%) -> Page faults + DRAM write ({bw_1st:.2f} GB/s)")
    print(f"3. 2nd Touch Zeroing  (`memset` warm):   {t_2nd_touch_ms:>8.4f} ms (Speedup: {speedup:.2f}x faster! -> 0 page faults, {bw_2nd:.2f} GB/s)")
    print(f"4. Deallocation       (`free`):          {t_free_ms:>8.4f} ms ({t_free_ms / total_cold_ms * 100:>5.1f}%) -> Unmapping pages")
    print(f"Total Cold Allocation Lifecycle Time:    {total_cold_ms:>8.4f} ms")


# ================================================================================
# PART 2: LINUX KERNEL MINOR PAGE FAULT PROFILING (1ST TOUCH vs. 2ND TOUCH)
# ================================================================================

def demonstrate_kernel_page_faults(sz: int = 32 * 1024 * 1024):
    """
    Demonstrates Linux demand paging by tracking minor page faults (ru_minflt).
    Shows how virtual allocation generates 0 page faults, 1st touch faults all pages,
    and 2nd touch generates 0 page faults.
    """
    print("\n" + "=" * 80)
    print(f"PART 2: KERNEL MINOR PAGE FAULTS ({sz // (1024 * 1024)} MB / 4 KB PAGES)")
    print("=" * 80)

    expected_pages = sz // 4096
    print(f"Total 4 KB pages in buffer: {expected_pages:,}")

    # Phase 1: Anonymous mmap (Virtual allocation only)
    f_before = resource.getrusage(resource.RUSAGE_SELF).ru_minflt
    t0 = time.perf_counter_ns()
    mm = mmap.mmap(-1, sz, mmap.MAP_PRIVATE | mmap.MAP_ANONYMOUS)
    t_alloc_ms = (time.perf_counter_ns() - t0) / 1e6
    faults_alloc = resource.getrusage(resource.RUSAGE_SELF).ru_minflt - f_before

    print(f"1. Anonymous mmap (Virtual Alloc):  {t_alloc_ms:.4f} ms | Page Faults: {faults_alloc}")

    # Phase 2: 1st Touch (Zeroing every page - cold)
    f_before = resource.getrusage(resource.RUSAGE_SELF).ru_minflt
    t0 = time.perf_counter_ns()
    for i in range(0, sz, 4096):
        mm[i] = 0
    t_1st_touch_ms = (time.perf_counter_ns() - t0) / 1e6
    faults_1st_touch = resource.getrusage(resource.RUSAGE_SELF).ru_minflt - f_before

    print(f"2. 1st Touch (Cold Page Faulting):  {t_1st_touch_ms:.4f} ms | Page Faults: {faults_1st_touch:,}")

    # Phase 3: 2nd Touch (Warm memory - pages already mapped!)
    f_before = resource.getrusage(resource.RUSAGE_SELF).ru_minflt
    t0 = time.perf_counter_ns()
    for i in range(0, sz, 4096):
        mm[i] = 0
    t_2nd_touch_ms = (time.perf_counter_ns() - t0) / 1e6
    faults_2nd_touch = resource.getrusage(resource.RUSAGE_SELF).ru_minflt - f_before

    speedup = t_1st_touch_ms / max(t_2nd_touch_ms, 0.0001)
    print(f"3. 2nd Touch (Warm Memory):         {t_2nd_touch_ms:.4f} ms | Page Faults: {faults_2nd_touch} ({speedup:.1f}x faster!)")

    # Phase 4: Deallocation (munmap)
    t0 = time.perf_counter_ns()
    mm.close()
    del mm
    t_dealloc_ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"4. Deallocation (munmap):           {t_dealloc_ms:.4f} ms")


# ================================================================================
# PART 3: PYTHON BUFFER LIFECYCLE & GC IMPACT
# ================================================================================

def demonstrate_python_buffer_lifecycle(sz: int = 16 * 1024 * 1024, iters: int = 20):
    """
    Measures high-level Python bytearray allocation, in-place re-zeroing, and deallocation.
    Evaluates the impact of disabling Python GC.
    """
    print("\n" + "=" * 80)
    print(f"PART 3: PYTHON BUFFER LIFECYCLE ({sz // (1024 * 1024)} MB x {iters} ITERS)")
    print("=" * 80)

    # --- Run with GC Enabled vs Disabled ---
    for gc_enabled in [True, False]:
        if gc_enabled:
            gc.enable()
            mode = "GC ENABLED"
        else:
            gc.disable()
            mode = "GC DISABLED"

        # 1. Allocate + Zero (bytearray initialisation)
        t0 = time.perf_counter_ns()
        buffers = [bytearray(sz) for _ in range(iters)]
        t_alloc_ms = (time.perf_counter_ns() - t0) / iters / 1e6

        # 2. In-place re-zeroing of existing buffer (2nd touch)
        zero_payload = b"\x00" * sz
        t0 = time.perf_counter_ns()
        for ba in buffers:
            ba[:] = zero_payload
        t_rezero_ms = (time.perf_counter_ns() - t0) / iters / 1e6

        # 3. Deallocation
        t0 = time.perf_counter_ns()
        del buffers
        t_dealloc_ms = (time.perf_counter_ns() - t0) / iters / 1e6

        print(f"[{mode}]")
        print(f"  • 1st Touch (Alloc + Initial Zero): {t_alloc_ms:>8.3f} ms/iter")
        print(f"  • 2nd Touch (In-place Re-zero):     {t_rezero_ms:>8.3f} ms/iter")
        print(f"  • Deallocation (`del`):             {t_dealloc_ms:>8.3f} ms/iter")

    gc.enable()


# ================================================================================
# PART 4: SCALABILITY BENCHMARK ACROSS SIZES (128 KB TO 64 MB)
# ================================================================================

BUFFER_SIZES: List[Tuple[str, int, int]] = [
    ("128 KB", 128 * 1024, 1_000),
    ("512 KB", 512 * 1024, 500),
    ("2 MB",   2 * 1024 * 1024, 100),
    ("8 MB",   8 * 1024 * 1024, 30),
    ("32 MB",  32 * 1024 * 1024, 10),
    ("64 MB",  64 * 1024 * 1024, 5),
]

def run_scalability_benchmark():
    print("\n" + "=" * 115)
    print("PART 4: MULTI-SIZE SCALABILITY BENCHMARK (1ST TOUCH vs. 2ND TOUCH ZEROING)")
    print("=" * 115)
    print(f"{'Size':<10} | {'Virtual Alloc':<14} | {'1st Touch (Cold)':<18} | {'2nd Touch (Warm)':<18} | {'Speedup':<9} | {'2nd Touch BW':<14}")
    print("-" * 115)

    for label, sz, iters in BUFFER_SIZES:
        t_alloc_total = 0.0
        t_1st_total = 0.0
        t_2nd_total = 0.0
        t_free_total = 0.0

        for _ in range(iters):
            # Virtual allocation
            t0 = time.perf_counter_ns()
            ptr = libc.malloc(sz)
            t_alloc_total += (time.perf_counter_ns() - t0)

            # 1st Touch Zeroing (Cold)
            t0 = time.perf_counter_ns()
            libc.memset(ptr, 0, sz)
            t_1st_total += (time.perf_counter_ns() - t0)

            # 2nd Touch Zeroing (Warm)
            t0 = time.perf_counter_ns()
            libc.memset(ptr, 0, sz)
            t_2nd_total += (time.perf_counter_ns() - t0)

            # Free
            t0 = time.perf_counter_ns()
            libc.free(ptr)
            t_free_total += (time.perf_counter_ns() - t0)

        avg_alloc_ms = (t_alloc_total / iters) / 1e6
        avg_1st_ms = (t_1st_total / iters) / 1e6
        avg_2nd_ms = (t_2nd_total / iters) / 1e6
        speedup = avg_1st_ms / max(avg_2nd_ms, 0.00001)
        bw_2nd_gb_s = (sz / (1024 ** 3)) / (avg_2nd_ms / 1000) if avg_2nd_ms > 0 else 0

        print(f"{label:<10} | {avg_alloc_ms:>10.4f} ms | {avg_1st_ms:>14.4f} ms | {avg_2nd_ms:>14.4f} ms | {speedup:>7.2f}x | {bw_2nd_gb_s:>10.2f} GB/s")


# ================================================================================
# YOUR TURN: EXERCISE 33
# ================================================================================
# Scenario:
# You are building a diagnostic memory profiling utility for a high-throughput
# data pipeline. You need to create a class `MemoryLifecycleProfiler` that can
# profile any buffer size and return a structured report of:
# 1. Virtual allocation time (ms)
# 2. 1st Touch Zeroing time (ms)
# 3. 2nd Touch Zeroing time (ms)
# 4. 2nd Touch Speedup factor
# 5. Deallocation time (ms)
# 6. Number of minor page faults during 1st touch vs 2nd touch
#
# INSTRUCTIONS:
# 1. Create a class `MemoryLifecycleProfiler`.
# 2. Implement `profile_c_memory(self, size_bytes: int) -> dict`:
#    - Allocate memory using `libc.malloc(size_bytes)`.
#    - 1st Touch: `libc.memset(ptr, 0, size_bytes)`.
#    - 2nd Touch: `libc.memset(ptr, 0, size_bytes)`.
#    - Free: `libc.free(ptr)`.
#    - Return dict with keys: 'alloc_ms', 'first_touch_ms', 'second_touch_ms', 'speedup', 'free_ms', 'bandwidth_gb_s'.
# 3. Implement `profile_page_faults(self, size_bytes: int) -> dict`:
#    - Use `mmap.mmap(-1, size_bytes)` and track page faults on 1st touch and 2nd touch.
#    - Return dict with keys: 'first_touch_faults', 'second_touch_faults', 'first_touch_ms', 'second_touch_ms'.
#
# Un-comment the test code at the bottom of the file once you've written your solution!
# ================================================================================

# WRITE YOUR MemoryLifecycleProfiler CLASS HERE:




# --- EXERCISE 33 TEST CODE (Un-comment below to test your implementation) ---
# def run_exercise_tests():
#     print("\n==================================================")
#     print("RUNNING EXERCISE 33 TESTS")
#     print("==================================================")
#     
#     profiler = MemoryLifecycleProfiler()
#     res_c = profiler.profile_c_memory(16 * 1024 * 1024)
#     assert "alloc_ms" in res_c and "first_touch_ms" in res_c and "second_touch_ms" in res_c, "FAILED: Missing keys in C profile"
#     assert res_c["speedup"] >= 1.0, "FAILED: Expected 2nd touch speedup >= 1.0"
#     print(f"C Profile (16 MB): Alloc={res_c['alloc_ms']:.4f}ms, 1st Touch={res_c['first_touch_ms']:.4f}ms, 2nd Touch={res_c['second_touch_ms']:.4f}ms (Speedup: {res_c['speedup']:.2f}x)")
#     
#     res_pf = profiler.profile_page_faults(4 * 1024 * 1024)
#     assert "first_touch_faults" in res_pf and "second_touch_faults" in res_pf, "FAILED: Missing keys in page fault profile"
#     assert res_pf["second_touch_faults"] == 0, f"FAILED: Expected 0 faults on 2nd touch, got {res_pf['second_touch_faults']}"
#     print(f"Page Faults (4 MB): 1st Touch Faults={res_pf['first_touch_faults']}, 2nd Touch Faults={res_pf['second_touch_faults']}")
#     print("🎉 Exercise 33 Passed Successfully!")


def main():
    print("================================================================================")
    print("LESSON 33: MEMORY ALLOCATION, 1ST TOUCH VS. 2ND TOUCH ZEROING, AND DEALLOCATION")
    print("================================================================================")

    demonstrate_c_level_breakdown(64 * 1024 * 1024)
    demonstrate_kernel_page_faults(32 * 1024 * 1024)
    demonstrate_python_buffer_lifecycle(16 * 1024 * 1024, iters=10)
    run_scalability_benchmark()

    print("\n" + "=" * 80)
    print("KEY ARCHITECTURAL TAKEAWAYS")
    print("=" * 80)
    print("1. 1ST TOUCH ZEROING IS EXPENSIVE DUE TO OS PAGE FAULTS:")
    print("   - Allocating virtual address space is almost instantaneous.")
    print("   - 1st touch triggers kernel minor page faults and security zeroing.")
    print("\n2. 2ND TOUCH IS PURE MEMORY BUS WRITE (ZERO PAGE FAULTS):")
    print("   - 2nd touch bypasses all kernel traps and page table allocations.")
    print("   - Speedup ranges from 1.5x to 8x faster depending on CPU cache vs DRAM.")
    print("\n3. BUFFER POOLING EXPLOITS 2ND TOUCH ADVANTAGE:")
    print("   - Pre-allocated buffers operate exclusively in 2nd-touch mode.")
    print("=" * 80)

    # run_exercise_tests()


if __name__ == "__main__":
    main()
