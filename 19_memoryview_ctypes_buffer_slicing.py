#!/usr/bin/env python3
"""
================================================================================
LESSON 19: MEMORYVIEW, CTYPES MEMMOVE, AND BUFFER SLICING OVERHEAD
================================================================================

When working with binary data, large buffers, multi-threading, or multi-processing,
how you slice and copy memory has a massive impact on performance.

In this lesson, we compare three memory management techniques in Python:
1. Normal Buffer Slicing (`bytes[a:b]` / `bytearray[a:b]`)
2. Memoryview Slicing (`memoryview(buf)[a:b]`)
3. `ctypes.memmove(dst, src, count)`

--------------------------------------------------------------------------------
SUMMARY OF MECHANICS & OVERHEAD
--------------------------------------------------------------------------------
1. Standard Slicing (`bytes[a:b]`):
   - O(N) Time & Space Complexity (where N = slice size).
   - Allocates a NEW Python object and copies all bytes into new memory.
   - High memory allocation and Garbage Collection (GC) overhead.
   - Holds the GIL during allocation and memory copying.

2. `memoryview` (`memoryview(buf)[a:b]`):
   - O(1) Time & Space Complexity (Zero-copy!).
   - Uses CPython's Buffer Protocol (`Py_buffer`).
   - Slicing creates a small (~200 byte) view wrapper pointing directly to 
     the existing buffer's memory address offset.
   - Ideal for single-process multi-threaded concurrent reads (thread-safe on immutable bytes).
   - Standard library methods (sockets, files, zlib, OpenSSL) release GIL when operating on memoryview!

3. `ctypes.memmove(dst, src, count)`:
   - Direct wrapper for C libc `memmove(3)` / `memcpy`.
   - O(N) memory copy executed at raw C SIMD speed.
   - Zero object allocation (operates directly on pre-allocated memory addresses).
   - RELEASES THE GIL in CPython during large memory copies! Enables true CPU-level 
     parallel bulk writes across multiple threads.

--------------------------------------------------------------------------------
MULTI-THREADING VS MULTI-PROCESSING SUMMARY
--------------------------------------------------------------------------------
- MULTI-THREADING (Shared Address Space):
  * Use `memoryview` for zero-copy slicing and thread-safe concurrent reads.
  * Use `ctypes.memmove` for fast, parallel multi-threaded writes into distinct buffer regions (releases GIL!).

- MULTI-PROCESSING (Isolated Address Spaces):
  * Passing normal slices over IPC (Queue/Pipe) incurs double/triple copy overhead (slice copy + pickling).
  * Combine `memoryview` with `multiprocessing.shared_memory.SharedMemory` for true ZERO-COPY 
    cross-process data slicing!
  * Use `ctypes.memmove` to write process worker outputs directly into target slices of shared memory.
"""

import time
import ctypes
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import shared_memory, Process

# ================================================================================
# PART 1: SLICE CREATION OVERHEAD (O(N) COPY vs O(1) ZERO-COPY VIEW)
# ================================================================================

def demonstrate_slice_creation_overhead():
    print("\n" + "=" * 80)
    print("PART 1: SLICE CREATION OVERHEAD (O(N) COPY vs O(1) ZERO-COPY VIEW)")
    print("=" * 80)

    buffer_size = 50_000_000  # 50 MB
    slice_size = 10_000_000   # 10 MB slice
    iterations = 200

    print(f"📦 Source Buffer: {buffer_size / 1e6:.1f} MB | Slice Request: {slice_size / 1e6:.1f} MB | Iterations: {iterations}")

    raw_bytes = bytes(buffer_size)
    raw_ba = bytearray(buffer_size)
    mv = memoryview(raw_ba)

    # 1. Standard Bytes Slicing
    start_t = time.perf_counter()
    for _ in range(iterations):
        _s = raw_bytes[1000:1000 + slice_size]
    t_bytes = (time.perf_counter() - start_t) / iterations * 1000  # ms per op

    # 2. memoryview Slicing
    start_t = time.perf_counter()
    for _ in range(iterations):
        _s = mv[1000:1000 + slice_size]
    t_mv = (time.perf_counter() - start_t) / iterations * 1000  # ms per op

    speedup = t_bytes / max(t_mv, 0.000001)

    print(f"⏱️  Bytes Slicing (`bytes[a:b]`):             {t_bytes:.4f} ms/op  (O(N) allocation + copy)")
    print(f"⏱️  Memoryview Slicing (`mv[a:b]`):          {t_mv:.4f} ms/op  (O(1) zero-copy pointer window)")
    print(f"🚀 Speedup Factor:                           {speedup:.1f}x faster!")


# ================================================================================
# PART 2: IN-PLACE BUFFER COPYING (UPDATING PRE-ALLOCATED MEMORY)
# ================================================================================

def demonstrate_in_place_copying():
    print("\n" + "=" * 80)
    print("PART 2: IN-PLACE BUFFER COPYING (UPDATING PRE-ALLOCATED MEMORY)")
    print("=" * 80)

    buffer_size = 30_000_000  # 30 MB
    copy_size = 5_000_000     # 5 MB copy payload
    iterations = 100

    src_ba = bytearray(buffer_size)
    dst_ba = bytearray(buffer_size)

    src_mv = memoryview(src_ba)
    dst_mv = memoryview(dst_ba)

    # 1. Bytes slice copy (Creates temporary bytes object, then copies)
    start_t = time.perf_counter()
    for _ in range(iterations):
        dst_ba[1000:1000 + copy_size] = src_ba[1000:1000 + copy_size]
    t_bytes_copy = (time.perf_counter() - start_t) / iterations * 1000

    # 2. Memoryview slice assignment (Direct C buffer transfer, no temp objects)
    start_t = time.perf_counter()
    for _ in range(iterations):
        dst_mv[1000:1000 + copy_size] = src_mv[1000:1000 + copy_size]
    t_mv_copy = (time.perf_counter() - start_t) / iterations * 1000

    # 3. ctypes.memmove (Direct C libc memmove call)
    src_ptr = (ctypes.c_char * buffer_size).from_buffer(src_ba)
    dst_ptr = (ctypes.c_char * buffer_size).from_buffer(dst_ba)
    src_addr = ctypes.addressof(src_ptr) + 1000
    dst_addr = ctypes.addressof(dst_ptr) + 1000

    start_t = time.perf_counter()
    for _ in range(iterations):
        ctypes.memmove(dst_addr, src_addr, copy_size)
    t_memmove_copy = (time.perf_counter() - start_t) / iterations * 1000

    print(f"📋 Copying {copy_size / 1e6:.1f} MB into destination buffer:")
    print(f"⏱️  Bytes Slice Copy (`dst[a:b] = src[a:b]`):      {t_bytes_copy:.4f} ms  (Creates temp bytes slice object)")
    print(f"⏱️  Memoryview Slice Copy (`dst_mv[a:b] = src_mv`): {t_mv_copy:.4f} ms  (Direct buffer transfer, 0 temp objects)")
    print(f"⏱️  ctypes.memmove (`ctypes.memmove(...)`):       {t_memmove_copy:.4f} ms  (Direct libc SIMD copy)")


# ================================================================================
# PART 3: MULTI-THREADING (GIL RELEASE & CONCURRENT READS)
# ================================================================================

def _threaded_writer_memmove(dst_addr: int, src_addr: int, size: int):
    """Helper function to perform ctypes.memmove across threads."""
    ctypes.memmove(dst_addr, src_addr, size)

def demonstrate_multithreading_concurrency():
    print("\n" + "=" * 80)
    print("PART 3: MULTI-THREADING (GIL RELEASE WITH CTYPES MEMMOVE & CONCURRENT READS)")
    print("=" * 80)

    chunk_size = 10_000_000  # 10 MB per chunk
    num_threads = 4
    total_size = chunk_size * num_threads

    src_ba = bytearray(b"X" * total_size)
    dst_ba = bytearray(total_size)

    src_ptr = (ctypes.c_char * total_size).from_buffer(src_ba)
    dst_ptr = (ctypes.c_char * total_size).from_buffer(dst_ba)

    # Launching parallel thread writes using ctypes.memmove (releases GIL in CPython)
    start_t = time.perf_counter()
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = []
        for i in range(num_threads):
            s_addr = ctypes.addressof(src_ptr) + (i * chunk_size)
            d_addr = ctypes.addressof(dst_ptr) + (i * chunk_size)
            futures.append(executor.submit(_threaded_writer_memmove, d_addr, s_addr, chunk_size))
        for f in futures:
            f.result()
    t_parallel = (time.perf_counter() - start_t) * 1000

    print(f"🧵 Multi-Threaded Parallel Copy ({num_threads} threads writing {chunk_size/1e6:.1f} MB each):")
    print(f"⏱️  Total Parallel Transfer Time: {t_parallel:.4f} ms")
    print(f"✅ Verified Data Integrity: {dst_ba[:10] == b'XXXXXXXXXX'}")


# ================================================================================
# PART 4: MULTI-PROCESSING & POSIX SHARED MEMORY (ZERO-COPY CROSS-PROCESS)
# ================================================================================

def _child_process_worker(shm_name: str, offset: int, size: int):
    """Child process worker accessing shared memory zero-copy via memoryview."""
    # Attach to existing shared memory segment created by parent process
    existing_shm = shared_memory.SharedMemory(name=shm_name)
    try:
        msg = f"WORKER_{offset}".encode("utf-8").ljust(size, b".")
        ba_msg = bytearray(msg)
        
        src_ptr = (ctypes.c_char * len(ba_msg)).from_buffer(ba_msg)
        dst_ptr = (ctypes.c_char * len(existing_shm.buf)).from_buffer(existing_shm.buf)
        
        dst_addr = ctypes.addressof(dst_ptr) + offset
        src_addr = ctypes.addressof(src_ptr)
        ctypes.memmove(dst_addr, src_addr, len(msg))
        
        # Must delete buffer reference objects before closing shared memory
        del src_ptr
        del dst_ptr
    finally:
        existing_shm.close()

def demonstrate_multiprocessing_shared_memory():
    print("\n" + "=" * 80)
    print("PART 4: MULTI-PROCESSING & POSIX SHARED MEMORY (ZERO-COPY CROSS-PROCESS)")
    print("=" * 80)

    total_shm_size = 50_000_000  # 50 MB Shared Memory block
    shm = shared_memory.SharedMemory(create=True, size=total_shm_size)

    try:
        print(f"🖥️  Created POSIX Shared Memory segment '{shm.name}' of size {total_shm_size / 1e6:.1f} MB")
        
        # Spawn child worker processes modifying non-overlapping memory slices
        p1 = Process(target=_child_process_worker, args=(shm.name, 0, 100))
        p2 = Process(target=_child_process_worker, args=(shm.name, 1000, 100))

        p1.start()
        p2.start()

        p1.join()
        p2.join()

        # Parent process inspects shared buffer zero-copy
        parent_mv = memoryview(shm.buf)
        output_worker1 = bytes(parent_mv[0:30])
        output_worker2 = bytes(parent_mv[1000:1030])
        
        print(f"✨ Parent process read worker 1 output: {output_worker1}")
        print(f"✨ Parent process read worker 2 output: {output_worker2}")

        parent_mv.release()
    finally:
        shm.close()
        shm.unlink()
        print("🧹 Cleaned up POSIX Shared Memory segment.")


# ================================================================================
# MAIN LESSON EXECUTION
# ================================================================================

def main():
    print("================================================================================")
    print("LESSON 19: MEMORYVIEW, CTYPES MEMMOVE, AND BUFFER SLICING OVERHEAD")
    print("================================================================================")

    demonstrate_slice_creation_overhead()
    demonstrate_in_place_copying()
    demonstrate_multithreading_concurrency()
    demonstrate_multiprocessing_shared_memory()

    print("\n" + "=" * 80)
    print("SUMMARY COMPARISON TABLE")
    print("=" * 80)
    print(f"{'Feature':<25} | {'bytes[a:b]':<18} | {'memoryview':<18} | {'ctypes.memmove':<18}")
    print("-" * 88)
    print(f"{'Slice Complexity':<25} | {'O(N) (Copy)':<18} | {'O(1) (Zero-Copy)':<18} | {'N/A (Copy op)':<18}")
    print(f"{'Memory Overhead':<25} | {'High (New Object)':<18} | {'Tiny (~200B View)':<18} | {'Zero Allocation':<18}")
    print(f"{'GC Pressure':<25} | {'High':<18} | {'Minimal':<18} | {'None':<18}")
    print(f"{'GIL Release (CPython)':<25} | {'No':<18} | {'On I/O methods':<18} | {'Yes (Releases GIL)':<18}")
    print(f"{'Multi-Threading Use':<25} | {'Avoid for large data':<18} | {'Concurrent Reads':<18} | {'Parallel Writes':<18}")
    print(f"{'Multi-Processing Use':<25} | {'IPC Pickle Penalty':<18} | {'SharedMemory View':<18} | {'Direct SHM Writes':<18}")

if __name__ == "__main__":
    main()
