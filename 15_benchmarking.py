#!/usr/bin/env python3
"""
================================================================================
LESSON 15: BENCHMARKING & PROFILING IN PYTHON — CPU TIME & MEMORY ALLOCATION
================================================================================

When optimizing Python code, you must measure before you optimize.
Python provides powerful built-in tools for benchmarking:

1. CPU Execution Time:
   - `time.perf_counter()`: High-precision clock for timing code blocks.
   - `timeit`: Standard library module designed to run code thousands of times 
     to eliminate operating system background noise.
   - `cProfile`: Profiler that breaks down execution time spent inside every function call.

2. Memory Allocation:
   - `tracemalloc`: Built-in memory tracking module that measures current memory,
     peak memory allocation, and pinpoints exact lines allocating memory.
"""

import time
import timeit
import tracemalloc
import cProfile
import pstats

# ================================================================================
# THE TWO METHODS WE WANT TO BENCHMARK & COMPARE
# ================================================================================
# Method A: Building a list using a standard for-loop with .append()
def method_a_for_loop(n=1_000_000):
    result = []
    for i in range(n):
        if i % 2 == 0:
            result.append(i * 2)
    return result

# Method B: Building a list using List Comprehension (Optimized in C bytecode)
def method_b_list_comprehension(n=1_000_000):
    return [i * 2 for i in range(n) if i % 2 == 0]

# Method C: Generator Expression (Memory-efficient streaming)
def method_c_generator(n=1_000_000):
    return (i * 2 for i in range(n) if i % 2 == 0)


# ================================================================================
# 1. CPU EXECUTION TIME BENCHMARKING (timeit & time.perf_counter)
# ================================================================================

def benchmark_cpu_time():
    print("==================================================")
    print("1. CPU EXECUTION TIME BENCHMARKING")
    print("==================================================")
    
    n = 2_000_000

    # A) Simple perf_counter measurement
    start = time.perf_counter()
    res_a = method_a_for_loop(n)
    time_a = time.perf_counter() - start

    start = time.perf_counter()
    res_b = method_b_list_comprehension(n)
    time_b = time.perf_counter() - start

    print(f"⏱️ Method A (For Loop)       : {time_a:.4f} seconds")
    print(f"⏱️ Method B (List Comp)       : {time_b:.4f} seconds")
    print(f"⚡ Speedup                    : Method B is {time_a / time_b:.2f}x faster!")

    # B) Precise benchmarking using `timeit` module
    print("\n--- Running timeit (10 iterations) ---")
    t_a = timeit.timeit(lambda: method_a_for_loop(100_000), number=10)
    t_b = timeit.timeit(lambda: method_b_list_comprehension(100_000), number=10)
    print(f"⏱️ timeit Method A: {t_a:.4f}s")
    print(f"⏱️ timeit Method B: {t_b:.4f}s")


# ================================================================================
# 2. MEMORY ALLOCATION BENCHMARKING (tracemalloc)
# ================================================================================

def benchmark_memory_allocation():
    print("\n==================================================")
    print("2. MEMORY ALLOCATION BENCHMARKING (tracemalloc)")
    print("==================================================")
    
    n = 2_000_000

    # --- Benchmark Method A Memory ---
    tracemalloc.start()
    data_a = method_a_for_loop(n)
    current_a, peak_a = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # --- Benchmark Method B Memory ---
    tracemalloc.start()
    data_b = method_b_list_comprehension(n)
    current_b, peak_b = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # --- Benchmark Method C (Generator) Memory ---
    tracemalloc.start()
    data_c = method_c_generator(n)
    current_c, peak_c = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Convert bytes to Megabytes (MB)
    print(f"💾 Method A (For Loop List)  -> Peak Memory: {peak_a / (1024 * 1024):.2f} MB")
    print(f"💾 Method B (List Comp)      -> Peak Memory: {peak_b / (1024 * 1024):.2f} MB")
    print(f"💾 Method C (Generator)      -> Peak Memory: {peak_c / (1024 * 1024):.4f} MB (Streamed memory!)")


# ================================================================================
# 3. DETAILED CALL PROFILING (cProfile)
# ================================================================================

def profile_functions():
    print("\n==================================================")
    print("3. DETAILED FUNCTION CALL PROFILING (cProfile)")
    print("==================================================")
    
    profiler = cProfile.Profile()
    profiler.enable()
    
    # Run functions inside profiler
    method_a_for_loop(1_000_000)
    method_b_list_comprehension(1_000_000)
    
    profiler.disable()
    
    # Print sorted stats
    stats = pstats.Stats(profiler).sort_stats('cumtime')
    stats.print_stats(10)


# ================================================================================
# MAIN ENTRY POINT
# ================================================================================

if __name__ == "__main__":
    benchmark_cpu_time()
    benchmark_memory_allocation()
    profile_functions()
