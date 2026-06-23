#!/usr/bin/env python3
"""
================================================================================
LESSON 9: GENERATORS AND YIELD — MEMORY-EFFICIENT DATA STREAMS
================================================================================

In Python, we often work with collections of data (like lists, tuples, or dicts).
However, loading a massive dataset (like millions of log lines, database rows,
or sensor readings) into a list can completely consume your computer's RAM.

This is where **Generators** and the **`yield`** keyword come to the rescue!
They allow us to produce a stream of values "on-demand" (lazily) instead of 
computing and storing them all in memory at once.

--------------------------------------------------------------------------------
1. THE `yield` KEYWORD
--------------------------------------------------------------------------------
- Standard Function (`return`): Executes its code, returns a single value, 
  and destroys its local state and variables completely.
  
- Generator Function (`yield`): When a function contains `yield`, it becomes a
  Generator. When called, it doesn't run the code immediately. Instead, it returns
  a generator object.
  
  Each time you call `next()` on the generator (or loop over it):
  1. The function runs until it hits `yield`.
  2. It pauses, saves its entire state (local variables, line position), 
     and hands the yielded value back to the caller.
  3. The next time you ask for a value, it resumes *exactly* where it left off!

--------------------------------------------------------------------------------
2. THE POWER OF LAZY EVALUATION (MEMORY SAVINGS)
--------------------------------------------------------------------------------
Let's see this in action with a simple number generator compared to a list.
"""

import sys
import time

# --- A Normal Function that returns a list ---
def get_squares_list(n):
    result = []
    for i in range(n):
        result.append(i * i)
    return result

# --- A Generator Function that yields squares ---
def get_squares_generator(n):
    for i in range(n):
        # We 'yield' instead of appending to a list and returning!
        yield i * i


# ------------------------------------------------------------------------------
# 3. COMPARING LISTS VS. GENERATORS
# ------------------------------------------------------------------------------
limit = 10_000_000  # 10 Million numbers

print("--- Testing memory usage and creation time ---")

# --- Test 1: The List approach ---
t0 = time.time()
my_list = get_squares_list(limit)
t1 = time.time()
list_memory = sys.getsizeof(my_list) / (1024 * 1024) # Convert bytes to Megabytes
print(f"📦 List: took {t1 - t0:.2f}s to create. Memory size: {list_memory:.2f} MB")

# Free up memory
del my_list

# --- Test 2: The Generator approach ---
t0 = time.time()
my_gen = get_squares_generator(limit)
t1 = time.time()
gen_memory = sys.getsizeof(my_gen) / (1024 * 1024) # Convert bytes to Megabytes
# Note how fast and how incredibly small this is!
print(f"⚡ Generator: took {t1 - t0:.4f}s to create. Memory size: {gen_memory:.6f} MB")


# ------------------------------------------------------------------------------
# 4. HOW TO CONSUME A GENERATOR
# ------------------------------------------------------------------------------
print("\n--- Consuming a Generator ---")

# Let's make a small generator for demonstration
def simple_counter():
    print("🎬 Starting generator...")
    yield "First Value"
    print("🔁 Resuming for second value...")
    yield "Second Value"
    print("🔁 Resuming for final value...")
    yield "Third Value"
    print("🏁 Finished!")

# Create the generator object
counter = simple_counter()

# We get values one by one using the built-in next() function
print("Calling next():")
val1 = next(counter)
print(f"-> Received: {val1}\n")

print("Calling next() again:")
val2 = next(counter)
print(f"-> Received: {val2}\n")

print("Calling next() a third time:")
val3 = next(counter)
print(f"-> Received: {val3}\n")

# If we call next() again, the generator runs out of values and raises a 'StopIteration' exception,
# which is how loops know when to stop!
try:
    next(counter)
except StopIteration:
    print("🛑 StopIteration caught! Generator has finished running.")


# ------------------------------------------------------------------------------
# 5. GENERATOR EXPRESSIONS
# ------------------------------------------------------------------------------
# Just like you can write List Comprehensions with square brackets `[...]`,
# you can write Generator Expressions using parentheses `(...)`.
print("\n--- Generator Expressions ---")

list_comp = [x * x for x in range(5)]      # Computes and stores all squares in memory
gen_exp = (x * x for x in range(5))        # Creates a generator object (lazy!)

print(f"List Comprehension: {list_comp}")
print(f"Generator Expression: {gen_exp}")
print("Iterating over generator expression:")
for val in gen_exp:
    print(f"  value: {val}")


# ================================================================================
# YOUR TURN: EXERCISE 9
# ================================================================================
# Let's practice generators by building an Infinite Fibonacci Sequence generator
# and a Log File Reader!
#
# INSTRUCTIONS:
# 1. Complete the generator function `fibonacci_sequence()`.
#    - This generator should run an infinite loop (`while True`) and yield
#      the next number in the Fibonacci sequence (0, 1, 1, 2, 3, 5, 8, 13...).
#      Since generators are lazy, an infinite loop is perfectly safe and won't crash
#      your program! It will only generate a number when we call `next()` or loop.
# 2. Complete the generator function `parse_log_file(filename)`.
#    - Open the specified file using a context manager.
#    - Read the file line-by-line using a loop (to keep memory usage low!).
#    - If a line contains the word "[ERROR]", yield that line (strip any extra whitespace).
#
# Un-comment the test code at the bottom of the file once you've written your solution!
# ================================================================================

# WRITE YOUR GENERATORS HERE:

def fibonacci_sequence():
    # TODO: Initialize two variables for the sequence (e.g. a=0, b=1)
    # Run an infinite loop and yield the next number, then update the values.
    pass


def parse_log_file(filename):
    # TODO: Open file, loop through lines, yield lines containing "[ERROR]"
    pass



# --- TEST CODE (Un-comment below to test your implementation) ---
# # Setup dummy log file
# log_data = """[INFO] 10:00:01 - System booted.
# [INFO] 10:00:05 - Connection established.
# [ERROR] 10:01:23 - Database connection failed!
# [INFO] 10:01:25 - Retrying database connection...
# [ERROR] 10:01:30 - Timeout connecting to database.
# [INFO] 10:02:00 - System shutting down."""
# 
# with open("app_log.txt", "w") as f:
#     f.write(log_data)
# 
# if __name__ == "__main__":
#     print("\n==================================================")
#     print("RUNNING EXERCISE 9 TESTS")
#     print("==================================================")
#     
#     # Test 1: Infinite Fibonacci
#     print("🌀 Testing Fibonacci Generator (first 8 values):")
#     fib_gen = fibonacci_sequence()
#     if fib_gen:
#         for _ in range(8):
#             print(next(fib_gen), end=" ")
#         print()
#     
#     # Test 2: Log File Parser
#     print("\n📋 Testing Log File Parser (extracting errors):")
#     errors = parse_log_file("app_log.txt")
#     if errors:
#         for err in errors:
#             print(f"  Filtered Error: {err}")
