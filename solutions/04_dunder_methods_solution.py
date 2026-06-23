#!/usr/bin/env python3
"""
================================================================================
LESSON 4: MAGIC (DUNDER) METHODS — SOLUTION
================================================================================
"""

class TimeDuration:
    def __init__(self, hours, minutes):
        # Normalize minutes (e.g. 75 minutes becomes 1 hour and 15 minutes)
        extra_hours = minutes // 60
        self.minutes = minutes % 60
        self.hours = hours + extra_hours

    def __str__(self):
        return f"{self.hours}h {self.minutes}m"

    def __repr__(self):
        return f"TimeDuration(hours={self.hours}, minutes={self.minutes})"

    def __add__(self, other):
        if isinstance(other, TimeDuration):
            # Add hours and minutes separately, then let the constructor normalize them!
            total_hours = self.hours + other.hours
            total_minutes = self.minutes + other.minutes
            return TimeDuration(total_hours, total_minutes)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, TimeDuration):
            # Compare total minutes of both durations
            self_total = (self.hours * 60) + self.minutes
            other_total = (other.hours * 60) + other.minutes
            return self_total == other_total
        return False


# --- TEST CODE ---
print("--- Running TimeDuration Tests ---")
t1 = TimeDuration(1, 45)
t2 = TimeDuration(2, 30)
t3 = TimeDuration(0, 105) # 105 minutes = 1h 45m

print(f"t1: {t1}") # Should print: 1h 45m
print(f"t2: {t2}") # Should print: 2h 30m
print(f"t3: {t3}") # Should print: 1h 45m

print(f"Is t1 equal to t3? {t1 == t3}") # Should print: True

t_sum = t1 + t2
print(f"t1 + t2 = {t_sum}") # Should print: 4h 15m
