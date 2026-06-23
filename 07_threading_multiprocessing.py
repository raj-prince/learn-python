#!/usr/bin/env python3
"""
================================================================================
LESSON 7: CONCURRENCY — THREADING AND MULTIPROCESSING
================================================================================

When writing programs, we often want to run multiple tasks at the same time.
But did you know that "running at the same time" can mean two completely 
different things in Python? 

Let's demystify Concurrency vs. Parallelism and learn how to use Threading 
and Multiprocessing!

--------------------------------------------------------------------------------
1. THE CORE CONCEPTS
--------------------------------------------------------------------------------
- CONCURRENCY (Multitasking): Dealing with many things at once. 
  It's like a single chef chopping onions, then turning around to stir the soup.
  The chef switches tasks so quickly that it feels like they are doing both at once.
  
- PARALLELISM (True Multi-core): Doing many things at once.
  It's like having two chefs in the kitchen: one chopping onions while the other
  stirs the soup at the exact same moment.

--------------------------------------------------------------------------------
2. THE GIL (GLOBAL INTERPRETER LOCK)
--------------------------------------------------------------------------------
Python has a mechanism called the GIL. It ensures that only ONE thread can execute
Python code at any given second. 

Because of the GIL:
- THREADING is great for I/O-BOUND tasks (waiting for network, web APIs, disk read/write).
  While one thread is waiting for the web API to respond, Python releases the lock and
  lets another thread run.
- MULTIPROCESSING is required for CPU-BOUND tasks (heavy calculations, image processing).
  It bypasses the GIL completely by spawning entirely separate Python processes (each
  with its own CPU core and memory!).

--------------------------------------------------------------------------------
3. MODERN CONCURRENCY: THE `concurrent.futures` MODULE
--------------------------------------------------------------------------------
Instead of managing raw threads and processes manually, Python provides a clean,
high-level API: `concurrent.futures`. We use:
- `ThreadPoolExecutor` for Threading (I/O-bound).
- `ProcessPoolExecutor` for Multiprocessing (CPU-bound).
"""

import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# ================================================================================
# PART 1: THREADING FOR I/O-BOUND TASKS (E.g., Simulating Web Downloads)
# ================================================================================
def download_file(file_id):
    print(f"📡 [Thread] Starting download for file #{file_id}...")
    # Simulate a network delay of 1.5 seconds
    time.sleep(1.5)
    print(f"✅ [Thread] Finished downloading file #{file_id}!")
    return f"File #{file_id} Data"

def run_io_sequential():
    start = time.time()
    results = []
    for i in range(1, 5):
        results.append(download_file(i))
    end = time.time()
    print(f"⏱️ Sequential I/O took {end - start:.2f} seconds.")

def run_io_threaded():
    start = time.time()
    # ThreadPoolExecutor manages a pool of threads for us
    with ThreadPoolExecutor(max_workers=4) as executor:
        # executor.map automatically runs download_file in parallel across our thread pool
        file_ids = [1, 2, 3, 4]
        results = list(executor.map(download_file, file_ids))
    end = time.time()
    print(f"⏱️ Threaded I/O took {end - start:.2f} seconds (Should be ~1.5s instead of ~6s!).")


# ================================================================================
# PART 2: MULTIPROCESSING FOR CPU-BOUND TASKS (E.g., Heavy Math Calculations)
# ================================================================================
def cpu_heavy_calculation(n):
    print(f"🧠 [Process] Calculating sum of squares up to {n}...")
    # Perform a heavy math loop to stress the CPU
    total = sum(i * i for i in range(n))
    print(f"✅ [Process] Calculation for {n} finished!")
    return total

def run_cpu_sequential():
    start = time.time()
    numbers = [8_000_000, 8_000_000, 8_000_000, 8_000_000]
    results = []
    for num in numbers:
        results.append(cpu_heavy_calculation(num))
    end = time.time()
    print(f"⏱️ Sequential CPU tasks took {end - start:.2f} seconds.")

def run_cpu_multiprocessed():
    start = time.time()
    # ProcessPoolExecutor bypasses the GIL by using separate CPU cores
    with ProcessPoolExecutor(max_workers=4) as executor:
        numbers = [8_000_000, 8_000_000, 8_000_000, 8_000_000]
        results = list(executor.map(cpu_heavy_calculation, numbers))
    end = time.time()
    print(f"⏱️ Multiprocessed CPU tasks took {end - start:.2f} seconds.")


# --- DRIVER CODE ---
if __name__ == "__main__":
    print("==================================================")
    print("RUNNING I/O-BOUND TESTS (Threading vs. Sequential)")
    print("==================================================")
    run_io_sequential()
    print("-" * 50)
    run_io_threaded()
    
    print("\n==================================================")
    print("RUNNING CPU-BOUND TESTS (Multiprocessing vs. Sequential)")
    print("==================================================")
    # Note: On some systems, multiprocessing can take a moment to initialize processes.
    run_cpu_sequential()
    print("-" * 50)
    run_cpu_multiprocessed()


# ================================================================================
# YOUR TURN: EXERCISE 7
# ================================================================================
# Let's write a concurrent program to optimize a batch processing pipeline!
#
# Scenario:
# You have a list of image file IDs. Processing each image involves two stages:
# 1. DOWNLOADING the image (I/O-bound: takes 1 second).
# 2. APPLYING A FILTER (CPU-bound: takes some computational effort).
#
# INSTRUCTIONS:
# 1. Complete the `download_image(image_id)` function to simulate download (sleep 1 second).
# 2. Complete the `apply_filter(image_id)` function to simulate image processing.
#    To simulate a heavy calculation, calculate the sum of numbers from 1 to 10,000,000.
# 3. Write a function `process_images_concurrently()` that:
#    - Downloads 4 images concurrently using `ThreadPoolExecutor`.
#    - Once all 4 are downloaded, applies filters to all 4 concurrently using `ProcessPoolExecutor`.
#
# Un-comment the test code at the bottom of the file once you've written your solution!
# ================================================================================

# --- WRITE YOUR EXERCISE FUNCTIONS HERE ---

def download_image(image_id):
    pass # TODO: Print start, sleep 1.0 second, print finish, return image_id

def apply_filter(image_id):
    pass # TODO: Print start, calculate sum(i for i in range(10_000_000)), print finish, return image_id

def process_images_concurrently():
    # TODO:
    # 1. Download images 1, 2, 3, 4 concurrently using ThreadPoolExecutor.
    # 2. Apply filters to the downloaded images concurrently using ProcessPoolExecutor.
    pass



# --- TEST CODE (Un-comment below to test your implementation) ---
# if __name__ == "__main__":
#     print("\n==================================================")
#     print("RUNNING EXERCISE 7: BATCH IMAGE PIPELINE")
#     print("==================================================")
#     pipeline_start = time.time()
#     process_images_concurrently()
#     pipeline_end = time.time()
#     print(f"⏱️ Entire pipeline took {pipeline_end - pipeline_start:.2f} seconds!")
