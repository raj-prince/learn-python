#!/usr/bin/env python3
"""
================================================================================
LESSON 11: METAPROGRAMMING AND METACLASSES — CODE THAT WRITES CODE
================================================================================

In Python, there is a famous saying: "Everything is an object." 
This is literally true. Integers, strings, functions, and even **Classes themselves**
are objects!

Since a class is an object, it must be an instance of something. In Python, 
classes are instances of a special class called a **Metaclass**. 
By default, the metaclass for all Python classes is **`type`**.

Metaprogramming refers to the ability of a program to inspect, modify, or generate
its own code at runtime. Metaclasses are the ultimate tool for metaprogramming:
they allow you to customize how classes are created!

--------------------------------------------------------------------------------
1. DYNAMIC CLASS CREATION WITH `type`
--------------------------------------------------------------------------------
Usually, we create classes using the `class` keyword. However, because classes
are objects, we can create them dynamically at runtime using the `type()` function!

`type(name, bases, dict)` takes:
1. `name` (string): The name of the class.
2. `bases` (tuple): The parent classes to inherit from.
3. `dict` (dictionary): The attributes and methods of the class.
"""

# Dynamic creation of a class
# This is exactly equivalent to:
#   class Robot:
#       def greet(self):
#           print("Hello, I am a robot!")
def robot_greet(self):
    print("🤖 Hello, I am a robot!")

# We create the Robot class dynamically!
Robot = type("Robot", (object,), {"greet": robot_greet, "version": 1.0})

print("--- Testing Dynamically Created Class ---")
bot = Robot()
print(f"Robot class: {Robot}")
print(f"Robot version: {bot.version}")
bot.greet()


# ------------------------------------------------------------------------------
# 2. WHAT IS A METACLASS?
# ------------------------------------------------------------------------------
# A Metaclass is a class whose instances are classes.
# To create a custom metaclass, we inherit from `type` and override the `__new__` method.
#
# - `__new__(cls, name, bases, dct)`: Runs when Python compiles the class.
#   It allows us to inspect, modify, or validate the class structure BEFORE it is created.

class UpperCaseMethodMeta(type):
    def __new__(cls, name, bases, dct):
        # We intercept class creation!
        # Let's automatically convert all method names to UPPERCASE.
        uppercase_dct = {}
        for attr_name, attr_val in dct.items():
            # If the attribute is a function (method) and doesn't start with double underscore
            if callable(attr_val) and not attr_name.startswith("__"):
                uppercase_dct[attr_name.upper()] = attr_val
            else:
                uppercase_dct[attr_name] = attr_val

        # Call the parent type.__new__ to actually create the class with our modified dictionary
        return super().__new__(cls, name, bases, uppercase_dct)


# 3. USING A CUSTOM METACLASS
# We pass our metaclass into the class definition using the `metaclass` keyword parameter.
class User(metaclass=UpperCaseMethodMeta):
    def login(self):
        print("🔑 Logging in user...")

    def logout(self):
        print("🚪 Logging out user...")

print("\n--- Testing Custom Metaclass (UpperCaseMethodMeta) ---")
u = User()
# u.login() will fail because the metaclass renamed it to LOGIN!
try:
    u.login()
except AttributeError:
    print("AttributeError: 'User' object has no attribute 'login' (Metaclass renamed it!)")

# This works!
u.LOGIN()
u.LOGOUT()


# ================================================================================
# YOUR TURN: EXERCISE 11
# ================================================================================
# Let's practice metaprogramming by building an **Automatic Class Registry**!
#
# Scenario:
# You are building a plugin system or an API handler. Every time a developer defines
# a new handler class, you want it to automatically register itself in a global
# dictionary, so your server knows it exists without manual configuration.
#
# INSTRUCTIONS:
# 1. Create a global dictionary named `PLUGINS = {}`.
# 2. Define a custom Metaclass named `PluginRegistryMeta` that inherits from `type`.
# 3. Inside `PluginRegistryMeta.__new__`:
#    - Intercept class creation.
#    - If the class name is NOT "BasePlugin" (we want to skip registering the base class),
#      add the class to the `PLUGINS` dictionary, where:
#        - Key: The name of the class (or a custom `"plugin_name"` attribute if defined in the class).
#        - Value: The class object itself.
#    - Call `super().__new__` to create the class and return it.
# 4. Create a base class `BasePlugin` that uses `PluginRegistryMeta` as its metaclass.
#
# Un-comment the test code at the bottom of the file once you've written your solution!
# ================================================================================

# WRITE YOUR METACLASS AND BASE CLASS HERE:

PLUGINS = {}




# --- TEST CODE (Un-comment below to test your implementation) ---
# # Developers can now write plugins, and they register AUTOMATICALLY!
# class ImageCompressor(BasePlugin):
#     def run(self):
#         print("🖼️ Compressing image...")
# 
# class TextTranslator(BasePlugin):
#     def run(self):
#         print("📝 Translating text...")
# 
# if __name__ == "__main__":
#     print("\n==================================================")
#     print("RUNNING EXERCISE 11 TESTS")
#     print("==================================================")
#     
#     # Check if the plugins were registered automatically by the metaclass
#     print(f"Registered Plugins: {list(PLUGINS.keys())}")
#     
#     # Instantiate and run all registered plugins dynamically!
#     print("\nExecuting all registered plugins:")
#     for plugin_name, plugin_class in PLUGINS.items():
#         instance = plugin_class()
#         print(f"Running: {plugin_name}")
#         instance.run()
