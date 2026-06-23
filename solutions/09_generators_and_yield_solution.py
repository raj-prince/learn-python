#!/usr/bin/env python3
"""
================================================================================
LESSON 9: GENERATORS AND YIELD — SOLUTION
================================================================================
"""

def fibonacci_sequence():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def parse_log_file(filename):
    # Context manager automatically closes the file when done
    with open(filename, "r") as file:
        # Loop over the file line-by-line (highly memory-efficient!)
        for line in file:
            if "[ERROR]" in line:
                # Yield the filtered error line on-demand
                yield line.strip()


# --- TEST CODE ---
# Setup dummy log file
log_data = """[INFO] 10:00:01 - System booted.
[INFO] 10:00:05 - Connection established.
[ERROR] 10:01:23 - Database connection failed!
[INFO] 10:01:25 - Retrying database connection...
[ERROR] 10:01:30 - Timeout connecting to database.
[INFO] 10:02:00 - System shutting down."""

with open("app_log.txt", "w") as f:
    f.write(log_data)

if __name__ == "__main__":
    print("\n==================================================")
    print("RUNNING EXERCISE 9 TESTS")
    print("==================================================")
    
    # Test 1: Infinite Fibonacci
    print("🌀 Testing Fibonacci Generator (first 8 values):")
    fib_gen = fibonacci_sequence()
    for _ in range(8):
        print(next(fib_gen), end=" ")
    print()
    
    # Test 2: Log File Parser
    print("\n📋 Testing Log File Parser (extracting errors):")
    errors = parse_log_file("app_log.txt")
    for err in errors:
        print(f"  Filtered Error: {err}")
