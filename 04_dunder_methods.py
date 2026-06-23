#!/usr/bin/env python3
"""
================================================================================
LESSON 4: MAGIC (DUNDER) METHODS — HOOKING INTO PYTHON'S SYNTAX
================================================================================

Have you ever wondered how Python knows how to add two numbers with `+`, or how it
knows the length of a list with `len()`? 

Python uses special methods called "Dunder Methods" (short for "Double Under", 
because they start and end with double underscores: `__method__`). 
By implementing these methods in our custom classes, we can hook directly into 
Python's built-in operators and functions. This is called "Operator Overloading."

--------------------------------------------------------------------------------
1. COMMON DUNDER METHODS
--------------------------------------------------------------------------------
- `__init__(self, ...)` : The constructor (which you already know!).
- `__str__(self)`       : Defines what happens when you `print(obj)` or `str(obj)`.
                          Should return a clean, user-friendly string.
- `__repr__(self)`      : Defines the developer-friendly representation. 
                          Ideally, it should show how to recreate the object.
- `__len__(self)`       : Hooks into the `len(obj)` function.
- `__add__(self, other)`: Hooks into the addition operator `+`.
- `__eq__(self, other)` : Hooks into the equality operator `==`.

--------------------------------------------------------------------------------
2. THE PLAYLIST EXAMPLE
--------------------------------------------------------------------------------
Let's build a custom `Playlist` class to see how these dunder methods make
our class feel like a native Python data type.
"""

class Playlist:
    def __init__(self, name, songs=None):
        self.name = name
        # If no songs are provided, initialize with an empty list
        self.songs = songs if songs is not None else []

    # 1. USER-FRIENDLY STRING REPRESENTATION
    def __str__(self):
        song_list = ", ".join(self.songs) if self.songs else "Empty"
        return f"🎶 Playlist '{self.name}' ({len(self.songs)} songs) -> [{song_list}]"

    # 2. DEVELOPER-FRIENDLY STRING REPRESENTATION
    def __repr__(self):
        return f"Playlist(name={repr(self.name)}, songs={repr(self.songs)})"

    # 3. HOOKING INTO len()
    def __len__(self):
        return len(self.songs)

    # 4. HOOKING INTO + OPERATOR
    # This allows us to do: playlist1 + playlist2
    def __add__(self, other):
        # We make sure we are adding another Playlist object
        if isinstance(other, Playlist):
            combined_name = f"{self.name} + {other.name}"
            combined_songs = self.songs + other.songs
            return Playlist(combined_name, combined_songs)
        
        # If it's not a Playlist, raise a TypeError
        return NotImplemented

    # 5. HOOKING INTO == OPERATOR
    def __eq__(self, other):
        if isinstance(other, Playlist):
            # Two playlists are equal if they have the same songs in the same order
            return self.songs == other.songs
        return False


# ------------------------------------------------------------------------------
# 3. TESTING DUNDER METHODS
# ------------------------------------------------------------------------------
# Create two playlists
rock_mix = Playlist("Rock Classics", ["Bohemian Rhapsody", "Back in Black"])
pop_mix = Playlist("Pop Hits", ["Levitating", "Blinding Lights"])

print("--- Testing __str__ and __repr__ ---")
# When we print(), Python calls __str__ behind the scenes!
print(rock_mix) 

# When we inspect the raw representation (or in a list/shell), Python calls __repr__
print(f"Developer representation: {repr(rock_mix)}")

print("\n--- Testing __len__ ---")
# len() calls __len__ behind the scenes
print(f"Number of songs in pop_mix: {len(pop_mix)}")

print("\n--- Testing __add__ (Playlist Merging) ---")
# Using the '+' operator calls __add__!
mega_playlist = rock_mix + pop_mix
print(mega_playlist)

print("\n--- Testing __eq__ (Equality) ---")
# Create another playlist with the exact same songs
another_pop = Playlist("My Pop Collection", ["Levitating", "Blinding Lights"])

print(f"Is pop_mix equal to another_pop? {pop_mix == another_pop}")  # True
print(f"Is pop_mix equal to rock_mix? {pop_mix == rock_mix}")        # False


# ================================================================================
# YOUR TURN: EXERCISE 4
# ================================================================================
# Let's practice by creating a `TimeDuration` class representing hours and minutes.
#
# INSTRUCTIONS:
# 1. Create a class named `TimeDuration`.
# 2. Inside `__init__`, initialize `hours` (int) and `minutes` (int).
#    - Normalize minutes! If minutes is 65, it should become 1 hour and 5 minutes.
#    - Hint: `extra_hours = minutes // 60` and `remaining_minutes = minutes % 60`.
# 3. Implement `__str__` to return a friendly format like: "2h 45m" or "0h 15m".
# 4. Implement `__add__` to allow adding two `TimeDuration` objects together.
#    - Example: `TimeDuration(1, 40) + TimeDuration(2, 30)` should return a new
#      `TimeDuration` object representing 4 hours and 10 minutes.
# 5. Implement `__eq__` to compare if two `TimeDuration` objects are equal in total minutes.
#
# Un-comment the test code below once you've written your class!
# ================================================================================

# WRITE YOUR TimeDuration CLASS HERE:



# --- TEST CODE (Un-comment below to test your implementation) ---
# t1 = TimeDuration(1, 45)
# t2 = TimeDuration(2, 30)
# t3 = TimeDuration(0, 105) # 105 minutes = 1h 45m
# 
# print(f"t1: {t1}") # Should print: 1h 45m
# print(f"t2: {t2}") # Should print: 2h 30m
# print(f"t3: {t3}") # Should print: 1h 45m
# 
# print(f"Is t1 equal to t3? {t1 == t3}") # Should print: True
# 
# t_sum = t1 + t2
# print(f"t1 + t2 = {t_sum}") # Should print: 4h 15m (1h 45m + 2h 30m = 3h 75m -> 4h 15m)
