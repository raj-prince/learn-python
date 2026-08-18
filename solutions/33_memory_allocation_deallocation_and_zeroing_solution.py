#!/usr/bin/env python3
"""
================================================================================
SOLUTION: LESSON 33 — MEMORY ALLOCATION, 1ST VS. 2ND TOUCH ZEROING, AND DEALLOCATION
================================================================================
"""

import time
import mmap
import resource
import ctypes
from typing import Dict

# Load standard C library functions
libc = ctypes.CDLL(None)
libc.malloc.restype = ctypes.c_void_p
libc.malloc.argtypes = [ctypes.c_size_t]
libc.free.argtypes = [ctypes.c_void_p]
libc.memset.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_size_t]


class MemoryLifecycleProfiler:
    """
    Diagnostic memory profiling utility for isolating virtual allocation,
    1st touch (cold) vs. 2nd touch (warm) zeroing, and deallocation latencies.
    """

    def profile_c_memory(self, size_bytes: int) -> Dict[str, float]:
        """
        Measures raw C-level malloc, 1st touch memset (cold), 2nd touch memset (warm),
        and free latency.
        """
        # 1. Virtual allocation
        t0 = time.perf_counter_ns()
        ptr = libc.malloc(size_bytes)
        alloc_ms = (time.perf_counter_ns() - t0) / 1e6

        # 2. 1st Touch (Cold zeroing with page faults)
        t0 = time.perf_counter_ns()
        libc.memset(ptr, 0, size_bytes)
        first_touch_ms = (time.perf_counter_ns() - t0) / 1e6

        # 3. 2nd Touch (Warm zeroing with 0 page faults)
        t0 = time.perf_counter_ns()
        libc.memset(ptr, 0, size_bytes)
        second_touch_ms = (time.perf_counter_ns() - t0) / 1e6

        # 4. Deallocation (free)
        t0 = time.perf_counter_ns()
        libc.free(ptr)
        free_ms = (time.perf_counter_ns() - t0) / 1e6

        # Calculate metrics
        speedup = first_touch_ms / max(second_touch_ms, 0.00001)
        bandwidth_gb_s = (size_bytes / (1024 ** 3)) / (second_touch_ms / 1000) if second_touch_ms > 0 else 0.0

        return {
            "alloc_ms": alloc_ms,
            "first_touch_ms": first_touch_ms,
            "second_touch_ms": second_touch_ms,
            "speedup": speedup,
            "free_ms": free_ms,
            "bandwidth_gb_s": bandwidth_gb_s,
        }

    def profile_page_faults(self, size_bytes: int) -> Dict[str, float]:
        """
        Measures minor page faults and latency during 1st touch vs. 2nd touch zeroing.
        """
        mm = mmap.mmap(-1, size_bytes, mmap.MAP_PRIVATE | mmap.MAP_ANONYMOUS)

        # --- 1st Touch ---
        f0 = resource.getrusage(resource.RUSAGE_SELF).ru_minflt
        t0 = time.perf_counter_ns()
        for i in range(0, size_bytes, 4096):
            mm[i] = 0
        first_touch_ms = (time.perf_counter_ns() - t0) / 1e6
        first_touch_faults = resource.getrusage(resource.RUSAGE_SELF).ru_minflt - f0

        # --- 2nd Touch ---
        f0 = resource.getrusage(resource.RUSAGE_SELF).ru_minflt
        t0 = time.perf_counter_ns()
        for i in range(0, size_bytes, 4096):
            mm[i] = 0
        second_touch_ms = (time.perf_counter_ns() - t0) / 1e6
        second_touch_faults = resource.getrusage(resource.RUSAGE_SELF).ru_minflt - f0

        mm.close()

        return {
            "first_touch_faults": first_touch_faults,
            "second_touch_faults": second_touch_faults,
            "first_touch_ms": first_touch_ms,
            "second_touch_ms": second_touch_ms,
        }


def run_exercise_tests():
    print("\n==================================================")
    print("RUNNING EXERCISE 33 TESTS")
    print("==================================================")

    profiler = MemoryLifecycleProfiler()
    res_c = profiler.profile_c_memory(16 * 1024 * 1024)
    assert "alloc_ms" in res_c and "first_touch_ms" in res_c and "second_touch_ms" in res_c, "FAILED: Missing keys in C profile"
    assert res_c["speedup"] >= 1.0, "FAILED: Expected 2nd touch speedup >= 1.0"
    print(f"C Profile (16 MB): Alloc={res_c['alloc_ms']:.4f}ms, 1st Touch={res_c['first_touch_ms']:.4f}ms, 2nd Touch={res_c['second_touch_ms']:.4f}ms (Speedup: {res_c['speedup']:.2f}x)")

    res_pf = profiler.profile_page_faults(4 * 1024 * 1024)
    assert "first_touch_faults" in res_pf and "second_touch_faults" in res_pf, "FAILED: Missing keys in page fault profile"
    assert res_pf["second_touch_faults"] == 0, f"FAILED: Expected 0 faults on 2nd touch, got {res_pf['second_touch_faults']}"
    print(f"Page Faults (4 MB): 1st Touch Faults={res_pf['first_touch_faults']}, 2nd Touch Faults={res_pf['second_touch_faults']}")
    print("🎉 Exercise 33 Passed Successfully!")


if __name__ == "__main__":
    run_exercise_tests()
