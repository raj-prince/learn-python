#!/usr/bin/env python3
"""
================================================================================
SOLUTION: LESSON 29 — BUFFER POOLS & MEMORY MANAGEMENT
================================================================================
"""

from collections import deque


class PacketBufferPool:
    """
    A high-performance buffer pool for network packet processing.
    Recycles pre-allocated bytearray slots to minimize memory allocations.
    """

    def __init__(self, slot_count: int, slot_size: int):
        self.slot_size = slot_size
        self._free_slots = deque([bytearray(slot_size) for _ in range(slot_count)])
        self.reused_count = 0

    def get_slot(self) -> bytearray:
        """Fetch an available slot buffer from the pool."""
        if self._free_slots:
            self.reused_count += 1
            return self._free_slots.popleft()
        return bytearray(self.slot_size)

    def recycle_slot(self, buf: bytearray):
        """Return a slot buffer back to the pool."""
        if len(buf) == self.slot_size:
            self._free_slots.append(buf)

    def available_slots(self) -> int:
        """Return the number of available slots in the pool."""
        return len(self._free_slots)


def run_exercise_tests():
    print("\n==================================================")
    print("RUNNING EXERCISE 29 TESTS")
    print("==================================================")
    
    pool = PacketBufferPool(slot_count=4, slot_size=1024)
    assert pool.available_slots() == 4, f"FAILED: Expected 4 slots, got {pool.available_slots()}"
    
    slot1 = pool.get_slot()
    slot2 = pool.get_slot()
    assert len(slot1) == 1024, "FAILED: Slot size is incorrect"
    assert pool.available_slots() == 2, f"FAILED: Expected 2 available slots, got {pool.available_slots()}"
    
    pool.recycle_slot(slot1)
    assert pool.available_slots() == 3, "FAILED: Slot was not recycled"
    
    slot3 = pool.get_slot()
    assert pool.reused_count == 3, f"FAILED: Expected reused_count 3, got {pool.reused_count}"
    print(f"Pool status: Available={pool.available_slots()}, Reused Count={pool.reused_count}")
    print("🎉 Exercise 29 Passed Successfully!")


if __name__ == "__main__":
    run_exercise_tests()
