#!/usr/bin/env python3
"""
================================================================================
LESSON 29: BUFFER POOLS, OBJECT REUSE, AND CPYTHON MEMORY MECHANICS
================================================================================

In high-throughput applications (network socket processing, streaming file parsers,
real-time audio/video processing, database drivers), repeatedly allocating and
deallocating memory chunks creates heavy CPU overhead due to operating system `malloc()`
calls, memory fragmentation, and Garbage Collection (GC) pauses.

A **Buffer Pool** pre-allocates a set of reusable memory buffers or object instances,
recycling them across operations rather than allocating new objects on demand.

--------------------------------------------------------------------------------
CPYTHON INTERNAL MEMORY POOLING & FREE-LISTS
--------------------------------------------------------------------------------
CPython itself relies heavily on internal memory pools and free-lists:

1. Small Object Allocator (PyMalloc):
   - CPython manages memory for objects <= 512 bytes using `PyMalloc`.
   - Organizes memory into Arenas (256 KB), Pools (4 KB), and Blocks (8 to 512 bytes).

2. Small Integer Pre-allocation:
   - Integers from -5 to 256 are pre-allocated at Python startup in a global pool.
   - `a = 10` and `b = 10` point to the exact same object in memory (`id(a) == id(b)`).

3. String Interning:
   - Python automatically interns short strings matching identifier syntax (or via `sys.intern()`).
   - Enables fast O(1) pointer comparison (`is`) instead of O(N) string comparison (`==`).

4. Free-Lists (Object Reuse Pools):
   - CPython maintains internal free-lists for `float`, `tuple`, `list`, and `frame` objects.
   - When a float is destroyed, its C struct (`PyFloatObject`) is saved on a free-list to be
     reused immediately when a new float is created.

--------------------------------------------------------------------------------
I/O STREAM BUFFERING & CUSTOM BUFFER POOLS
--------------------------------------------------------------------------------
1. Stream Buffering (`io.DEFAULT_BUFFER_SIZE`):
   - `open()` and `io.BufferedReader`/`BufferedWriter` use an 8 KB internal buffer pool.
   - Reduces expensive operating system `read()` and `write()` kernel system calls by batching.

2. Zero-Copy Custom Buffer Pools:
   - By combining `bytearray` pre-allocation with `memoryview` slicing, application code
     can construct high-performance zero-copy buffer pools that eliminate GC overhead entirely.
"""

import sys
import time
import io
import threading
from collections import deque


# ================================================================================
# PART 1: CPYTHON INTERNAL MEMORY POOLING & FREE-LISTS
# ================================================================================

def demonstrate_cpython_internal_pools():
    print("\n" + "=" * 80)
    print("PART 1: CPYTHON INTERNAL MEMORY POOLING & FREE-LISTS")
    print("=" * 80)

    # 1. Small Integer Pool (-5 to 256)
    a = 42
    b = 42
    c = 300
    d = 300
    print(f"Small int pool (42 is 42)    : {a is b} (id(a)==id(b): {id(a) == id(b)})")
    print(f"Large int pool (300 is 300)  : {c is d} (id(c)==id(d): {id(c) == id(d)})")

    # 2. String Interning
    s1 = "hello_world_key"
    s2 = "hello_world_key"
    print(f"Auto-interned identifiers    : {s1 is s2}")

    # Manual interning for arbitrary strings
    raw_a = sys.intern("user_profile_id_999!@#")
    raw_b = sys.intern("user_profile_id_999!@#")
    print(f"Manual sys.intern()          : {raw_a is raw_b}")

    # 3. Float Free-List Demo
    f1 = 3.14159
    f1_id = id(f1)
    del f1  # Deallocating float returns its PyFloatObject struct to CPython's float free-list!
    f2 = 2.71828
    f2_id = id(f2)
    print(f"Float Struct Recycled        : {f1_id == f2_id} (f1 addr: {f1_id:#x}, f2 addr: {f2_id:#x})")


# ================================================================================
# PART 2: I/O STREAM BUFFERING (io.DEFAULT_BUFFER_SIZE)
# ================================================================================

def demonstrate_io_stream_buffering():
    print("\n" + "=" * 80)
    print("PART 2: I/O STREAM BUFFERING (io.DEFAULT_BUFFER_SIZE)")
    print("=" * 80)

    print(f"Default I/O Buffer Size in Python: {io.DEFAULT_BUFFER_SIZE} bytes ({io.DEFAULT_BUFFER_SIZE / 1024:.1f} KB)")

    # Unbuffered vs Buffered memory stream simulation
    buffer = io.BytesIO()
    payload = b"X" * 100

    start_t = time.perf_counter()
    for _ in range(10_000):
        buffer.write(payload)
    t_buffered = time.perf_counter() - start_t

    print(f"⏱️  Buffered 10,000 write ops time: {t_buffered:.5f} sec (Buffer Size: {len(buffer.getvalue()):,} bytes)")


# ================================================================================
# PART 3: CUSTOM ZERO-COPY REUSABLE BUFFER POOL
# ================================================================================

class BufferPool:
    """
    A thread-safe pool of fixed-size pre-allocated bytearray buffers.
    
    Prevents repeated malloc/free allocations and garbage collection overhead
    during intensive packet parsing or stream processing.
    """

    def __init__(self, capacity: int, buffer_size: int):
        self.buffer_size = buffer_size
        self._pool = deque([bytearray(buffer_size) for _ in range(capacity)])
        self._lock = threading.Lock()
        self._allocated = 0

    def acquire(self) -> bytearray:
        """Acquire a pre-allocated buffer from the pool."""
        with self._lock:
            if self._pool:
                self._allocated += 1
                return self._pool.popleft()
            # Pool exhausted: fallback to creating a new buffer
            self._allocated += 1
            return bytearray(self.buffer_size)

    def release(self, buf: bytearray):
        """Return a buffer to the pool for future reuse."""
        if len(buf) != self.buffer_size:
            return  # Invalid buffer size, ignore
        with self._lock:
            self._pool.append(buf)
            self._allocated -= 1

    def pool_status(self) -> tuple[int, int]:
        """Returns (available_buffers, active_in_use_buffers)."""

        with self._lock:
            return len(self._pool), self._allocated


def demonstrate_buffer_pool_performance():
    print("\n" + "=" * 80)
    print("PART 3: BENCHMARK — REPEATED MALLOC vs REUSABLE BUFFER POOL")
    print("=" * 80)

    iterations = 50_000
    buf_size = 65_536  # 64 KB buffers (typical network packet / file chunk size)

    print(f"📦 Buffer Size: {buf_size / 1024:.0f} KB | Total Operations: {iterations:,}")

    # 1. Benchmark Repeated Allocation (malloc + OS memory zeroing per iteration)
    start_t = time.perf_counter()
    for _ in range(iterations):
        buf = bytearray(buf_size)
        buf[0] = 65  # Simulating buffer use
        _ = buf[0]
        del buf
    t_malloc = time.perf_counter() - start_t

    # 2. Benchmark Reusable Buffer Pool
    pool = BufferPool(capacity=16, buffer_size=buf_size)
    start_t = time.perf_counter()
    for _ in range(iterations):
        buf = pool.acquire()
        buf[0] = 65  # Simulating buffer use
        _ = buf[0]
        pool.release(buf)
    t_pool = time.perf_counter() - start_t

    speedup = t_malloc / max(t_pool, 0.000001)

    print(f"⏱️  Repeated Allocations (`bytearray(64KB)`): {t_malloc:.4f} sec")
    print(f"⏱️  Reusable Buffer Pool (`pool.acquire()`):   {t_pool:.4f} sec")
    print(f"🚀 Speedup Factor:                             {speedup:.2f}x faster!")
    print("\n💡 Key Insight: For large payloads (>= 64 KB), OS memory allocation and zeroing")
    print("   dominates CPU time. Buffer pooling bypasses page allocation completely!")



# ================================================================================
# YOUR TURN: EXERCISE 29
# ================================================================================
# Scenario:
# You are building a high-performance network packet processor. Packets arrive 
# rapidly and must be written into pre-allocated memory slots, processed, and 
# then the slots recycled.
#
# INSTRUCTIONS:
# 1. Create a class `PacketBufferPool`.
# 2. In `__init__(self, slot_count: int, slot_size: int)`:
#    - Store `slot_size`.
#    - Initialize a deque `self._free_slots` populated with `slot_count` bytearray buffers of size `slot_size`.
#    - Initialize an integer counter `self.reused_count = 0` to track how many times a pooled buffer was reused.
# 3. Implement `get_slot(self) -> bytearray`:
#    - If `self._free_slots` has buffers, pop and return one, and increment `self.reused_count`.
#    - Otherwise, return a new `bytearray(self.slot_size)`.
# 4. Implement `recycle_slot(self, buf: bytearray)`:
#    - Append `buf` back to `self._free_slots`.
# 5. Add method `available_slots(self) -> int`:
#    - Return `len(self._free_slots)`.
#
# Un-comment the test code at the bottom of the file once you've written your solution!
# ================================================================================

# WRITE YOUR PacketBufferPool CLASS HERE:




# --- EXERCISE 29 TEST CODE (Un-comment below to test your implementation) ---
# def run_exercise_tests():
#     print("\n==================================================")
#     print("RUNNING EXERCISE 29 TESTS")
#     print("==================================================")
#     
#     pool = PacketBufferPool(slot_count=4, slot_size=1024)
#     assert pool.available_slots() == 4, f"FAILED: Expected 4 slots, got {pool.available_slots()}"
#     
#     slot1 = pool.get_slot()
#     slot2 = pool.get_slot()
#     assert len(slot1) == 1024, "FAILED: Slot size is incorrect"
#     assert pool.available_slots() == 2, f"FAILED: Expected 2 available slots, got {pool.available_slots()}"
#     
#     pool.recycle_slot(slot1)
#     assert pool.available_slots() == 3, "FAILED: Slot was not recycled"
#     
#     slot3 = pool.get_slot()
#     assert pool.reused_count == 3, f"FAILED: Expected reused_count 3, got {pool.reused_count}"
#     print(f"Pool status: Available={pool.available_slots()}, Reused Count={pool.reused_count}")
#     print("🎉 Exercise 29 Passed Successfully!")


if __name__ == "__main__":
    demonstrate_cpython_internal_pools()
    demonstrate_io_stream_buffering()
    demonstrate_buffer_pool_performance()
    # run_exercise_tests()
