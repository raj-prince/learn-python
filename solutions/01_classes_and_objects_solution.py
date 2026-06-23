#!/usr/bin/env python3
"""
================================================================================
LESSON 1: CLASSES AND OBJECTS — SOLUTION
================================================================================
"""

class SmartDevice:
    def __init__(self, model, battery_level=100, is_on=False):
        self.model = model
        self.battery_level = battery_level
        self.is_on = is_on

    def turn_on(self):
        self.is_on = True
        print(f"📱 {self.model} is now ON.")

    def use_app(self, app_name, battery_cost):
        if not self.is_on:
            print(f"❌ Cannot use {app_name}. {self.model} is OFF.")
            return

        if self.battery_level >= battery_cost:
            self.battery_level -= battery_cost
            print(f"🚀 Running {app_name}... Battery is now at {self.battery_level}%.")
        else:
            print(f"🪫 Low battery! Cannot run {app_name}. Please charge.")

    def charge(self):
        self.battery_level = 100
        print(f"🔌 {self.model} is fully charged to 100%.")


# --- TEST CODE ---
print("--- Running SmartDevice Tests ---")
my_phone = SmartDevice("AeroPhone X")
my_phone.use_app("Camera", 15) # Should fail (device is off)
my_phone.turn_on()
my_phone.use_app("Camera", 15) # Should succeed
my_phone.use_app("3D Game", 90) # Should fail (battery low)
my_phone.charge()
my_phone.use_app("3D Game", 90) # Should succeed now
