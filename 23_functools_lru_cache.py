#!/usr/bin/env python3
"""
================================================================================
LESSON 23: FUNCTOOLS.LRU_CACHE — MEMOIZATION & CACHING MECHANICS
================================================================================

The `@lru_cache` decorator from Python's standard `functools` module adds 
Least Recently Used (LRU) memoization to any function.

Memoization caches function return values for specific input arguments, turning 
expensive computational calls ($O(2^N)$ algorithms like recursive Fibonacci, 
database queries, API calls) into instant $O(1)$ dictionary lookups!

--------------------------------------------------------------------------------
KEY PARAMETERS & FUNCTIONS
--------------------------------------------------------------------------------
1. `@lru_cache(maxsize=128, typed=False)`:
   - `maxsize`: Maximum number of call results retained. 
     When the cache fills up, the least recently used item is evicted.
     If `maxsize=None`, the cache grows unbounded with no eviction.
   - `typed`: If `True`, arguments of different types are cached separately 
     (e.g., `func(3)` and `func(3.0)` create separate cache entries).

2. `@functools.cache` (Python 3.9+):
   - A faster shortcut equivalent to `@lru_cache(maxsize=None)` (unbounded cache).

3. Cache Inspection & Management Methods:
   - `func.cache_info()`  : Returns `CacheInfo(hits, misses, maxsize, currsize)`.
   - `func.cache_clear()` : Flushes all cached results and resets statistics.
   - `func.__wrapped__`   : Accesses the original, uncached function directly.

--------------------------------------------------------------------------------
IMPORTANT GOTCHAS & PITFALLS
--------------------------------------------------------------------------------
1. HASHABLE ARGUMENTS ONLY:
   All arguments passed to an `@lru_cache` function MUST be hashable.
   Passing a `list` or `dict` raises `TypeError: unhashable type: 'list'`.
   Fix: Pass `tuple` or `frozenset` instead!

2. METHOD CACHING MEMORY LEAK:
   Applying `@lru_cache` directly on an instance method holds a strong reference 
   to `self`, preventing garbage collection of the instance!

3. FUNCTIONS WITH SIDE EFFECTS:
   Do NOT use `@lru_cache` on functions that write to files, send network 
   payloads, or rely on mutable global state.
"""

import time
import functools
from functools import lru_cache, cache


# ================================================================================
# PART 1: EXPONENTIAL RECURSION TO INSTANT LOOKUP (FIBONACCI BENCHMARK)
# ================================================================================

def slow_fibonacci(n: int) -> int:
    """Uncached recursive Fibonacci — O(2^N) time complexity!"""
    if n < 2:
        return n
    return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)


@lru_cache(maxsize=128)
def fast_fibonacci(n: int) -> int:
    """Cached recursive Fibonacci — O(N) time complexity!"""
    if n < 2:
        return n
    return fast_fibonacci(n - 1) + fast_fibonacci(n - 2)


def demonstrate_fibonacci_speedup():
    print("\n" + "=" * 80)
    print("PART 1: EXPONENTIAL O(2^N) TO O(N) MEMOIZATION SPEEDUP")
    print("=" * 80)

    n_val = 35

    # 1. Uncached Fibonacci
    start_t = time.perf_counter()
    res_slow = slow_fibonacci(n_val)
    t_slow = time.perf_counter() - start_t
    print(f"⏱️  Uncached `slow_fibonacci({n_val})` : {t_slow:.4f} sec (Res: {res_slow:,})")

    # 2. Cached Fibonacci
    start_t = time.perf_counter()
    res_fast = fast_fibonacci(n_val)
    t_fast = time.perf_counter() - start_t
    print(f"🚀 Cached   `fast_fibonacci({n_val})` : {t_fast:.6f} sec (Res: {res_fast:,})")

    speedup = t_slow / max(t_fast, 0.000001)
    print(f"🔥 Speedup Factor                   : {speedup:,.1f}x Faster!")


# ================================================================================
# PART 2: INSPECTING CACHE STATISTICS & CLEARING CACHE
# ================================================================================

@lru_cache(maxsize=4)
def compute_square(x: int) -> int:
    print(f"  [EXEC] Computing square for {x}...")
    return x * x


def demonstrate_cache_info_and_clear():
    print("\n" + "=" * 80)
    print("PART 2: CACHE INSPECTION (cache_info & cache_clear)")
    print("=" * 80)

    compute_square.cache_clear()  # Start fresh

    print("1. Initial Calls:")
    compute_square(2)  # Miss
    compute_square(3)  # Miss
    compute_square(2)  # Hit! (Cached)
    compute_square(4)  # Miss
    compute_square(3)  # Hit! (Cached)

    info = compute_square.cache_info()
    print(f"\n📊 Cache Info: Hits={info.hits}, Misses={info.misses}, MaxSize={info.maxsize}, CurrSize={info.currsize}")

    print("\n2. Eviction Demo (maxsize=4):")
    compute_square(5)  # Miss (4th item)
    compute_square(6)  # Miss (5th item - Evicts least recently used: 4!)
    
    print("   Calling 4 again (was evicted):")
    compute_square(4)  # Miss again!

    print("\n3. Bypassing Cache using `__wrapped__`:")
    res_unwrapped = compute_square.__wrapped__(10)
    print(f"   Executed directly via __wrapped__: {res_unwrapped}")

    # calling compute_square(10) will not use the cached value
    again_10 = compute_square(10)
    print(f"Cache miss only for 10 because we used __wrapped__: {again_10}")


# ================================================================================
# PART 3: `typed=True` vs `typed=False`
# ================================================================================

@lru_cache(maxsize=16, typed=False)
def untyped_func(val1, val2="a"):
    return f"Processed {val1}, {val2}"


@lru_cache(maxsize=16, typed=True)
def typed_func(val1, val2="a"):
    return f"Processed {val1}, {val2}"


def demonstrate_typed_parameter():
    print("\n" + "=" * 80)
    print("PART 3: `typed=False` vs `typed=True` PARAMETER")
    print("=" * 80)

    untyped_func.cache_clear()
    typed_func.cache_clear()

    # 1. Multi-argument call: shared entry for 3 & 3.0 when typed=False
    untyped_func(3, "a")
    untyped_func(3.0, "a")
    print(f"Untyped Cache (typed=False) [3, 'a'] vs [3.0, 'a'] -> CurrSize: {untyped_func.cache_info().currsize} (Shared entry for 3 & 3.0!)")

    # typed=True: 3 and 3.0 get separate entries because types (int vs float) are included in the key
    typed_func(3, "a")
    typed_func(3.0, "a")
    print(f"Typed   Cache (typed=True)  [3, 'a'] vs [3.0, 'a'] -> CurrSize: {typed_func.cache_info().currsize} (Separate entries for 3 & 3.0)")

    # 2. Gotcha: Single scalar int vs float fast-path quirk in functools._make_key
    # Python optimizes single int/str args by returning raw values, but wraps floats in _HashedSeq.
    # Hence, single-arg untyped_func(3) vs untyped_func(3.0) results in key comparison `3 == _HashedSeq((3.0,))` (False), producing CurrSize=2.
    untyped_single = lru_cache(maxsize=16, typed=False)(lambda x: x)
    untyped_single(3)
    untyped_single(3.0)
    print(f"Single-arg int vs float Quirk (typed=False)        -> CurrSize: {untyped_single.cache_info().currsize} (int unwrapped vs float _HashedSeq)")


# ================================================================================
# PART 4: COMMON PITFALL — UNHASHABLE ARGUMENTS & SOLUTIONS
# ================================================================================

@lru_cache(maxsize=32)
def process_data(items: tuple) -> int:
    return sum(items)


def demonstrate_unhashable_args_fix():
    print("\n" + "=" * 80)
    print("PART 4: UNHASHABLE ARGUMENTS PITFALL & FIX")
    print("=" * 80)

    raw_list = [10, 20, 30]

    try:
        # Trying to pass a list raises TypeError!
        @lru_cache
        def bad_func(data):
            return sum(data)
        bad_func(raw_list)
    except TypeError as exc:
        print("❌ Passing list to lru_cache raised TypeError:", exc)

    # FIX: Convert mutable structures (list/set/dict) to immutable tuples/frozensets/tuples of items
    safe_tuple = tuple(raw_list)
    result = process_data(safe_tuple)
    print(f"✅ Fixed by converting list to tuple: sum({safe_tuple}) = {result}")


# ================================================================================
# PART 5: PROGRAMMATIC / NON-DECORATOR USAGE OF lru_cache
# ================================================================================

def raw_factorial(n: int) -> int:
    """Standard uncached function."""
    if n <= 1:
        return 1
    return n * raw_factorial(n - 1)


class PerInstanceCacheService:
    """
    Demonstrates creating a per-instance cache in __init__ 
    without leaking memory via global class method decorators!
    """
    def __init__(self, service_id: str):
        self.service_id = service_id
        # Bind a per-instance lru_cache programmatically!
        self.fetch_user = lru_cache(maxsize=10)(self._raw_fetch_user)

    def _raw_fetch_user(self, user_id: int) -> str:
        print(f"  [{self.service_id}] DB query for user {user_id}...")
        return f"User_{user_id}_data"


def demonstrate_programmatic_lru_cache():
    print("\n" + "=" * 80)
    print("PART 5: PROGRAMMATIC / NON-DECORATOR USAGE")
    print("=" * 80)

    # 1. Programmatically wrapping an external function (e.g. from standard library or third party)
    import math
    cached_sin = lru_cache(maxsize=100)(math.sin)
    
    print("1. Wrapped math.sin programmatically:")
    print("   cached_sin(1.57) ->", cached_sin(1.57))
    print("   cached_sin(1.57) ->", cached_sin(1.57))  # Hit!
    print("   Cache Info:", cached_sin.cache_info())

    # 2. Programmatically wrapping a custom function
    cached_factorial = lru_cache(maxsize=50)(raw_factorial)
    print("\n2. Wrapped raw_factorial programmatically:")
    print("   cached_factorial(5) ->", cached_factorial(5))

    # 3. Per-Instance Caching (Prevents Class-Level Memory Leaks)
    print("\n3. Per-Instance Cache (Independent Caches Per Object):")
    service1 = PerInstanceCacheService("Service-A")
    service2 = PerInstanceCacheService("Service-B")

    service1.fetch_user(42)
    service1.fetch_user(42)  # Hits service1 cache!
    
    service2.fetch_user(42)  # Misses service2 cache (independent instance cache)!


# ================================================================================
# PART 6: BUILDING AN LRU DICTIONARY (collections.OrderedDict)
# ================================================================================

from collections import OrderedDict


class LRUDictCache:
    """
    An LRU (Least Recently Used) dictionary cache built using `collections.OrderedDict`.
    
    NOTE ON A COMMON PITFALL:
    Attempting to use `@lru_cache` as an eviction callback queue for a dict via:
        self._q = lru_cache(maxsize)(lambda key: self._cache.pop(key, None))
    DOES NOT WORK! `@lru_cache` only calls the decorated function on a CACHE MISS, 
    NOT upon eviction. Eviction in `@lru_cache` silently drops internal keys without 
    triggering callbacks.
    
    The standard Pythonic solution is `OrderedDict` with `move_to_end()` and `popitem(last=False)`.
    """
    def __init__(self, max_paths: int = 3):
        self.max_paths = max_paths
        self._cache = OrderedDict()

    def put(self, key: str, value: str):
        if key in self._cache:
            self._cache.move_to_end(key)  # Refresh position
        self._cache[key] = value
        if len(self._cache) > self.max_paths:
            self._cache.popitem(last=False)  # Evict oldest / least recently used item!

    def get(self, key: str):
        if key in self._cache:
            self._cache.move_to_end(key)  # Mark as Most Recently Used
            return self._cache[key]
        return None


def demonstrate_lru_dict_cache():
    print("\n" + "=" * 80)
    print("PART 6: BUILDING AN LRU DICTIONARY (USING collections.OrderedDict)")
    print("=" * 80)

    cache_system = LRUDictCache(max_paths=3)

    print("1. Inserting 3 paths ('path/A', 'path/B', 'path/C'):")
    cache_system.put("path/A", "Data_A")
    cache_system.put("path/B", "Data_B")
    cache_system.put("path/C", "Data_C")
    print("   Current Cache Keys:", list(cache_system._cache.keys()))

    print("\n2. Accessing 'path/A' to mark it as Most Recently Used:")
    val_a = cache_system.get("path/A")
    print(f"   Fetched 'path/A': {val_a} -> Updated Order:", list(cache_system._cache.keys()))

    print("\n3. Inserting 4th path ('path/D') -> Exceeds max_paths=3:")
    cache_system.put("path/D", "Data_D")
    
    print("   Active Cache Keys:", list(cache_system._cache.keys()))
    print(f"   Value of 'path/D': {cache_system._cache['path/D']}")
    print("   ✅ 'path/B' was correctly evicted because 'path/A' was refreshed!")



# ================================================================================
# MAIN EXECUTION
# ================================================================================

if __name__ == "__main__":
    demonstrate_fibonacci_speedup()
    demonstrate_cache_info_and_clear()
    demonstrate_typed_parameter()
    demonstrate_unhashable_args_fix()
    demonstrate_programmatic_lru_cache()
    demonstrate_lru_dict_cache()



