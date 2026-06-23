#!/usr/bin/env python3
"""
================================================================================
LESSON 6: FILE I/O AND CONTEXT MANAGERS — WORKING WITH EXTERNAL DATA
================================================================================

In real-world applications, programs need to read and write data to files,
databases, or network sockets. Managing these external resources properly is 
critical because leaving files open can cause memory leaks, file locks, or data loss.

--------------------------------------------------------------------------------
1. THE OLD WAY VS. THE NEW WAY (CONTEXT MANAGERS)
--------------------------------------------------------------------------------
- Old Way (Explicit close):
    f = open("example.txt", "r")
    data = f.read()
    # If an error happens here, the file is never closed!
    f.close()

- New Way (Context Manager using `with`):
    with open("example.txt", "r") as f:
        data = f.read()
    # The file is AUTOMATICALLY closed here, even if an error occurs inside!

The `with` statement is a powerful Python feature powered by "Context Managers."

--------------------------------------------------------------------------------
2. READING AND WRITING TEXT FILES
--------------------------------------------------------------------------------
Common file modes:
- 'r' : Read (default). Fails if the file doesn't exist.
- 'w' : Write. Overwrites the file if it exists, or creates a new one.
- 'a' : Append. Writes data to the end of the file without overwriting.
"""

import json
import time

# --- Creating a dummy file to read ---
with open("sample_data.txt", "w") as f:
    f.write("Line 1: Learning Python is awesome!\n")
    f.write("Line 2: File IO is easy with context managers.\n")
    f.write("Line 3: Keep practicing!\n")

# 1. READING A FILE
print("--- Reading File Content ---")
with open("sample_data.txt", "r") as file:
    # Read the entire file as a single string
    content = file.read()
    print("Full Content:\n", content)

with open("sample_data.txt", "r") as file:
    # Read line-by-line using a loop (extremely memory efficient for large files!)
    print("Reading Line by Line:")
    for line in file:
        print(f"  > {line.strip()}") # strip() removes the newline character \n

# 2. WORKING WITH JSON
# JSON (JavaScript Object Notation) is the standard format for exchanging data.
# Python has a built-in `json` module to serialize (dump) and deserialize (load) JSON.
print("\n--- Working with JSON Data ---")
user_profile = {
    "username": "coder_neo",
    "level": 42,
    "skills": ["Python", "OOP", "File I/O"],
    "is_active": True
}

# Writing JSON to a file
with open("user.json", "w") as json_file:
    # indent=4 formats it beautifully
    json.dump(user_profile, json_file, indent=4)
    print("Saved user_profile to user.json")

# Reading JSON from a file
with open("user.json", "r") as json_file:
    loaded_data = json.load(json_file)
    print("Loaded JSON Data:", loaded_data)
    print(f"User's primary skill: {loaded_data['skills'][0]}")


# ------------------------------------------------------------------------------
# 3. CONNECTING TO OOP: CUSTOM CONTEXT MANAGERS
# ------------------------------------------------------------------------------
# Any class can become a context manager and support the `with` statement
# by implementing two dunder methods:
# - `__enter__(self)`: Setup code (runs when entering the `with` block).
# - `__exit__(self, exc_type, exc_val, exc_tb)`: Teardown code (runs when leaving).
#
# Let's build a simple Timer context manager to measure how long code takes to run!

class ExecutionTimer:
    def __enter__(self):
        self.start_time = time.time()
        # Whatever is returned here is assigned to the variable after 'as'
        return self 

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        duration = self.end_time - self.start_time
        print(f"⏱️ Execution completed in {duration:.4f} seconds.")
        # Returning False (or None) let's any exception bubble up.
        # Returning True would suppress any exceptions that occurred inside the block.
        return False


# Let's test our custom context manager!
print("\n--- Testing Custom Context Manager ---")
with ExecutionTimer():
    print("Starting a heavy computation...")
    # Simulate work by sleeping for 0.5 seconds
    time.sleep(0.5)
    print("Heavy computation finished!")


# ================================================================================
# YOUR TURN: EXERCISE 6
# ================================================================================
# Let's practice File I/O and JSON by writing a small log processor.
#
# INSTRUCTIONS:
# 1. Create a JSON file named `servers.json` containing a list of server dictionaries.
#    I have written the data structure for you below in `servers_data`. Write this
#    data to `servers.json`.
# 2. Read `servers.json` back into your program.
# 3. Process the data: Filter and find all servers where `"status"` is `"offline"`.
# 4. Write the names of all offline servers into a plain text file named `offline_report.txt`,
#    with one server name per line.
#
# Un-comment the test code below once you've written your solution!
# ================================================================================

servers_data = [
    {"name": "Web-Server-01", "ip": "192.168.1.1", "status": "online"},
    {"name": "DB-Server-Primary", "ip": "192.168.1.2", "status": "offline"},
    {"name": "Cache-Node-A", "ip": "192.168.1.3", "status": "online"},
    {"name": "Auth-Gateway", "ip": "192.168.1.4", "status": "offline"},
    {"name": "Backup-Vault", "ip": "192.168.1.5", "status": "offline"}
]

# WRITE YOUR CODE HERE:




# --- TEST CODE (Un-comment below to test your implementation) ---
# # Verify the report exists and has the correct contents
# print("\n--- Verifying Offline Report ---")
# try:
#     with open("offline_report.txt", "r") as report:
#         lines = report.readlines()
#         print("Offline servers found in report:")
#         for line in lines:
#             print(f"  - {line.strip()}")
#         
#         # Quick validation
#         expected = ["DB-Server-Primary", "Auth-Gateway", "Backup-Vault"]
#         actual = [line.strip() for line in lines]
#         if actual == expected:
#             print("🎉 Success! The report is 100% correct.")
#         else:
#             print("⚠️ The report contents don't match the expected offline servers.")
# except FileNotFoundError:
#     print("❌ Error: offline_report.txt was not found. Make sure you write to this file!")
