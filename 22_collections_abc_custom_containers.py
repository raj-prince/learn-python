#!/usr/bin/env python3
"""
================================================================================
LESSON 22: COLLECTIONS.ABC — MUTABLEMAPPING & CUSTOM CONTAINERS
================================================================================

Python's `collections.abc` module provides Abstract Base Classes (ABCs) for 
all built-in container types (dict, list, set, tuple).

This lesson explores:
1. Why subclassing built-in `dict` or `list` is BROKEN in CPython.
2. How `collections.abc.MutableMapping` works (The 5 abstract methods).
3. How `MutableMapping` automatically provides ~12 dictionary methods for free.
4. Other collection ABCs (`MutableSequence`, `MutableSet`, `Mapping`, `Sequence`).
5. `collections.UserDict` vs `collections.abc.MutableMapping`.

--------------------------------------------------------------------------------
PITFALL: WHY SUBCLASSING `dict` DIRECTLY IS BROKEN IN CPYTHON
--------------------------------------------------------------------------------
If you inherit from `dict` directly:
  class LoggingDict(dict):
      def __setitem__(self, key, value):
          print(f"Setting {key}")
          super().__setitem__(key, value)

  d = LoggingDict()
  d.update({"a": 1})  # <--- DOES NOT PRINT "Setting a"!

In CPython, C-level methods like `dict.update()` or `dict()` constructor 
bypass Python-level method overrides like `__setitem__` for speed!

--------------------------------------------------------------------------------
THE SOLUTION: `collections.abc.MutableMapping`
--------------------------------------------------------------------------------
By subclassing `collections.abc.MutableMapping`:
- You MUST implement only 5 core abstract methods:
  1. `__getitem__(self, key)`
  2. `__setitem__(self, key, value)`
  3. `__delitem__(self, key)`
  4. `__iter__(self)`
  5. `__len__(self)`

- `MutableMapping` automatically provides mixin implementations for:
  `get()`, `keys()`, `values()`, `items()`, `pop()`, `popitem()`, 
  `clear()`, `update()`, `setdefault()`, `__eq__`, `__contains__`.

- Calling `.update()` will ALWAYS route through YOUR `__setitem__`!
"""

from collections.abc import MutableMapping, MutableSequence, MutableSet
from collections import UserDict


# ================================================================================
# PART 1: THE BUILT-IN `dict` SUBCLASSING PITFALL vs MutableMapping
# ================================================================================

class BrokenLoggingDict(dict):
    """Direct dict subclass - Overridden __setitem__ is bypassed by C-methods!"""
    def __setitem__(self, key, value):
        print(f"  [BrokenDict] Setting {key} = {value}")
        super().__setitem__(key, value)


class CorrectLoggingDict(MutableMapping):
    """Subclassing MutableMapping - Guarantees all methods route through __setitem__."""
    def __init__(self, *args, **kwargs):
        self._store = {}
        self.update(dict(*args, **kwargs))  # Safe update call

    # The 5 Mandatory Abstract Methods:
    def __getitem__(self, key):
        return self._store[key]

    def __setitem__(self, key, value):
        print(f"  [CorrectDict] Setting {key} = {value}")
        self._store[key] = value

    def __delitem__(self, key):
        del self._store[key]

    def __iter__(self):
        return iter(self._store)

    def __len__(self):
        return len(self._store)


def demonstrate_dict_subclass_pitfall():
    print("\n" + "=" * 80)
    print("PART 1: PITFALL OF SUBCLASSING `dict` vs `collections.abc.MutableMapping`")
    print("=" * 80)

    print("1. Testing BrokenLoggingDict (Subclassing `dict` directly):")
    broken = BrokenLoggingDict()
    broken["key1"] = "val1"             # Calls __setitem__
    broken.update({"key2": "val2"})     # BYPASSES __setitem__ in CPython!
    print(f"   Contents: {broken}\n")

    print("2. Testing CorrectLoggingDict (Subclassing `MutableMapping`):")
    correct = CorrectLoggingDict()
    correct["key1"] = "val1"            # Calls __setitem__
    correct.update({"key2": "val2"})    # PROPERLY calls __setitem__ via mixin!
    print(f"   Contents: {dict(correct)}")


# ================================================================================
# PART 2: BUILDING A REAL-WORLD CASE-INSENSITIVE DICTIONARY
# ================================================================================

class CaseInsensitiveDict(MutableMapping):
    """
    A custom dictionary where string keys are case-insensitive.
    e.g., d['Header'] == d['header'] == d['HEADER']
    """
    def __init__(self, *args, **kwargs):
        self._store = {}  # Maps lowercased_key -> (original_key, value)
        self.update(dict(*args, **kwargs))

    def __getitem__(self, key):
        lower_key = key.lower() if isinstance(key, str) else key
        return self._store[lower_key][1]

    def __setitem__(self, key, value):
        lower_key = key.lower() if isinstance(key, str) else key
        self._store[lower_key] = (key, value)

    def __delitem__(self, key):
        lower_key = key.lower() if isinstance(key, str) else key
        del self._store[lower_key]

    def __iter__(self):
        # Yield original key casing
        return (original_key for original_key, _ in self._store.values())

    def __len__(self):
        return len(self._store)

    def __repr__(self):
        return f"{self.__class__.__name__}({dict(self.items())})"


def demonstrate_case_insensitive_dict():
    print("\n" + "=" * 80)
    print("PART 2: CASE-INSENSITIVE DICTIONARY USING MutableMapping")
    print("=" * 80)

    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    headers["AUTHORIZATION"] = "Bearer token_xyz"

    print("Created Headers:", headers)
    print("  headers['content-type']  ->", headers['content-type'])
    print("  headers['Authorization'] ->", headers['Authorization'])
    print("  'authorization' in headers ->", 'authorization' in headers)
    
    # Testing inherited mixin methods for free!
    print("  headers.get('CONTENT-TYPE') ->", headers.get('CONTENT-TYPE'))
    print("  headers.keys()              ->", list(headers.keys()))


# ================================================================================
# PART 3: OTHER CONTAINER ABCs (MutableSequence, MutableSet)
# ================================================================================

class BoundedList(MutableSequence):
    """A list that enforces a maximum capacity limit."""
    def __init__(self, max_capacity: int, initial=None):
        self.max_capacity = max_capacity
        self._list = list(initial) if initial else []
        if len(self._list) > max_capacity:
            raise ValueError("Initial items exceed max capacity!")

    # The 5 Mandatory Abstract Methods for MutableSequence:
    def __getitem__(self, index):
        return self._list[index]

    def __setitem__(self, index, value):
        self._list[index] = value

    def __delitem__(self, index):
        del self._list[index]

    def __len__(self):
        return len(self._list)

    def insert(self, index, value):
        if len(self._list) >= self.max_capacity:
            raise OverflowError(f"Cannot insert! List reached max capacity of {self.max_capacity}")
        self._list.insert(index, value)

    def __repr__(self):
        return f"BoundedList(capacity={self.max_capacity}, data={self._list})"


def demonstrate_mutable_sequence():
    print("\n" + "=" * 80)
    print("PART 3: CUSTOM LIST VIA MutableSequence")
    print("=" * 80)

    blist = BoundedList(max_capacity=3)
    blist.append("A")  # Inherited mixin method!
    blist.append("B")  # Inherited mixin method!
    blist.append("C")
    print("BoundedList filled:", blist)

    try:
        blist.append("D")  # Should trigger OverflowError
    except OverflowError as exc:
        print("  Caught expected error:", exc)


# ================================================================================
# PART 4: SUMMARY OF COLLECTIONS.ABC HIERARCHY
# ================================================================================

def print_collections_abc_hierarchy():
    print("\n" + "=" * 80)
    print("PART 4: SUMMARY OF COLLECTIONS.ABC HIERARCHY & MIXINS")
    print("=" * 80)
    summary = """
┌──────────────────┬─────────────────────────────────────────┬───────────────────────────────────────────┐
│ Collection ABC   │ Mandatory Abstract Methods              │ Provided Mixin Methods for Free           │
├──────────────────┼─────────────────────────────────────────┼───────────────────────────────────────────┤
│ Mapping          │ __getitem__, __iter__, __len__          │ __contains__, keys, items, values, get    │
│ MutableMapping   │ Mapping + __setitem__, __delitem__      │ pop, popitem, clear, update, setdefault   │
│ Sequence         │ __getitem__, __len__                    │ __contains__, __iter__, __reversed__,     │
│                  │                                         │ index, count                              │
│ MutableSequence  │ Sequence + __setitem__, __delitem__,    │ append, extend, reverse, pop, remove,     │
│                  │ insert                                  │ __iadd__                                  │
│ Set              │ __contains__, __iter__, __len__         │ __le__, __lt__, __eq__, __ne__, __ge__,   │
│                  │                                         │ __gt__, __and__, __or__, __sub__, __xor__ │
│ MutableSet       │ Set + add, discard                      │ pop, clear, __ior__, __iand__, __isub__   │
└──────────────────┴─────────────────────────────────────────┴───────────────────────────────────────────┘

UserDict / UserList vs MutableMapping / MutableSequence:
- `collections.UserDict`: High-level wrapper around an internal `self.data` dict. Use when 
  you just want a dictionary with slight tweaks without manually writing the 5 abstract methods.
- `collections.abc.MutableMapping`: Low-level interface contract. Use when creating custom data 
  structures (e.g. database-backed dict, Redis-backed dict, LRU cache dict, Tree map).
"""
    print(summary)


# ================================================================================
# MAIN EXECUTION
# ================================================================================

if __name__ == "__main__":
    demonstrate_dict_subclass_pitfall()
    demonstrate_case_insensitive_dict()
    demonstrate_mutable_sequence()
    print_collections_abc_hierarchy()
