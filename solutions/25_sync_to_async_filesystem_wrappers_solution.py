#!/usr/bin/env python3
"""
================================================================================
LESSON 25: WRAPPING SYNCHRONOUS FILESYSTEMS FOR ASYNC / ASYNCIO — SOLUTION
================================================================================
"""

import asyncio
import time

class SyncKVStore:
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


class AsyncKVStoreWrapper:
    """Async wrapper around SyncKVStore supporting async with context management."""
    
    def __init__(self, store: SyncKVStore):
        self.store = store

    async def __aenter__(self):
        await asyncio.to_thread(self.store.connect)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await asyncio.to_thread(self.store.disconnect)

    async def get(self, key: str) -> str:
        return await asyncio.to_thread(self.store.get, key)

    async def put(self, key: str, val: str):
        return await asyncio.to_thread(self.store.put, key, val)


async def run_exercise_solution():
    print("\n==================================================")
    print("RUNNING EXERCISE 25 SOLUTION")
    print("==================================================")
    
    sync_store = SyncKVStore()
    async_store = AsyncKVStoreWrapper(sync_store)
    
    async with async_store as store:
        assert sync_store.connected is True, "FAILED: Store was not connected in __aenter__"
        
        # Test concurrent writes
        await asyncio.gather(
            store.put("user_1", "Alice"),
            store.put("user_2", "Bob"),
        )
        
        val1 = await store.get("user_1")
        val2 = await store.get("user_2")
        
        assert val1 == "Alice", f"FAILED: Expected 'Alice', got '{val1}'"
        assert val2 == "Bob", f"FAILED: Expected 'Bob', got '{val2}'"
        print(f"Fetched values: user_1={val1}, user_2={val2}")
        
    assert sync_store.connected is False, "FAILED: Store was not disconnected in __aexit__"
    print("🎉 Solution Verified Successfully!")

if __name__ == "__main__":
    asyncio.run(run_exercise_solution())
