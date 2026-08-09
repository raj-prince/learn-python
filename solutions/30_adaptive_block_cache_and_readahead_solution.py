#!/usr/bin/env python3
"""
================================================================================
SOLUTION: LESSON 30 — ADAPTIVE BLOCK CACHE & KERNEL READAHEAD MECHANICS
================================================================================
"""

import sys
import time
import importlib
from pathlib import Path

# Dynamic import for module starting with number
repo_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(repo_root))

mod_30 = importlib.import_module("30_adaptive_block_cache_and_readahead")
AdaptiveNetworkBlockCache = mod_30.AdaptiveNetworkBlockCache
mock_network_fetcher = mod_30.mock_network_fetcher


class PrefetchingFileReader:
    """
    High-level reader wrapping AdaptiveNetworkBlockCache to track statistics.
    """

    def __init__(self, fetcher, max_readahead: int = 8):
        self.fetcher = fetcher
        self.max_readahead = max_readahead
        self.cache = AdaptiveNetworkBlockCache(fetcher, max_readahead=max_readahead)
        self.hit_count = 0
        self.miss_count = 0

    def read(self, block_index: int) -> bytes:
        """Reads block_index and tracks hits vs misses."""
        if block_index in self.cache._cache:
            self.hit_count += 1
        else:
            self.miss_count += 1

        return self.cache.read_block(block_index)

    def get_stats(self) -> dict:
        """Returns cache stats."""
        return {
            "hits": self.hit_count,
            "misses": self.miss_count,
            "window": self.cache.current_window(),
        }


def run_exercise_tests():
    print("\n==================================================")
    print("RUNNING EXERCISE 30 TESTS")
    print("==================================================")
    
    reader = PrefetchingFileReader(mock_network_fetcher, max_readahead=8)
    
    # Sequential reads: block 0 (miss), blocks 1..5 (hits due to prefetch)
    for i in range(6):
        reader.read(i)
        time.sleep(0.02)
        
    stats = reader.get_stats()
    print("Reader Stats:", stats)
    assert stats["hits"] > 0, "FAILED: Expected hits from prefetching!"
    assert stats["window"] > 1, "FAILED: Window should have expanded on sequential reads"
    reader.cache.close()
    print("🎉 Exercise 30 Passed Successfully!")


if __name__ == "__main__":
    run_exercise_tests()
