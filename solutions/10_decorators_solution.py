#!/usr/bin/env python3
"""
================================================================================
LESSON 10: DECORATORS — SOLUTION
================================================================================
"""
from functools import wraps

def count_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Increment the call counter attached to the wrapper
        wrapper.calls += 1
        print(f"📈 [COUNT] Function '{func.__name__}' has been called {wrapper.calls} time(s).")
        return func(*args, **kwargs)
    
    # Initialize the counter attribute on the wrapper function object
    # Functions in Python are objects, so we can dynamically assign attributes to them!
    wrapper.calls = 0
    return wrapper


# --- TEST CODE ---
@count_calls
def process_payment(amount):
    print(f"💳 Processing payment of ${amount}...")

@count_calls
def send_notification(user):
    print(f"📧 Sending notification to {user}...")

if __name__ == "__main__":
    print("\n==================================================")
    print("RUNNING EXERCISE 10 TESTS")
    print("==================================================")
    
    # Test process_payment calls
    process_payment(100)
    process_payment(250)
    
    # Test send_notification calls
    send_notification("Bob")
    
    # Test process_payment again to see the counter incrementing
    process_payment(50)
    
    # Final check of the counts
    print(f"\nFinal payment call count: {process_payment.calls}") # Should be 3
    print(f"Final notification call count: {send_notification.calls}") # Should be 1
