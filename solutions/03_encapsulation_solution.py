#!/usr/bin/env python3
"""
================================================================================
LESSON 3: ENCAPSULATION — SOLUTION
================================================================================
"""

class Thermostat:
    def __init__(self, initial_temperature=20):
        # Initialize the protected attribute.
        # Note: We can also pass it through the setter to validate the initial temperature!
        self._temperature = 20
        self.temperature = initial_temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if 10 <= value <= 35:
            self._temperature = value
        else:
            print(f"❌ Warning: Temperature {value}°C is out of range! Must be between 10°C and 35°C.")

    def boost_heating(self):
        print(f"🔥 Boosting heating by 5°C...")
        # We use the setter (self.temperature) so that the validation checks are applied
        self.temperature = self.temperature + 5


# --- TEST CODE ---
print("--- Running Thermostat Tests ---")
home_thermostat = Thermostat(22)
print(f"Current temp: {home_thermostat.temperature}°C")

home_thermostat.temperature = 28 # Should succeed
print(f"New temp: {home_thermostat.temperature}°C")

home_thermostat.temperature = 40 # Should print warning and NOT change temp
print(f"Temp after invalid set: {home_thermostat.temperature}°C")

home_thermostat.boost_heating() # Should boost to 33°C
print(f"Temp after boost: {home_thermostat.temperature}°C")

home_thermostat.boost_heating() # Should print warning (33 + 5 = 38 is out of range)
print(f"Temp after second boost attempt: {home_thermostat.temperature}°C")
