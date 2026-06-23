#!/usr/bin/env python3
"""
================================================================================
LESSON 10: DECORATORS — MODIFYING BEHAVIOR DYNAMICALLY
================================================================================

You have already used decorators in earlier lessons, like `@property`, 
`@classmethod`, and `@staticmethod`. But what exactly is a decorator, and 
how do you write your own?

A **Decorator** is a function that takes another function as an argument, 
extends or modifies its behavior, and returns a new function—all without 
modifying the original function's source code!

--------------------------------------------------------------------------------
1. FUNCTIONS ARE FIRST-CLASS CITIZENS
--------------------------------------------------------------------------------
To understand decorators, you must remember that in Python, functions are objects.
This means:
- You can assign functions to variables.
- You can pass functions as arguments to other functions.
- You can return functions from inside other functions (nested functions).

--------------------------------------------------------------------------------
2. WRITING YOUR FIRST DECORATOR
--------------------------------------------------------------------------------
Let's build a simple decorator that logs when a function starts and ends.
"""

from functools import wraps
import time

# This is our decorator function
def log_execution(func):
    # We use @wraps from the functools module to preserve the original 
    # function's name and docstring. Without this, our decorated function 
    # would report its name as "wrapper"!
    @wraps(func)
    # *args and **kwargs allow the wrapper to accept ANY arguments that the
    # original function might have.
    def wrapper(*args, **kwargs):
        print(f"📢 [LOG] Calling function: '{func.__name__}'")
        
        # Call the original function and capture its return value
        result = func(*args, **kwargs)
        
        print(f"📢 [LOG] Function '{func.__name__}' completed execution.")
        # Return the result so the caller gets what they expect
        return result
        
    return wrapper # Return the new wrapper function


# ------------------------------------------------------------------------------
# 3. USING THE DECORATOR WITH THE @ SYNTAX
# ------------------------------------------------------------------------------
# The '@' symbol is just syntactic sugar. Writing:
#   @log_execution
#   def greet(): ...
# Is exactly the same as writing:
#   greet = log_execution(greet)

@log_execution
def greet(name):
    print(f"👋 Hello, {name}!")

@log_execution
def add_numbers(a, b):
    return a + b

print("--- Testing Greet ---")
greet("Alice")

print("\n--- Testing Add Numbers ---")
total = add_numbers(5, 7)
print(f"Total: {total}")


# ------------------------------------------------------------------------------
# 4. PRACTICAL EXAMPLE: AN EXECUTION TIMER DECORATOR
# ------------------------------------------------------------------------------
# Let's write a decorator that measures how long a function takes to run.
def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"⏱️ '{func.__name__}' took {end_time - start_time:.4f} seconds to execute.")
        return result
    return wrapper

@time_it
def heavy_calculation():
    print("🧠 Starting calculation...")
    time.sleep(0.5) # Simulate workload
    print("🧠 Calculation complete!")

print("\n--- Testing Timer Decorator ---")
heavy_calculation()


# ================================================================================
# YOUR TURN: EXERCISE 10
# ================================================================================
# Let's practice by creating a `@count_calls` decorator!
#
# Scenario:
# You want to track how many times a particular function is called throughout 
# your program's execution.
#
# INSTRUCTIONS:
# 1. Write a decorator named `count_calls`.
# 2. Inside the decorator, you need to store a counter. Since the wrapper function
#    is defined inside `count_calls`, we can attach the counter directly to the
#    wrapper function object!
#    Hint: Inside `count_calls`, define `wrapper`. Before returning it, initialize
#          `wrapper.calls = 0`.
# 3. Inside the `wrapper` function:
#    - Increment `wrapper.calls` by 1.
#    - Print a message: "Function [name] has been called [calls] times."
#    - Call the original function and return its result.
#
# Un-comment the test code at the bottom of the file once you've written your solution!
# ================================================================================

# WRITE YOUR count_calls DECORATOR HERE:




# --- TEST CODE (Un-comment below to test your implementation) ---
# @count_calls
# def process_payment(amount):
#     print(f"💳 Processing payment of ${amount}...")
# 
# @count_calls
# def send_notification(user):
#     print(f"📧 Sending notification to {user}...")
# 
# if __name__ == "__main__":
#     print("\n==================================================")
#     print("RUNNING EXERCISE 10 TESTS")
#     print("==================================================")
#     
#     # Test process_payment calls
#     process_payment(100)
#     process_payment(250)
#     
#     # Test send_notification calls
#     send_notification("Bob")
#     
#     # Test process_payment again to see the counter incrementing
#     process_payment(50)
#     
#     # Final check of the counts
#     print(f"\nFinal payment call count: {process_payment.calls}") # Should be 3
#     print(f"Final notification call count: {send_notification.calls}") # Should be 1
