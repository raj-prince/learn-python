#!/usr/bin/env python3
"""
================================================================================
LESSON 5: CLASS AND STATIC METHODS — DIFFERENT LEVELS OF BEHAVIOR
================================================================================

So far, every method we have written has been an "Instance Method." They all took
`self` as the first parameter, meaning they operate on a specific object.

However, Python classes can have methods that operate on the *class itself* or behave
as simple *utility functions* grouped inside the class namespace.

--------------------------------------------------------------------------------
1. THE THREE TYPES OF METHODS
--------------------------------------------------------------------------------
- INSTANCE METHODS:
  - Definition: The standard method. Takes `self` as the first argument.
  - Purpose: Read or modify attributes of a specific object instance.

- CLASS METHODS (`@classmethod`):
  - Definition: Marked with the `@classmethod` decorator. Takes `cls` as the first argument.
  - Purpose: Operate on the class, not the instance. Often used as "Factory Methods"
    (alternative constructors to create objects in different ways).

- STATIC METHODS (`@staticmethod`):
  - Definition: Marked with the `@staticmethod` decorator. Takes no special first argument.
  - Purpose: Simple utility functions that don't need access to the class or instance data,
    but are logically related to the class topic.

--------------------------------------------------------------------------------
2. CLASS VARIABLES VS. INSTANCE VARIABLES
--------------------------------------------------------------------------------
- Class Variables: Shared by ALL instances of a class (defined directly under the class header).
- Instance Variables: Unique to each individual instance (defined inside `__init__` using `self.`).

--------------------------------------------------------------------------------
3. THE PIZZA EXAMPLE
--------------------------------------------------------------------------------
Let's see how these three methods and variable types work together in a `Pizza` class!
"""

class Pizza:
    # --- CLASS VARIABLE ---
    # This is shared by all Pizza objects. We use it to track total pizzas sold!
    total_pizzas_sold = 0
    allowed_toppings = ["cheese", "tomato", "pepperoni", "mushrooms", "olives", "basil"]

    def __init__(self, size, toppings):
        self.size = size          # Instance variable
        self.toppings = toppings  # Instance variable
        
        # Increment the class variable whenever a new pizza is created!
        # Note: We access it using the Class name: `Pizza.total_pizzas_sold`
        Pizza.total_pizzas_sold += 1

    # 1. INSTANCE METHOD
    # Operates on a specific pizza. Uses `self` to access that pizza's size/toppings.
    def calculate_price(self):
        base_price = 10 if self.size == "Medium" else 14
        topping_price = len(self.toppings) * 1.5
        return base_price + topping_price

    # 2. CLASS METHOD (Factory Method)
    # Operates on the class `cls`. Used to create pre-configured Pizza recipes!
    # Instead of typing: Pizza("Medium", ["cheese", "tomato", "basil"]), we can just type: Pizza.margherita()
    @classmethod
    def margherita(cls):
        # `cls` refers to the class 'Pizza'. Calling `cls(...)` is the same as calling `Pizza(...)`
        return cls("Medium", ["cheese", "tomato", "basil"])

    @classmethod
    def pepperoni(cls):
        return cls("Large", ["cheese", "tomato", "pepperoni"])

    @classmethod
    def get_total_sold(cls):
        # Class methods can access and return class variables
        return cls.total_pizzas_sold

    # 3. STATIC METHOD
    # A utility function. It doesn't need `self` or `cls`. It just takes a topping name
    # and validates it against our list.
    @staticmethod
    def validate_topping(topping):
        # We can check if a topping is allowed. Note that we access `Pizza.allowed_toppings` directly.
        return topping.lower() in Pizza.allowed_toppings


# ------------------------------------------------------------------------------
# 4. TESTING THE DIFFERENT METHODS
# ------------------------------------------------------------------------------
print("--- Testing Static Method (Utility) ---")
# We can call static methods directly on the class without creating an object!
print(f"Is pepperoni allowed? {Pizza.validate_topping('pepperoni')}") # True
print(f"Is pineapple allowed? {Pizza.validate_topping('pineapple')}") # False

print("\n--- Creating Pizzas using Class Methods (Factories) ---")
# Create pre-configured pizzas using our factory class methods
pizza1 = Pizza.margherita()
pizza2 = Pizza.pepperoni()

# Create a custom pizza using the standard constructor
pizza3 = Pizza("Medium", ["cheese", "mushrooms", "olives"])

print(f"Pizza 1 (Margherita) toppings: {pizza1.toppings}")
print(f"Pizza 2 (Pepperoni) size: {pizza2.size}")

print("\n--- Calculating Prices (Instance Methods) ---")
# Prices are unique to each pizza instance
print(f"Pizza 1 Price: ${pizza1.calculate_price():.2f}")
print(f"Pizza 2 Price: ${pizza2.calculate_price():.2f}")
print(f"Pizza 3 Price: ${pizza3.calculate_price():.2f}")

print("\n--- Checking Class Variable ---")
# Accessing the shared class variable
print(f"Total pizzas sold: {Pizza.get_total_sold()}")


# ================================================================================
# YOUR TURN: EXERCISE 5
# ================================================================================
# Let's practice by creating a `Book` class that tracks total books cataloged
# and offers alternative ways to create books!
#
# INSTRUCTIONS:
# 1. Create a class named `Book`.
# 2. Add a class variable:
#    - `total_books` (int, initialized to 0, increments by 1 on every new Book creation).
# 3. Inside `__init__`, initialize `title` and `author`.
# 4. Create an instance method `get_info(self)` that returns a string:
#    - "[title] by [author]"
# 5. Create a class method `from_string(cls, book_str)`:
#    - This is a factory method that parses a string in the format "Title - Author"
#      and returns a new instance of `Book`.
#      Hint: You can split the string using `book_str.split(" - ")`.
# 6. Create a static method `is_bestseller(copies_sold)`:
#    - Returns True if `copies_sold` is greater than or equal to 100,000, else False.
#
# Un-comment the test code below once you've written your class!
# ================================================================================

# WRITE YOUR Book CLASS HERE:



# --- TEST CODE (Un-comment below to test your implementation) ---
# # Test static method
# print(f"Is 150k sold a bestseller? {Book.is_bestseller(150000)}") # Should be True
# 
# # Test standard constructor
# b1 = Book("1984", "George Orwell")
# print(b1.get_info()) # Should print: 1984 by George Orwell
# 
# # Test factory class method
# b2 = Book.from_string("The Hobbit - J.R.R. Tolkien")
# print(b2.get_info()) # Should print: The Hobbit by J.R.R. Tolkien
# 
# # Test class variable tracking
# print(f"Total books cataloged: {Book.total_books}") # Should be 2
