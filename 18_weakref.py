#!/usr/bin/env python3
"""
================================================================================
LESSON 18: WEAKREF — WEAK REFERENCES AND MEMORY MANAGEMENT IN PYTHON
================================================================================

In Python, memory management relies on Reference Counting.
When you assign an object to a variable or insert it into a standard dictionary/list,
Python creates a STRONG REFERENCE. This increments the object's reference counter,
preventing the Garbage Collector from freeing its memory.

`weakref` allows you to create WEAK REFERENCES to objects. A weak reference does NOT 
increment the reference counter. If all strong references to an object are removed, 
the object is garbage collected immediately, even if weak references still point to it!

--------------------------------------------------------------------------------
COMMON USE CASES FOR WEAKREF
--------------------------------------------------------------------------------
1. Caches / Flyweight pools: Cache large objects in memory without preventing GC.
2. Parent-Child / Circular References: Prevent memory leaks in tree structures.
3. Event Observers: Keep track of subscribers without keeping them alive artificially.
"""

import weakref
import gc

class LargeDataObject:
    """A heavy object representing data loaded into memory."""
    def __init__(self, name: str):
        self.name = name
        self.data = [i for i in range(100_000)]  # Consume some RAM
        print(f"🏗️  [Created] {self.name}")

    def __del__(self):
        """Called by Python when the object is garbage collected."""
        print(f"🗑️  [Destroyed/GC] {self.name}")


# ================================================================================
# 1. STRONG REF VS WEAK REF (weakref.ref)
# ================================================================================

def demonstrate_weak_reference():
    print("==================================================")
    print("1. STRONG REF VS WEAK REF (weakref.ref)")
    print("==================================================")
    
    # 1. Create a strong reference
    obj = LargeDataObject("Dataset-Alpha")

    # 2. Create a weak reference pointing to `obj`
    r = weakref.ref(obj)

    print(f"🔍 Accessing via weakref `r()`: {r()}")
    print(f"Is object still alive? {r() is not None}")

    print("\n--- Deleting the strong reference `del obj` ---")
    del obj  # Removing the ONLY strong reference

    # Accessing the weak reference after strong reference is deleted
    print(f"🔍 Accessing via weakref `r()` after `del obj`: {r()}")
    print(f"Is object still alive? {r() is not None}")


# ================================================================================
# 2. WEAK VALUE DICTIONARY (AUTOMATIC CACHE CLEANUP)
# ================================================================================

def demonstrate_weak_value_dictionary():
    print("\n==================================================")
    print("2. WEAK VALUE DICTIONARY (WEAKREF.WEAKVALUEDICTIONARY)")
    print("==================================================")
    
    # Standard dict keeps objects alive forever (memory leak if forgotten)
    # WeakValueDictionary automatically removes keys when values are garbage collected!
    cache = weakref.WeakValueDictionary()

    # Create objects and store them in cache
    obj1 = LargeDataObject("Image-1")
    obj2 = LargeDataObject("Image-2")

    cache["img1"] = obj1
    cache["img2"] = obj2

    print(f"Cache keys before deletion: {list(cache.keys())}")

    # Delete the strong reference to Image-1
    print("\nDeleting strong reference `del obj1`...")
    del obj1

    # Notice Image-1 automatically vanished from the cache!
    print(f"Cache keys after `del obj1`: {list(cache.keys())}")


# ================================================================================
# 3. WEAKREF FINALIZE (CLEANUP CALLBACKS)
# ================================================================================

def cleanup_callback(name):
    print(f"🧹 [Finalizer Callback] Cleaned up external resources for {name}")


def demonstrate_finalizer():
    print("\n==================================================")
    print("3. WEAKREF FINALIZE (AUTOMATIC RESOURCE CLEANUP)")
    print("==================================================")
    
    obj = LargeDataObject("DatabaseConnection")
    
    # Register a callback to run when `obj` is garbage collected
    finalizer = weakref.finalize(obj, cleanup_callback, "DatabaseConnection")

    print(f"Is finalizer alive? {finalizer.alive}")

    print("Deleting `obj`...")
    del obj

    print(f"Is finalizer alive after GC? {finalizer.alive}")


# ================================================================================
# MAIN ENTRY POINT
# ================================================================================

if __name__ == "__main__":
    demonstrate_weak_reference()
    demonstrate_weak_value_dictionary()
    demonstrate_finalizer()
