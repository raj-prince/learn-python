#!/usr/bin/env python3
"""
================================================================================
LESSON 3: ENCAPSULATION — DATA PROTECTION AND GETTERS/SETTERS
================================================================================

In this lesson, we will explore Encapsulation, another core pillar of OOP.
Encapsulation is the practice of hiding the internal state and implementation
details of an object, and exposing a clean, controlled interface to the outside world.

--------------------------------------------------------------------------------
1. WHY DO WE NEED ENCAPSULATION?
--------------------------------------------------------------------------------
Imagine a `BankAccount` class with a `balance` attribute. If anyone can write:
    `my_account.balance = 1000000`
without actually depositing money, the banking system breaks! 

Encapsulation lets us protect attributes so they can only be changed through
valid, authorized methods (like `deposit` and `withdraw`), which can enforce rules
(like "no negative deposits").

--------------------------------------------------------------------------------
2. ACCESS MODIFIERS IN PYTHON (PUBLIC, PROTECTED, PRIVATE)
--------------------------------------------------------------------------------
Unlike languages like Java or C++, Python does not have strict keyword-enforced
privacy (like `private` or `public`). Instead, Python uses naming conventions:

- PUBLIC (e.g., `self.name`): 
  Accessible from anywhere. Anyone can read or modify this attribute directly.

- PROTECTED (e.g., `self._balance` - SINGLE UNDERSCORE):
  A gentle warning to other programmers: "This is internal. Please do not access
  or modify this directly outside of this class or its subclasses." Python
  won't stop you, but it's a strong social convention.

- PRIVATE (e.g., `self.__pin` - DOUBLE UNDERSCORE):
  Python triggers a mechanism called "Name Mangling" for double-underscore attributes.
  It changes the internal name to `_ClassName__attributeName`. This makes it 
  much harder to access directly from outside, acting as a true private variable.

--------------------------------------------------------------------------------
3. THE PYTHONIC WAY: THE `@property` DECORATOR (GETTERS & SETTERS)
--------------------------------------------------------------------------------
Sometimes we want to access a protected attribute as if it were a normal attribute,
but still have validation when we edit it. Python uses the `@property` decorator
to achieve this beautifully.
"""

class BankAccount:
    def __init__(self, owner, initial_balance):
        self.owner = owner          # Public attribute
        self._balance = initial_balance  # Protected attribute (use with care)
        self.__pin = "1234"         # Private attribute (name mangled)

    # 1. THE GETTER (using @property)
    # This allows us to read the balance like: `print(account.balance)`
    # instead of calling a method like: `print(account.get_balance())`
    @property
    def balance(self):
        return self._balance

    # 2. THE SETTER (using @balance.setter)
    # This allows us to set the balance like: `account.balance = 500`
    # BUT it runs this validation code first!
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("❌ Error: Balance cannot be negative!")
        else:
            self._balance = amount

    # A standard public method
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"💰 Deposited ${amount}. New Balance: ${self._balance}")
        else:
            print("❌ Error: Deposit amount must be positive!")

    # A method that requires our private PIN
    def withdraw(self, amount, pin):
        if pin != self.__pin:
            print("❌ Error: Invalid PIN! Access denied.")
            return

        if amount > self._balance:
            print("❌ Error: Insufficient funds!")
        elif amount <= 0:
            print("❌ Error: Withdrawal amount must be positive!")
        else:
            self._balance -= amount
            print(f"💸 Withdrew ${amount}. Remaining Balance: ${self._balance}")


# ------------------------------------------------------------------------------
# 4. TESTING ENCAPSULATION
# ------------------------------------------------------------------------------
print("--- Creating Account ---")
acct = BankAccount("Alice", 1000)

# Reading balance using our getter property (looks like a normal attribute!)
print(f"Account Owner: {acct.owner}")
print(f"Initial Balance: ${acct.balance}")

print("\n--- Trying to Modify Balance Directly ---")
# This works and is safe because our setter allows positive numbers
acct.balance = 1200
print(f"Updated Balance: ${acct.balance}")

# This will fail because our setter validates the number!
acct.balance = -500 
print(f"Balance after negative attempt: ${acct.balance}")

print("\n--- Testing Transactions ---")
acct.deposit(300)
acct.withdraw(400, "1234")  # Correct PIN
acct.withdraw(400, "9999")  # Incorrect PIN

print("\n--- Testing Private Variable Access ---")
# Try to access the private __pin directly:
try:
    print(acct.__pin)
except AttributeError as e:
    print(f"AttributeError successfully caught! (Python protected the private variable): {e}")

# Note: Python name-mangles it, so it *is* technically accessible via:
# `acct._BankAccount__pin` but you should NEVER do this in production code!
print(f"Mangled PIN (sneak peek): {acct._BankAccount__pin}")


# ================================================================================
# YOUR TURN: EXERCISE 3
# ================================================================================
# Let's practice encapsulation by building a `Thermostat` class.
#
# INSTRUCTIONS:
# 1. Create a class named `Thermostat`.
# 2. Inside `__init__`, initialize a protected attribute `_temperature` (default to 20).
# 3. Create a getter property `temperature` that returns `_temperature`.
# 4. Create a setter property `temperature` that:
#    - Validates that the new temperature is between 10 and 35 degrees (inclusive).
#    - If it is valid, update `_temperature`.
#    - If it's invalid, print a warning: "Temperature must be between 10°C and 35°C!"
# 5. Create a public method `boost_heating(self)` that increases the temperature by 5 degrees,
#    but still respects the maximum limit of 35 (Hint: use the property setter to change it!).
#
# Un-comment the test code below once you've written your class!
# ================================================================================

# WRITE YOUR Thermostat CLASS HERE:



# --- TEST CODE (Un-comment below to test your implementation) ---
# home_thermostat = Thermostat(22)
# print(f"Current temp: {home_thermostat.temperature}°C")
# 
# home_thermostat.temperature = 28 # Should succeed
# print(f"New temp: {home_thermostat.temperature}°C")
# 
# home_thermostat.temperature = 40 # Should print warning and NOT change temp
# print(f"Temp after invalid set: {home_thermostat.temperature}°C")
# 
# home_thermostat.boost_heating() # Should boost to 33°C
# home_thermostat.boost_heating() # Should print warning (33 + 5 = 38, which is > 35) and not exceed 35
