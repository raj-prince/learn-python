#!/usr/bin/env python3
"""
================================================================================
LESSON 25: WRAPPING SYNCHRONOUS FILESYSTEMS FOR ASYNC / ASYNCIO
================================================================================

In asynchronous Python (`asyncio`), running synchronous blocking I/O operations 
(like `file.read()`, `os.listdir()`, disk I/O, or synchronous network calls) 
freezes the single-threaded event loop, blocking all other concurrent coroutines!

To expose a synchronous filesystem or service class as an async API, we offload 
blocking synchronous methods to background worker threads using `asyncio.to_thread()`.

--------------------------------------------------------------------------------
KEY PATTERNS COVERED:
--------------------------------------------------------------------------------
1. EXPLICIT ASYNC WRAPPER:
   Explicitly defining `async def` methods that wrap synchronous calls in 
   `await asyncio.to_thread(sync_func, *args)`.

2. DYNAMIC AUTO-WRAPPER (FSSPEC PATTERN):
   Using `__getattr__` and `functools.wraps` to automatically convert any 
   synchronous method of a class into an awaitable async coroutine on the fly!

3. ASYNC CONTEXT MANAGERS FOR FILES:
   Implementing `__aenter__` and `__aexit__` to expose `async with` syntax 
   for file handles.
"""

import asyncio
import functools
import os
import time


# ================================================================================
# MOCK SYNCHRONOUS FILESYSTEM (SIMULATES BLOCKING DISK / NETWORK I/O)
# ================================================================================

class SyncLocalFileSystem:
    """A legacy synchronous filesystem class with blocking methods."""

    def __init__(self, root_dir: str = "."):
        self.root_dir = root_dir

    def read_file(self, filename: str) -> str:
        """Blocking read operation."""
        time.sleep(0.3)  # Simulate blocking disk I/O latency
        filepath = os.path.join(self.root_dir, filename)
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                return f.read()
        return f"[MOCK CONTENT of {filename}]"

    def write_file(self, filename: str, content: str) -> int:
        """Blocking write operation."""
        time.sleep(0.3)  # Simulate blocking disk I/O latency
        filepath = os.path.join(self.root_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            return f.write(content)

    def list_files(self) -> list[str]:
        """Blocking list operation."""
        time.sleep(0.1)
        return os.listdir(self.root_dir)


# ================================================================================
# PART 1: EXPLICIT ASYNC WRAPPER CLASS
# ================================================================================

class ExplicitAsyncFileSystem:
    """Wraps SyncLocalFileSystem and exposes explicit async def methods."""

    def __init__(self, sync_fs: SyncLocalFileSystem):
        self._sync_fs = sync_fs

    async def read_file(self, filename: str) -> str:
        # asyncio.to_thread offloads self._sync_fs.read_file to a ThreadPoolExecutor!
        return await asyncio.to_thread(self._sync_fs.read_file, filename)

    async def write_file(self, filename: str, content: str) -> int:
        return await asyncio.to_thread(self._sync_fs.write_file, filename, content)

    async def list_files(self) -> list[str]:
        return await asyncio.to_thread(self._sync_fs.list_files)


# ================================================================================
# PART 2: DYNAMIC AUTO-WRAPPER VIA REFLECTION (__getattr__)
# ================================================================================

class DynamicAsyncWrapper:
    """
    Automatically converts ANY synchronous method of the underlying class 
    into an awaitable async coroutine dynamically using __getattr__.
    (This is the pattern used by fsspec's AsyncFileSystemWrapper!)
    """

    def __init__(self, sync_instance):
        self._sync_instance = sync_instance

    def __getattr__(self, name: str):
        attr = getattr(self._sync_instance, name)

        # If the attribute is a callable method, return an async wrapper function
        if callable(attr):
            @functools.wraps(attr)
            async def async_method(*args, **kwargs):
                return await asyncio.to_thread(attr, *args, **kwargs)
            return async_method

        # If it's a standard property or variable, return it directly
        return attr


# ================================================================================
# PART 3: ASYNC FILE CONTEXT MANAGER (async with)
# ================================================================================

class AsyncFileHandle:
    """Exposes `async with` context management for open file handles."""

    def __init__(self, filepath: str, mode: str = "r"):
        self.filepath = filepath
        self.mode = mode
        self._file = None

    async def __aenter__(self):
        # Open file in background thread
        self._file = await asyncio.to_thread(open, self.filepath, self.mode, encoding="utf-8")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # Close file in background thread
        if self._file:
            await asyncio.to_thread(self._file.close)

    async def read(self) -> str:
        return await asyncio.to_thread(self._file.read)

    async def write(self, data: str) -> int:
        return await asyncio.to_thread(self._file.write, data)


# ================================================================================
# DEMONSTRATION & BENCHMARKING CONCURRENCY
# ================================================================================

async def demonstrate_concurrency():
    print("\n" + "=" * 80)
    print("DEMONSTRATING ASYNC CONCURRENCY WITH WRAPPED SYNC FILESYSTEM")
    print("=" * 80)

    sync_fs = SyncLocalFileSystem()
    async_fs = DynamicAsyncWrapper(sync_fs)

    # Prepare 3 test files concurrently
    start_time = time.perf_counter()

    print("🚀 Launching 3 async file writes concurrently using asyncio.gather()...")
    results = await asyncio.gather(
        async_fs.write_file("file1.txt", "Data 1"),
        async_fs.write_file("file2.txt", "Data 2"),
        async_fs.write_file("file3.txt", "Data 3"),
    )

    elapsed = time.perf_counter() - start_time
    print(f"⏱️  Completed 3 writes in {elapsed:.3f} seconds!")
    print(f"    (Notice: Total time is ~0.3s instead of 0.9s because threads ran concurrently!)")

    # Read content back using AsyncFileHandle
    async with AsyncFileHandle("file1.txt", "r") as f:
        content = await f.read()
        print(f"\n📖 Read via AsyncFileHandle: '{content}'")


# ================================================================================
# YOUR TURN: EXERCISE 25
# ================================================================================
# Scenario:
# You have a legacy synchronous Key-Value store class `SyncKVStore`. You need 
# to build an async wrapper `AsyncKVStoreWrapper` that exposes async methods 
# and supports `async with` context management.
#
# INSTRUCTIONS:
# 1. Create a class `AsyncKVStoreWrapper`.
# 2. In `__init__(self, store)`:
#    - Accept an instance of `SyncKVStore`.
# 3. Implement async method `async def get(self, key: str) -> str`:
#    - Offload `self.store.get(key)` using `asyncio.to_thread`.
# 4. Implement async method `async def put(self, key: str, val: str)`:
#    - Offload `self.store.put(key, val)` using `asyncio.to_thread`.
# 5. Implement `async def __aenter__(self)` and `async def __aexit__(self, exc_type, exc_val, exc_tb)`:
#    - `__aenter__` should offload `self.store.connect()` and return `self`.
#    - `__aexit__` should offload `self.store.disconnect()`.
#
# Un-comment the test code at the bottom of the file once you've written your solution!
# ================================================================================

class SyncKVStore:
    """Provided synchronous Key-Value store."""
    def __init__(self):
        self._data = {}
        self.connected = False

    def connect(self):
        time.sleep(0.1)
        self.connected = True

    def disconnect(self):
        time.sleep(0.1)
        self.connected = False

    def put(self, key: str, val: str):
        if not self.connected:
            raise RuntimeError("Store is not connected!")
        time.sleep(0.1)
        self._data[key] = val

    def get(self, key: str) -> str:
        if not self.connected:
            raise RuntimeError("Store is not connected!")
        time.sleep(0.1)
        return self._data.get(key, "")


# WRITE YOUR AsyncKVStoreWrapper CLASS HERE:




# --- EXERCISE 25 TEST CODE (Un-comment below to test your implementation) ---
# async def run_exercise_tests():
#     print("\n==================================================")
#     print("RUNNING EXERCISE 25 TESTS")
#     print("==================================================")
#     
#     sync_store = SyncKVStore()
#     async_store = AsyncKVStoreWrapper(sync_store)
#     
#     async with async_store as store:
#         assert sync_store.connected is True, "FAILED: Store was not connected in __aenter__"
#         
#         # Test concurrent writes
#         await asyncio.gather(
#             store.put("user_1", "Alice"),
#             store.put("user_2", "Bob"),
#         )
#         
#         val1 = await store.get("user_1")
#         val2 = await store.get("user_2")
#         
#         assert val1 == "Alice", f"FAILED: Expected 'Alice', got '{val1}'"
#         assert val2 == "Bob", f"FAILED: Expected 'Bob', got '{val2}'"
#         print(f"Fetched values: user_1={val1}, user_2={val2}")
#         
#     assert sync_store.connected is False, "FAILED: Store was not disconnected in __aexit__"
#     print("🎉 Exercise 25 Passed Successfully!")

if __name__ == "__main__":
    asyncio.run(demonstrate_concurrency())
    # asyncio.run(run_exercise_tests())

