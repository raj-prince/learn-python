#!/usr/bin/env python3
"""
================================================================================
LESSON 8: ASYNCIO — SINGLE-THREADED COOPERATIVE MULTITASKING
================================================================================

In Lesson 7, we learned about Threading and Multiprocessing. There is a third, 
extremely popular way to handle concurrency in Python: `asyncio` (Asynchronous I/O).

Unlike Threading (where the Operating System force-switches between threads at any time),
`asyncio` uses "Cooperative Multitasking." It runs on a SINGLE thread and uses an 
"Event Loop" to manage tasks. Tasks voluntarily yield control back to the event loop 
whenever they are waiting for I/O (like a network request or a database query).

--------------------------------------------------------------------------------
1. WHY ASYNCIO?
--------------------------------------------------------------------------------
- Extremely lightweight: Operating system threads are heavy. Running 1,000 threads 
  can consume a lot of memory and slow down your CPU due to context switching.
- With `asyncio`, you can easily run 10,000+ concurrent tasks on a single thread!
- It is the foundation of modern high-performance Python web frameworks like FastAPI.

--------------------------------------------------------------------------------
2. KEYWORDS: `async` AND `await`
--------------------------------------------------------------------------------
- `async def`: Declares a function to be a **Coroutine**. A coroutine is a special
  function that can pause its execution and resume later.
- `await`: Tells Python to pause the coroutine here and let the event loop run 
  other tasks while waiting for the awaited task to finish. You can only use 
  `await` inside an `async def` function.
"""

import asyncio
import time

# --- A Simple Coroutine ---
# This is a blueprint for an asynchronous task.
async def fetch_data(source, delay):
    print(f"🔍 [Async] Starting fetch from {source}...")
    # asyncio.sleep is the async version of time.sleep. 
    # It yields control back to the event loop instead of freezing the thread!
    await asyncio.sleep(delay)
    print(f"✨ [Async] Received data from {source}!")
    return f"{source} Data"


# --- Running Coroutines Sequentially (The Wrong Way) ---
async def run_sequential():
    start = time.time()
    # If we await them one by one, they run one after another (no concurrency!)
    data1 = await fetch_data("Database", 1.5)
    data2 = await fetch_data("Weather API", 1.0)
    end = time.time()
    print(f"⏱️ Sequential Async took {end - start:.2f} seconds.")


# --- Running Coroutines Concurrently (The Right Way) ---
async def run_concurrent():
    start = time.time()
    
    # asyncio.gather schedules all coroutines to run concurrently on the event loop
    # and waits for all of them to finish.
    results = await asyncio.gather(
        fetch_data("Database", 1.5),
        fetch_data("Weather API", 1.0),
        fetch_data("Payment Gateway", 0.8)
    )
    
    end = time.time()
    print(f"Results: {results}")
    print(f"⏱️ Concurrent Async took {end - start:.2f} seconds (Should be ~1.5s, the max delay!).")


# --- Main Entry Point ---
# Since we cannot call 'await' in the global scope, we use a main async function
# and run it using the asyncio event loop.
async def main():
    print("==================================================")
    print("RUNNING SEQUENTIAL ASYNC DEMO")
    print("==================================================")
    await run_sequential()
    
    print("\n==================================================")
    print("RUNNING CONCURRENT ASYNC DEMO (using asyncio.gather)")
    print("==================================================")
    await run_concurrent()

if __name__ == "__main__":
    # asyncio.run initializes the Event Loop and runs our main coroutine
    asyncio.run(main())


# ================================================================================
# YOUR TURN: EXERCISE 8
# ================================================================================
# Let's practice by building a simulated Smart Home automation script!
#
# Scenario:
# You want to run a "Good Morning" routine that performs several tasks concurrently:
# 1. Turn on the smart lights (takes 0.5 seconds).
# 2. Start the coffee maker (takes 2.0 seconds).
# 3. Fetch the daily news briefing (takes 1.0 second).
#
# INSTRUCTIONS:
# 1. Write an async coroutine `turn_on_lights()`. It should print a message,
#    use `await asyncio.sleep(0.5)` to simulate the delay, print a success message,
#    and return "💡 Lights: ON".
# 2. Write an async coroutine `brew_coffee()`. It should print a message,
#    use `await asyncio.sleep(2.0)` to simulate brewing, print a success message,
#    and return "☕ Coffee: BREWED".
# 3. Write an async coroutine `fetch_news()`. It should print a message,
#    use `await asyncio.sleep(1.0)` to simulate downloading, print a success message,
#    and return "📰 News: DOWNLOADED".
# 4. Write an async coroutine `morning_routine()` that:
#    - Runs all three tasks concurrently using `asyncio.gather()`.
#    - Prints out the gathered results.
#
# Un-comment the test code at the bottom of the file once you've written your solution!
# ================================================================================

# WRITE YOUR Smart Home COROUTINES HERE:




# --- TEST CODE (Un-comment below to test your implementation) ---
# async def run_exercise_test():
#     print("\n==================================================")
#     print("RUNNING EXERCISE 8: SMART HOME MORNING ROUTINE")
#     print("==================================================")
#     start = time.time()
#     await morning_routine()
#     end = time.time()
#     print(f"⏱️ Morning routine completed in {end - start:.2f} seconds! (Target: ~2.0s)")
# 
# if __name__ == "__main__":
#     # We run the exercise test coroutine using the event loop
#     asyncio.run(run_exercise_test())
