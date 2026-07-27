#!/usr/bin/env python3
"""
================================================================================
LESSON 17: ASYNCIO QUEUE AND EVENT — ASYNCHRONOUS SYNCHRONIZATION
================================================================================

When building asynchronous applications, coroutines often need to communicate, 
share work, or synchronize execution without blocking the event loop.

Python's `asyncio` module provides synchronization primitives tailored for coroutines:

1. `asyncio.Queue`:
   - A First-In, First-Out (FIFO) queue for Producer-Consumer patterns.
   - Non-blocking: `await queue.put()` and `await queue.get()` yield control to 
     the event loop when full or empty.
   - `queue.task_done()` & `await queue.join()` coordinate batch completion.

2. `asyncio.Event`:
   - A single-flag synchronization primitive used to notify multiple coroutines 
     that a specific event has occurred (like a "start signal" or "stop signal").
   - `await event.wait()`: Coroutine pauses until event flag becomes True.
   - `event.set()`: Sets flag to True and wakes up all waiting coroutines.
   - `event.clear()`: Resets flag to False.
"""

import asyncio
import random
import time

import aiohttp

# ================================================================================
# PART 1: ASYNCIO.QUEUE (NETWORK PRODUCER & BUFFER CONSUMER PIPELINE)
# ================================================================================

async def network_producer(queue: asyncio.Queue, session: aiohttp.ClientSession, endpoints: list):
    """Network Producer: Fetches raw JSON data from external web APIs and pushes to buffer queue."""
    for item_id in endpoints:
        url = f"https://jsonplaceholder.typicode.com/posts/{item_id}"
        print(f"🌐 [Network Producer] Fetching HTTP data for post #{item_id}...")
        
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                # Push fetched network payload into the buffer queue
                await queue.put(data)
                print(f"📥 [Network Producer] Pushed post #{item_id} into Buffer Queue (Queue Size: {queue.qsize()})")
            else:
                print(f"❌ [Network Producer] Failed to fetch post #{item_id}")

    print("✅ [Network Producer] Finished fetching all network endpoints.")


async def buffer_consumer(queue: asyncio.Queue, consumer_id: int):
    """Buffer Consumer: Reads payloads from the queue buffer and processes them asynchronously."""
    while True:
        # Read payload from the buffer queue (pauses if buffer is empty)
        data = await queue.get()
        post_id = data.get("id")
        title = data.get("title", "")[:35]
        
        print(f"⚙️  [Buffer Consumer {consumer_id}] Dequeued post #{post_id} from buffer. Processing: '{title}...'")
        
        # Simulate processing/saving data (e.g. database write, text analysis)
        await asyncio.sleep(0.4)
        print(f"✨ [Buffer Consumer {consumer_id}] Successfully processed & stored post #{post_id}")
        
        # Notify the queue buffer that processing for this item is complete
        queue.task_done()


async def run_queue_demo():
    print("==================================================")
    print("DEMO 1: ASYNCIO.QUEUE (NETWORK FETCH PRODUCER & BUFFER CONSUMER)")
    print("==================================================")
    
    # Create an in-memory buffer queue with max capacity of 4 items
    buffer_queue = asyncio.Queue(maxsize=4)
    endpoints = list(range(1, 9))  # 8 network items to fetch

    # Spawn 2 background buffer consumer tasks
    consumers = [
        asyncio.create_task(buffer_consumer(buffer_queue, consumer_id=i))
        for i in (1, 2)
    ]

    # Create an aiohttp ClientSession for the Network Producer
    async with aiohttp.ClientSession() as session:
        # Run network producer to fetch API data and push into buffer
        await network_producer(buffer_queue, session, endpoints)

    # Block until all items in the queue buffer have been read and processed by consumers
    await buffer_queue.join()
    print("🎉 All network data in the buffer queue has been processed!")

    # Cancel background consumer tasks gracefully
    for c in consumers:
        c.cancel()


# ================================================================================
# PART 2: ASYNCIO.EVENT (NOTIFICATION / BROADCAST SIGNALING)
# ================================================================================

async def worker_waiting_for_signal(worker_id: int, start_event: asyncio.Event):
    """Worker task that waits for a global start event before executing."""
    print(f"⏳ [Worker {worker_id}] Ready and waiting for start signal...")
    
    # Pause here until start_event.set() is called
    await start_event.wait()
    
    print(f"🚀 [Worker {worker_id}] Received signal! Executing task...")
    await asyncio.sleep(0.5)
    print(f"✅ [Worker {worker_id}] Task completed!")


async def run_event_demo():
    print("\n==================================================")
    print("DEMO 2: ASYNCIO.EVENT (BROADCAST START SIGNAL)")
    print("==================================================")
    
    # Create an Event object (initial state: False / cleared)
    start_event = asyncio.Event()

    # Create 4 worker coroutines waiting on the event
    tasks = [
        asyncio.create_task(worker_waiting_for_signal(i, start_event))
        for i in range(1, 5)
    ]

    print("📢 System preparing initial setup (2 seconds)...")
    await asyncio.sleep(2.0)

    print("🔥 Firing START SIGNAL (start_event.set())...")
    # Setting the event flag wakes up ALL waiting coroutines simultaneously!
    start_event.set()

    # Wait for all workers to finish
    await asyncio.gather(*tasks)


# ================================================================================
# MAIN ENTRY POINT
# ================================================================================

async def main():
    await run_queue_demo()
    await run_event_demo()

if __name__ == "__main__":
    asyncio.run(main())
