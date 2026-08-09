#!/usr/bin/env python3
"""
================================================================================
LESSON 31: MONKEY PATCHING & RUNTIME DYNAMIC BEHAVIOR MODIFICATION
================================================================================

**Monkey Patching** in Python refers to dynamically modifying or extending a module,
class, or function at **runtime** without altering the underlying source code file.

Because Python is a dynamic language where modules, classes, and functions are mutable
first-class objects, you can re-bind attributes and methods at execution time.

--------------------------------------------------------------------------------
COMMON USE CASES
--------------------------------------------------------------------------------
1. Unit Testing & Mocking:
   - Overriding blocking network calls (e.g. `requests.get`) or system calls (`time.sleep`)
     during test runs using `unittest.mock.patch`.

2. Hotfixing Third-Party Library Bugs:
   - Overriding a buggy method in an installed `pip` package at application startup
     without editing files in `site-packages`.

3. Async Event Loop Injection (`gevent` / `eventlet`):
   - Replacing standard blocking calls (`socket`, `select`, `time.sleep`) with non-blocking
     greenlet equivalents via `gevent.monkey.patch_all()`.

--------------------------------------------------------------------------------
RISKS & BEST PRACTICES
--------------------------------------------------------------------------------
- Risk: Hard to debug ("spooky action at a distance").
- Risk: Fragile across third-party library version upgrades.
- Risk: Global side effects affecting all threads and modules.
- Best Practice: Use context managers (`unittest.mock.patch` or custom context managers)
  so patches are automatically reverted when leaving the scope!
"""

import time
import types
from unittest.mock import patch


# ================================================================================
# PART 1: BASIC FUNCTION & MODULE MONKEY PATCHING
# ================================================================================

def original_fetch_data(endpoint: str) -> dict:
    """Simulates a blocking network call."""
    time.sleep(0.5)
    return {"status": 200, "data": f"Real response from {endpoint}"}


def demonstrate_basic_monkey_patching():
    global original_fetch_data

    print("\n" + "=" * 80)
    print("PART 1: BASIC FUNCTION & MODULE MONKEY PATCHING")
    print("=" * 80)

    print("1. Calling original function:")
    print("  ", original_fetch_data("https://api.example.com/users"))

    # Save reference to original function
    real_func = original_fetch_data

    # Define replacement function
    def mock_fetch_data(endpoint: str) -> dict:
        print(f"  🐒 [MonkeyPatch] Intercepted call to '{endpoint}'!")
        return {"status": 200, "data": f"MOCKED payload for {endpoint}"}

    # Apply Monkey Patch by re-assigning global reference
    original_fetch_data = mock_fetch_data


    print("\n2. Calling function after Monkey Patching:")
    print("  ", original_fetch_data("https://api.example.com/users"))

    # Restore original function
    original_fetch_data = real_func
    print("\n3. Restored original function:")
    print("  ", original_fetch_data("https://api.example.com/users"))


# ================================================================================
# PART 2: SAFE TEMPORARY PATCHING USING CONTEXT MANAGERS (unittest.mock.patch)
# ================================================================================

class ExternalServiceAPI:
    def send_payment(self, amount: float) -> str:
        """Simulates external payment gateway call."""
        return f"PAID ${amount:.2f} via Real Gateway"


def demonstrate_safe_context_patching():
    print("\n" + "=" * 80)
    print("PART 2: SAFE TEMPORARY PATCHING VIA CONTEXT MANAGERS")
    print("=" * 80)

    api = ExternalServiceAPI()

    print("1. Before patch:")
    print("  ", api.send_payment(100.0))

    # Using unittest.mock.patch as a context manager ensures automatic cleanup!
    with patch.object(ExternalServiceAPI, "send_payment", return_value="PAID $100.00 via MOCK Gateway"):
        print("\n2. Inside `with patch.object(...)` context:")
        print("  ", api.send_payment(100.0))

    print("\n3. Outside context (Automatically reverted!):")
    print("  ", api.send_payment(100.0))


# ================================================================================
# PART 3: HOTFIXING CLASS METHODS AT RUNTIME
# ================================================================================

class LegacyDataProcessor:
    def process_records(self, records: list[str]) -> list[str]:
        # BUG: Crashes with TypeError if records contains None!
        return [r.upper() for r in records]


def demonstrate_class_hotfixing():
    print("\n" + "=" * 80)
    print("PART 3: HOTFIXING CLASS METHODS AT RUNTIME")
    print("=" * 80)

    processor = LegacyDataProcessor()
    bad_data = ["alice", None, "bob"]

    try:
        processor.process_records(bad_data)
    except AttributeError as exc:
        print("❌ Original method crashed on None:", repr(exc))

    # Hotfix patch: Define a defensive implementation
    def fixed_process_records(self, records: list[str]) -> list[str]:
        cleaned = [r for r in records if r is not None]
        return [r.upper() for r in cleaned]

    # Monkey patch the method on the class
    LegacyDataProcessor.process_records = fixed_process_records

    # Now calling process_records on any instance uses the fixed implementation!
    result = processor.process_records(bad_data)
    print("✅ Hotfixed method output:", result)


# ================================================================================
# YOUR TURN: EXERCISE 31
# ================================================================================
# Scenario:
# You are writing a custom context manager `TemporaryPatch` to safely monkey patch
# an attribute on an object/module and automatically restore the original value upon exit.
#
# INSTRUCTIONS:
# 1. Create a class `TemporaryPatch`.
# 2. In `__init__(self, target_obj, attr_name: str, new_value)`:
#    - Store `target_obj`, `attr_name`, and `new_value`.
#    - Save the original attribute value retrieved via `getattr(target_obj, attr_name)`.
# 3. Implement `__enter__(self)`:
#    - Apply the patch using `setattr(target_obj, self.attr_name, self.new_value)`.
#    - Return `self.new_value`.
# 4. Implement `__exit__(self, exc_type, exc_val, exc_tb)`:
#    - Restore the original value using `setattr(target_obj, self.attr_name, self.original_value)`.
#
# Un-comment the test code at the bottom of the file once you've written your solution!
# ================================================================================

# WRITE YOUR TemporaryPatch CLASS HERE:




# --- EXERCISE 31 TEST CODE (Un-comment below to test your implementation) ---
# def run_exercise_tests():
#     print("\n==================================================")
#     print("RUNNING EXERCISE 31 TESTS")
#     print("==================================================")
#     
#     class DatabaseConfig:
#         host = "production-db.internal"
#         
#     config = DatabaseConfig()
#     assert config.host == "production-db.internal", "FAILED: Original host incorrect"
#     
#     with TemporaryPatch(config, "host", "localhost-test-db"):
#         assert config.host == "localhost-test-db", "FAILED: Patch was not applied inside context!"
#         print("Inside patch context: host =", config.host)
#         
#     assert config.host == "production-db.internal", "FAILED: Patch was not reverted after exit!"
#     print("Outside patch context: host =", config.host)
#     print("🎉 Exercise 31 Passed Successfully!")


if __name__ == "__main__":
    demonstrate_basic_monkey_patching()
    demonstrate_safe_context_patching()
    demonstrate_class_hotfixing()
    # run_exercise_tests()
