#!/usr/bin/env python3
"""
================================================================================
LESSON 28: EFFICIENT GENERIC LRU CACHE & FUNCTOOLS.LRU_CACHE MECHANICS
================================================================================

A Least Recently Used (LRU) cache is a fixed-capacity key-value store that evicts 
the least recently accessed item when full.

In Python, there are 3 major ways to implement or use LRU caches:

1. CUSTOM DUAL DATA STRUCTURE (`dict` + Doubly-Linked List `_Node`):
   - O(1) get/put/delete using slotted nodes and sentinel head/tail nodes.

2. STANDARD LIBRARY `collections.OrderedDict`:
   - Built-in C-optimized doubly-linked list with `.move_to_end()` and `.popitem(last=False)`.

3. STANDARD LIBRARY `functools.lru_cache`:
   - Function memoization decorator (`@lru_cache(maxsize=128)`).
   - Programmatic wrapper for expensive computational functions / API queries.
   - Safe instance method caching patterns (preventing `self` strong reference memory leaks).

--------------------------------------------------------------------------------
KEY CONCEPTS & DESIGN PATTERNS
--------------------------------------------------------------------------------
1. SLOTTED NODES (`__slots__`):
   Saves memory and speeds up attribute access (`prev`/`next`) by bypassing 
   the instance `__dict__`.

2. SENTINEL (DUMMY) BOUNDARY NODES:
   `head` sentinel represents MRU (Most Recently Used).
   `tail` sentinel represents LRU (Least Recently Used).
   Prevents special handling when adding to empty lists or removing single nodes.

3. GENERIC TYPING (`typing.Generic[K, V]`):
   Enables static type checking (mypy / pyright) for generic key and value types.

4. `collections.abc.MutableMapping`:
   Subclassing `MutableMapping` gives standard Python dictionary interface 
   (`cache[key] = val`, `key in cache`, `del cache[key]`, `.get()`, `.pop()`).

5. THREAD SAFETY (`threading.RLock`):
   Reentrant lock ensures thread-safe atomic operations across multiple threads.
"""

from __future__ import annotations
import time
import threading
import functools
from functools import lru_cache
from collections.abc import MutableMapping, Iterator
from typing import Generic, TypeVar, Optional, Any, Callable
from collections import OrderedDict

K = TypeVar("K")
V = TypeVar("V")


# ================================================================================
# PART 1: THE SLOTTED DOUBLY-LINKED LIST NODE
# ================================================================================

class _Node(Generic[K, V]):
    """Internal Doubly-Linked List Node with __slots__ for memory efficiency."""

    __slots__ = ("key", "val", "prev", "next")

    def __init__(self, key: Optional[K] = None, val: Optional[V] = None):
        self.key: Optional[K] = key
        self.val: Optional[V] = val
        self.prev: Optional[_Node[K, V]] = None
        self.next: Optional[_Node[K, V]] = None

    def __repr__(self) -> str:
        return f"Node({self.key}: {self.val})"


# ================================================================================
# PART 2: GENERIC LRU CACHE IMPLEMENTATION (HASH MAP + DLL)
# ================================================================================

class LRUCache(MutableMapping[K, V], Generic[K, V]):
    """
    Efficient Generic LRU Cache implementing MutableMapping.

    Time Complexity:
        - get() / __getitem__ : O(1)
        - put() / __setitem__ : O(1)
        - del / __delitem__   : O(1)
        - contains / in       : O(1)
    """

    def __init__(self, capacity: int, thread_safe: bool = False):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0")

        self.capacity: int = capacity
        self._cache: dict[K, _Node[K, V]] = {}

        # Sentinel dummy nodes (Head = Most Recently Used, Tail = Least Recently Used)
        self._head: _Node[K, V] = _Node()
        self._tail: _Node[K, V] = _Node()
        self._head.next = self._tail
        self._tail.prev = self._head

        # Stats
        self._hits: int = 0
        self._misses: int = 0
        self._evictions: int = 0

        # Optional thread safety lock
        self._lock: Optional[threading.RLock] = threading.RLock() if thread_safe else None

    def _add_to_head(self, node: _Node[K, V]) -> None:
        """Insert a node right after the head sentinel (MRU position)."""
        node.prev = self._head
        node.next = self._head.next
        assert self._head.next is not None
        self._head.next.prev = node
        self._head.next = node

    def _remove_node(self, node: _Node[K, V]) -> None:
        """Remove an existing node from the doubly linked list."""
        prev_node = node.prev
        next_node = node.next
        if prev_node is not None and next_node is not None:
            prev_node.next = next_node
            next_node.prev = prev_node

    def _move_to_head(self, node: _Node[K, V]) -> None:
        """Move an existing node to the MRU position."""
        self._remove_node(node)
        self._add_to_head(node)

    def _pop_tail(self) -> _Node[K, V]:
        """Remove and return the LRU node right before tail sentinel."""
        lru_node = self._tail.prev
        assert lru_node is not None and lru_node is not self._head
        self._remove_node(lru_node)
        return lru_node

    def __getitem__(self, key: K) -> V:
        if self._lock:
            with self._lock:
                return self._get_impl(key)
        return self._get_impl(key)

    def _get_impl(self, key: K) -> V:
        if key not in self._cache:
            self._misses += 1
            raise KeyError(key)

        self._hits += 1
        node = self._cache[key]
        self._move_to_head(node)
        return node.val  # type: ignore[return-value]

    def __setitem__(self, key: K, value: V) -> None:
        if self._lock:
            with self._lock:
                self._set_impl(key, value)
        else:
            self._set_impl(key, value)

    def _set_impl(self, key: K, value: V) -> None:
        if key in self._cache:
            node = self._cache[key]
            node.val = value
            self._move_to_head(node)
        else:
            if len(self._cache) >= self.capacity:
                lru_node = self._pop_tail()
                if lru_node.key is not None:
                    del self._cache[lru_node.key]
                    self._evictions += 1

            new_node = _Node(key, value)
            self._cache[key] = new_node
            self._add_to_head(new_node)

    def __delitem__(self, key: K) -> None:
        if self._lock:
            with self._lock:
                self._del_impl(key)
        else:
            self._del_impl(key)

    def _del_impl(self, key: K) -> None:
        if key not in self._cache:
            raise KeyError(key)
        node = self._cache.pop(key)
        self._remove_node(node)

    def __iter__(self) -> Iterator[K]:
        """Yield keys in MRU (Most Recently Used) to LRU order."""
        curr = self._head.next
        while curr is not None and curr is not self._tail:
            if curr.key is not None:
                yield curr.key
            curr = curr.next

    def __len__(self) -> int:
        return len(self._cache)

    def stats(self) -> dict[str, int]:
        return {
            "hits": self._hits,
            "misses": self._misses,
            "evictions": self._evictions,
            "currsize": len(self._cache),
            "maxsize": self.capacity,
        }


# ================================================================================
# PART 3: ALTERNATIVE IMPLEMENTATION USING COLLECTIONS.ORDEREDDICT
# ================================================================================

class OrderedDictLRU(MutableMapping[K, V], Generic[K, V]):
    """LRU Cache implemented using Python's built-in OrderedDict."""

    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0")
        self.capacity = capacity
        self._cache: OrderedDict[K, V] = OrderedDict()

    def __getitem__(self, key: K) -> V:
        val = self._cache[key]
        self._cache.move_to_end(key)  # Mark as MRU
        return val

    def __setitem__(self, key: K, value: V) -> None:
        if key in self._cache:
            self._cache.move_to_end(key)
        self._cache[key] = value
        if len(self._cache) > self.capacity:
            self._cache.popitem(last=False)  # Evict LRU (first item)

    def __delitem__(self, key: K) -> None:
        del self._cache[key]

    def __iter__(self) -> Iterator[K]:
        return iter(self._cache)

    def __len__(self) -> int:
        return len(self._cache)


# ================================================================================
# PART 4: GENERIC COMPUTATION CACHE USING FUNCTOOLS.LRU_CACHE
# ================================================================================

class FunctoolsMemoizedCache(Generic[K, V]):
    """
    Generic Computation Cache wrapping an expensive loader function 
    with `functools.lru_cache`.
    """

    def __init__(self, capacity: int, fetch_func: Callable[[K], V]):
        self.capacity = capacity
        # Dynamically wrap fetch_func with lru_cache
        self._cached_fetch = lru_cache(maxsize=capacity)(fetch_func)

    def get(self, key: K) -> V:
        """Retrieve cached result or compute and cache it."""
        return self._cached_fetch(key)

    def cache_info(self):
        """Return hits, misses, maxsize, currsize."""
        return self._cached_fetch.cache_info()

    def clear(self) -> None:
        """Clear all cached entries."""
        self._cached_fetch.cache_clear()


# ================================================================================
# PART 5: SAFE METHOD CACHING WITH FUNCTOOLS (PREVENTING MEMORY LEAKS)
# ================================================================================

class SafeCachedUserDatabase:
    """
    Shows how to use @functools.lru_cache with instance methods safely.

    PITFALL:
        Placing @lru_cache directly on an instance method holds `self` inside 
        the cache dictionary, preventing garbage collection of the instance!

    SAFE FIX:
        Create an instance-bound lru_cache in __init__ or use static/helper functions.
    """

    def __init__(self):
        # Instance-specific cache bound to this instance, cleaned up when instance is GC'd
        @lru_cache(maxsize=16)
        def _get_user_cached(user_id: int) -> dict[str, Any]:
            # Simulated slow DB query
            return {"user_id": user_id, "name": f"User_{user_id}", "status": "active"}

        self._get_user_cached = _get_user_cached

    def get_user(self, user_id: int) -> dict[str, Any]:
        return self._get_user_cached(user_id)


# ================================================================================
# DEMONSTRATION & BENCHMARKS
# ================================================================================

def demonstrate_functools_memoized_cache():
    print("=" * 80)
    print("PART 4: FUNCTOOLS-POWERED GENERIC COMPUTATION CACHE")
    print("=" * 80)

    # Simulated expensive computation (e.g. factorial / heavy operation)
    def expensive_square(n: int) -> int:
        print(f"   [COMPUTING] Calculating square for {n}...")
        return n * n

    cache = FunctoolsMemoizedCache[int, int](capacity=3, fetch_func=expensive_square)

    print("1. Fetching square for 5:")
    print("   Result:", cache.get(5))

    print("2. Fetching square for 5 again (Cache HIT):")
    print("   Result:", cache.get(5))

    print("3. Fetching square for 10 and 15:")
    cache.get(10)
    cache.get(15)

    print("4. Cache Info:", cache.cache_info())


def demonstrate_safe_method_caching():
    print("\n" + "=" * 80)
    print("PART 5: SAFE METHOD CACHING WITH FUNCTOOLS")
    print("=" * 80)

    db = SafeCachedUserDatabase()
    u1 = db.get_user(42)
    u2 = db.get_user(42)
    print(f"   Fetched user: {u1}")
    print(f"   Cache Info: {db._get_user_cached.cache_info()}")


def benchmark_all_implementations():
    print("\n" + "=" * 80)
    print("BENCHMARK — CUSTOM DLL vs ORDEREDDICT vs FUNCTOOLS CACHE")
    print("=" * 80)

    iterations = 300_000
    capacity = 1000

    # --------------------------------------------------------------------------
    # BENCHMARK 1: FAIR READ PERFORMANCE (get() on pre-populated cache)
    # --------------------------------------------------------------------------
    print("\n1. BENCHMARK: READ / LOOKUP PERFORMANCE (300,000 get() operations)")

    lru = LRUCache[int, int](capacity=capacity)
    od_lru = OrderedDictLRU[int, int](capacity=capacity)
    ft_cache = FunctoolsMemoizedCache[int, int](capacity=capacity, fetch_func=lambda x: x * 2)

    # Pre-populate all 3 caches
    for i in range(capacity):
        lru[i] = i
        od_lru[i] = i
        ft_cache.get(i)  # triggers initial load & cache store

    # Benchmark Custom LRUCache get()
    t0 = time.perf_counter()
    for i in range(iterations):
        _ = lru.get(i % capacity, None)
    t_custom_read = time.perf_counter() - t0

    # Benchmark OrderedDictLRU get()
    t0 = time.perf_counter()
    for i in range(iterations):
        _ = od_lru.get(i % capacity, None)
    t_od_read = time.perf_counter() - t0

    # Benchmark FunctoolsMemoizedCache get()
    t0 = time.perf_counter()
    for i in range(iterations):
        _ = ft_cache.get(i % capacity)
    t_ft_read = time.perf_counter() - t0

    print(f"   Custom DLL LRUCache      : {t_custom_read:.4f} sec")
    print(f"   OrderedDict LRUCache     : {t_od_read:.4f} sec ({t_custom_read/t_od_read:.2f}x faster than Custom)")
    print(f"   Functools MemoizedCache  : {t_ft_read:.4f} sec ({t_custom_read/t_ft_read:.2f}x faster than Custom)")

    # --------------------------------------------------------------------------
    # BENCHMARK 2: MIXED WRITE + READ WORKLOAD (set + get)
    # --------------------------------------------------------------------------
    print("\n2. BENCHMARK: WRITE + READ WORKLOAD (300,000 set + get operations)")

    lru_wr = LRUCache[int, int](capacity=capacity)
    od_wr = OrderedDictLRU[int, int](capacity=capacity)

    t0 = time.perf_counter()
    for i in range(iterations):
        lru_wr[i % 1500] = i
        _ = lru_wr.get(i % 1500, None)
    t_custom_wr = time.perf_counter() - t0

    t0 = time.perf_counter()
    for i in range(iterations):
        od_wr[i % 1500] = i
        _ = od_wr.get(i % 1500, None)
    t_od_wr = time.perf_counter() - t0

    print(f"   Custom DLL LRUCache      : {t_custom_wr:.4f} sec")
    print(f"   OrderedDict LRUCache     : {t_od_wr:.4f} sec ({t_custom_wr/t_od_wr:.2f}x faster than Custom)")


if __name__ == "__main__":
    demonstrate_functools_memoized_cache()
    demonstrate_safe_method_caching()
    benchmark_all_implementations()

