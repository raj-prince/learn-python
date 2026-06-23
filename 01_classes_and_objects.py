#!/usr/bin/env python3
"""
================================================================================
LESSON 1: CLASSES AND OBJECTS — THE BLUEPRINT AND THE INSTANCE
================================================================================

Welcome to the world of Object-Oriented Programming (OOP) in Python!
OOP is a programming paradigm that uses "objects" to represent data and methods.
It helps us organize our code to mimic the real world, making it more modular, 
reusable, and easier to understand.

--------------------------------------------------------------------------------
1. THE CORE CONCEPTS
--------------------------------------------------------------------------------
- CLASS: A blueprint, template, or recipe for creating objects. It defines the
         structure (attributes) and behaviors (methods) that its objects will have.
         Think of it as a cookie cutter.

- OBJECT (INSTANCE): An individual, concrete instance created from the class blueprint.
                     Think of it as the actual cookie stamped out by the cookie cutter.
                     Each cookie can have different toppings (data), but they all 
                     share the same basic shape.

--------------------------------------------------------------------------------
2. A SIMPLE EXAMPLE: THE SUPERHERO CLASS
--------------------------------------------------------------------------------
Let's build a blueprint for a Superhero.
"""

class Superhero:
    # The __init__ method is a special method called a CONSTRUCTOR.
    # Python runs it automatically whenever we create a new object from this class.
    # It initializes the object's attributes (its data).
    def __init__(self, name, superpower, energy_level=100):
        # 'self' refers to the specific object we are creating right now.
        # Think of it as saying: "This particular superhero's name is..."
        self.name = name
        self.superpower = superpower
        self.energy_level = energy_level  # A default value if none is provided

    # A METHOD is a function defined inside a class. 
    # It represents the actions or behaviors our object can perform.
    # Note: Every instance method MUST take 'self' as its first parameter.
    def introduce(self):
        print(f"🦸‍♂️ I am {self.name}! My power is {self.superpower}!")

    def use_power(self, intensity):
        if self.energy_level >= intensity:
            self.energy_level -= intensity
            print(f"🔥 {self.name} uses {self.superpower}! (Energy used: {intensity}, Remaining: {self.energy_level})")
        else:
            print(f"😴 {self.name} is too tired to use their power! Energy level: {self.energy_level}")

    def rest(self):
        self.energy_level = 100
        print(f"🔋 {self.name} took a nap! Energy restored to 100.")


# ------------------------------------------------------------------------------
# 3. CREATING AND USING OBJECTS (INSTANTIATION)
# ------------------------------------------------------------------------------
print("--- Creating our Superheroes ---")

# We create an object by calling the class name as if it were a function,
# passing the arguments that __init__ expects (except 'self', Python handles that!).
hero1 = Superhero("Shadow Weaver", "Teleportation")
hero2 = Superhero("Inferno", "Fire Manipulation", energy_level=80)

# Accessing attributes using dot notation (.)
print(f"Hero 1 Name: {hero1.name}")
print(f"Hero 2 Power: {hero2.superpower}")

print("\n--- Testing their Behaviors (Methods) ---")
# Calling methods on our objects
hero1.introduce()
hero2.introduce()

hero1.use_power(30)
hero1.use_power(80) # This should fail because energy will be too low (100 - 30 = 70, 70 < 80)
hero1.rest()
hero1.use_power(80) # This should succeed now!

# Each object maintains its own independent state
print(f"\nShadow Weaver's Energy: {hero1.energy_level}")
print(f"Inferno's Energy: {hero2.energy_level}")


# ================================================================================
# YOUR TURN: EXERCISE 1
# ================================================================================
# Let's practice! You will create a class representing a SmartDevice (like a phone).
#
# INSTRUCTIONS:
# 1. Define a class named `SmartDevice`.
# 2. Inside `__init__`, initialize three attributes:
#    - `model` (string)
#    - `battery_level` (integer, default is 100)
#    - `is_on` (boolean, default is False)
# 3. Create a method `turn_on` that sets `is_on` to True and prints a message.
# 4. Create a method `use_app` that takes `app_name` and `battery_cost`. 
#    - If the device is off, print a warning: "Cannot use app. Device is off."
#    - If it's on, check if there is enough battery. If yes, subtract the cost and
#      print "Running [app_name]...". If not, print "Low battery! Please charge."
# 5. Create a method `charge` that resets `battery_level` to 100.
#
# Un-comment the test code below once you've written your class!
# ================================================================================

# WRITE YOUR SmartDevice CLASS HERE:



# --- TEST CODE (Un-comment below to test your implementation) ---
# my_phone = SmartDevice("AeroPhone X")
# my_phone.use_app("Camera", 15) # Should fail (device is off)
# my_phone.turn_on()
# my_phone.use_app("Camera", 15) # Should succeed
# my_phone.use_app("3D Game", 90) # Should fail (battery low: 85 - 90 < 0)
# my_phone.charge()
# my_phone.use_app("3D Game", 90) # Should succeed now
