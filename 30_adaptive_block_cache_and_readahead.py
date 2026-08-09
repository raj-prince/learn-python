#!/usr/bin/env python3
"""
================================================================================
LESSON 30: ADAPTIVE BLOCK CACHE & KERNEL READ-AHEAD MECHANICS
================================================================================

In storage systems, database engines, and network file readers (like `fsspec`, `s3fs`,
and cloud storage APIs), reading data block-by-block over a high-latency network
creates severe performance bottlenecks if every block requires a synchronous request.

To maximize throughput while controlling memory usage, production systems implement
**Adaptive Read-Ahead Logic** inspired by the Linux kernel (`mm/readahead.c`).

--------------------------------------------------------------------------------
CORE READ-AHEAD ALGORITHM MECHANICS
--------------------------------------------------------------------------------
1. Pattern Recognition:
   - Sequential Reads (Blocks N, N+1, N+2): The application is reading sequentially.
     The readahead window grows exponentially (1 -> 2 -> 4 -> 8 -> ... -> max_readahead).
   - Random Reads (Non-sequential jumps like N to N+50): The application is seeking randomly.
     The readahead window resets to min_readahead (1 block) to avoid wasteful network traffic.

2. Dynamic Memory Pressure Throttling:
   - Under low memory pressure, the readahead ceiling scales up to max_readahead.
   - Under high memory pressure (system RAM usage > 80% or > 90%), the readahead ceiling
     is dynamically throttled down to prevent Out-Of-Memory (OOM) crashes.

3. Asynchronous Prefetch Workers:
   - Upcoming blocks (N+1 ... N+window) are fetched concurrently in background worker threads.
   - Subsequent sequential `read()` calls hit the pre-fetched cache with zero network latency.

4. Bounded LRU Cache Eviction:
   - Blocks are stored in an `OrderedDict` with a maximum capacity. Least Recently Used (LRU)
     blocks are evicted when capacity is reached.
"""

import time
import psutil
import threading
from collections import OrderedDict
from concurrent.futures import ThreadPoolExecutor
from typing import Callable, Optional


# ================================================================================
# PART 1: ADAPTIVE READAHEAD BLOCK CACHE CLASS
# ================================================================================

class AdaptiveNetworkBlockCache:
    """
    Network Block Cache with adaptive readahead logic inspired by Linux `mm/readahead.c`.
    """

    def __init__(
        self,
        fetcher: Callable[[int], bytes],
        block_size: int = 64 * 1024,      # 64 KB per block
        max_cache_blocks: int = 64,        # Max cache size (e.g. 4 MB)
        min_readahead: int = 1,             # Minimum readahead blocks
        max_readahead: int = 16,            # Maximum readahead blocks
        num_prefetch_workers: int = 4
    ):
        self.fetcher = fetcher
        self.block_size = block_size
        self.max_cache_blocks = max_cache_blocks
        self.min_readahead = min_readahead
        self.max_readahead = max_readahead

        self._cache = OrderedDict()         # block_index -> bytes
        self._lock = threading.Lock()
        
        # State tracking (Linux readahead.c pattern)
        self._last_requested_block = -1
        self._current_window = min_readahead

        # Background pre-fetch thread pool
        self._prefetch_pool = ThreadPoolExecutor(
            max_workers=num_prefetch_workers,
            thread_name_prefix="ReadaheadWorker"
        )

    # --------------------------------------------------------------------------
    # MEMORY PRESSURE EVALUATION
    # --------------------------------------------------------------------------
    def _get_memory_pressure_scale(self) -> float:
        """Returns a scaling factor between 0.1 and 1.0 based on system RAM pressure."""
        mem_percent = psutil.virtual_memory().percent
        if mem_percent > 90:
            return 0.1   # Severe pressure: drop readahead to ~10%
        elif mem_percent > 80:
            return 0.5   # Moderate pressure: drop readahead to 50%
        return 1.0       # Normal operation

    def effective_max_readahead(self) -> int:
        """Calculates max readahead window adjusted for current memory pressure."""
        scale = self._get_memory_pressure_scale()
        return max(self.min_readahead, int(self.max_readahead * scale))

    # --------------------------------------------------------------------------
    # CORE READ & ADAPTIVE READAHEAD ENGINE
    # --------------------------------------------------------------------------
    def read_block(self, block_index: int) -> bytes:
        """
        Reads a block by index. Updates pattern detection, triggers background 
        readahead for future blocks, and returns the requested data.
        """
        with self._lock:
            # Step A: Pattern Recognition & Readahead Window Adjustment
            if block_index == self._last_requested_block + 1:
                # Sequential Access: Exponential expansion up to effective max limit
                effective_max = self.effective_max_readahead()
                self._current_window = min(self._current_window * 2, effective_max)
                pattern = "SEQUENTIAL (EXPAND)"
            else:
                # Random / Out-of-Order Access: Reset window to min_readahead
                self._current_window = self.min_readahead
                pattern = "RANDOM (RESET)"

            self._last_requested_block = block_index
            window_size = self._current_window

            print(
                f"  [ReadBlock {block_index:3d}] Access: {pattern:19s} | "
                f"Readahead Window: {window_size:2d} blocks | "
                f"RAM: {psutil.virtual_memory().percent:.1f}%"
            )

            # Step B: Asynchronously Schedule Background Readahead (N+1 ... N+window)
            for ahead_idx in range(block_index + 1, block_index + 1 + window_size):
                if ahead_idx not in self._cache:
                    self._prefetch_pool.submit(self._async_prefetch, ahead_idx)

            # Step C: Retrieve Block Data (Cache Hit vs Cache Miss)
            if block_index in self._cache:
                self._cache.move_to_end(block_index)
                return self._cache[block_index]

        # Cache Miss: Synchronously fetch target block
        data = self.fetcher(block_index)
        self._store_in_cache(block_index, data)
        return data

    def _async_prefetch(self, block_index: int):
        """Worker thread task for fetching upcoming blocks in background."""
        with self._lock:
            if block_index in self._cache:
                return

        # Fetch over network without holding lock
        data = self.fetcher(block_index)
        self._store_in_cache(block_index, data)

    def _store_in_cache(self, block_index: int, data: bytes):
        """Stores block in OrderedDict and evicts LRU blocks if max_cache_blocks reached."""
        with self._lock:
            self._cache[block_index] = data
            self._cache.move_to_end(block_index)
            if len(self._cache) > self.max_cache_blocks:
                self._cache.popitem(last=False)  # Evict Least Recently Used block

    def current_window(self) -> int:
        with self._lock:
            return self._current_window

    def close(self):
        self._prefetch_pool.shutdown(wait=False)


# ================================================================================
# PART 2: DEMONSTRATING SEQUENTIAL VS RANDOM PATTERN ADAPTATION
# ================================================================================

def mock_network_fetcher(block_index: int) -> bytes:
    """Simulates network latency (e.g. S3 / HTTP byte-range request)."""
    time.sleep(0.01)
    return f"DATA_FOR_BLOCK_{block_index}".encode()


def demonstrate_adaptive_readahead():
    print("\n" + "=" * 80)
    print("DEMONSTRATING ADAPTIVE KERNEL-STYLE READAHEAD")
    print("=" * 80)

    cache = AdaptiveNetworkBlockCache(
        fetcher=mock_network_fetcher,
        min_readahead=1,
        max_readahead=8
    )

    print("1. Sequential Read Stream (Expect window to double: 2 -> 4 -> 8):")
    for block_num in range(6):
        _data = cache.read_block(block_num)
        time.sleep(0.02)  # Allow background threads to prefetch

    print("\n2. Random Seek (Expect window to reset to 1):")
    _data = cache.read_block(100)
    _data = cache.read_block(250)

    print("\n3. Resuming Sequential Read Stream (Expect window to double again):")
    _data = cache.read_block(251)
    _data = cache.read_block(252)

    cache.close()


# ================================================================================
# YOUR TURN: EXERCISE 30
# ================================================================================
# Scenario:
# You are extending a remote file reader. You need to implement a class 
# `PrefetchingFileReader` that tracks total hits, misses, and current window size.
#
# INSTRUCTIONS:
# 1. Create a class `PrefetchingFileReader`.
# 2. In `__init__(self, fetcher, max_readahead: int = 8)`:
#    - Store `fetcher` and `max_readahead`.
#    - Initialize `self.cache = AdaptiveNetworkBlockCache(fetcher, max_readahead=max_readahead)`.
#    - Initialize counters `self.hit_count = 0` and `self.miss_count = 0`.
# 3. Implement `read(self, block_index: int) -> bytes`:
#    - Check if `block_index` is in `self.cache._cache`.
#    - If hit, increment `self.hit_count`. If miss, increment `self.miss_count`.
#    - Call and return `self.cache.read_block(block_index)`.
# 4. Implement `get_stats(self) -> dict`:
#    - Return `{"hits": self.hit_count, "misses": self.miss_count, "window": self.cache.current_window()}`.
#
# Un-comment the test code at the bottom of the file once you've written your solution!
# ================================================================================

# WRITE YOUR PrefetchingFileReader CLASS HERE:




# --- EXERCISE 30 TEST CODE (Un-comment below to test your implementation) ---
# def run_exercise_tests():
#     print("\n==================================================")
#     print("RUNNING EXERCISE 30 TESTS")
#     print("==================================================")
#     
#     reader = PrefetchingFileReader(mock_network_fetcher, max_readahead=8)
#     
#     # Sequential reads: block 0 (miss), blocks 1..5 (hits due to prefetch)
#     for i in range(6):
#         reader.read(i)
#         time.sleep(0.02)
#         
#     stats = reader.get_stats()
#     print("Reader Stats:", stats)
#     assert stats["hits"] > 0, "FAILED: Expected hits from prefetching!"
#     assert stats["window"] > 1, "FAILED: Window should have expanded on sequential reads"
#     reader.cache.close()
#     print("🎉 Exercise 30 Passed Successfully!")


if __name__ == "__main__":
    demonstrate_adaptive_readahead()
    # run_exercise_tests()
