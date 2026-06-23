#!/usr/bin/env python3
"""
================================================================================
LESSON 2: INHERITANCE AND POLYMORPHISM — REUSABILITY AND FLEXIBILITY
================================================================================

Now that you understand how to build individual classes, let's explore how to
connect them to avoid repeating code. This is where two pillars of OOP come in:
Inheritance and Polymorphism.

--------------------------------------------------------------------------------
1. INHERITANCE
--------------------------------------------------------------------------------
Inheritance allows us to create a new class (Subclass or Child class) that inherits
attributes and methods from an existing class (Superclass or Parent class).
This follows the DRY principle: "Don't Repeat Yourself."

Analogy:
- Parent: A general "Animal" class.
- Child: A "Dog" class. A dog *is an* animal, so it inherits all animal behaviors 
  (eating, sleeping) but can add its own specific behaviors (barking).

--------------------------------------------------------------------------------
2. POLYMORPHISM
--------------------------------------------------------------------------------
Polymorphism literally means "many forms." In programming, it refers to the 
ability of different classes to respond to the same method call in their own 
unique way.

Analogy:
- If you tell a Dog to "speak", it barks.
- If you tell a Cat to "speak", it meows.
- They both have a `speak()` method, but the action they take is different.

--------------------------------------------------------------------------------
3. THE GAME CHARACTER HIERARCHY EXAMPLE
--------------------------------------------------------------------------------
Let's build a RPG game character system to see these concepts in action!
"""

# --- THE PARENT CLASS (Superclass) ---
class Character:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def take_damage(self, amount):
        self.health -= amount
        print(f"💥 {self.name} takes {amount} damage! Health: {self.health}")
        if self.health <= 0:
            print(f"💀 {self.name} has been defeated!")

    def attack(self):
        # A generic attack that subclasses will customize (override)
        print(f"⚔️ {self.name} performs a basic attack!")


# --- SUBCLASS 1: WARRIOR (Inherits from Character) ---
class Warrior(Character):
    def __init__(self, name, health=120, shield=20):
        # Use super() to call the parent class's constructor __init__.
        # This initializes 'name' and 'health' using the Parent's logic.
        super().__init__(name, health)
        
        # Now we initialize the Warrior-specific attribute
        self.shield = shield

    # METHOD OVERRIDING: Customizing a parent method.
    # Warriors have a shield, so they should take less damage!
    def take_damage(self, amount):
        if self.shield > 0:
            blocked = min(self.shield, amount // 2) # Block up to half the damage
            self.shield -= blocked
            actual_damage = amount - blocked
            print(f"🛡️ Warrior {self.name}'s shield blocks {blocked} damage!")
        else:
            actual_damage = amount

        # Call the parent class's take_damage method to handle the actual health deduction
        super().take_damage(actual_damage)

    # Overriding the attack method
    def attack(self):
        print(f"🪓 Warrior {self.name} swings a mighty battle-axe!")


# --- SUBCLASS 2: MAGE (Inherits from Character) ---
class Mage(Character):
    def __init__(self, name, health=80, mana=50):
        super().__init__(name, health)
        self.mana = mana

    # Overriding the attack method
    def attack(self):
        if self.mana >= 15:
            self.mana -= 15
            print(f"🔥 Mage {self.name} casts a Fireball! (Mana remaining: {self.mana})")
        else:
            # If out of mana, fall back to the generic attack from the parent class!
            print(f"✨ Mage {self.name} is out of mana...")
            super().attack()


# ------------------------------------------------------------------------------
# 4. POLYMORPHISM IN ACTION
# ------------------------------------------------------------------------------
print("--- Creating Characters ---")
grog = Warrior("Grog the Bold")
elara = Mage("Elara the Wise")

print("\n--- Individual Combat behaviors ---")
grog.attack()
elara.attack()

print("\n--- Taking Damage (Overridden Methods) ---")
# Warrior uses their shield to block damage
grog.take_damage(30)
# Mage takes full damage (no shield override)
elara.take_damage(30)

print("\n--- Demonstrating Polymorphism ---")
# We can treat different character classes uniformly!
party = [grog, elara, Character("NPC Villager")]

# A single loop can execute different behaviors because all objects share
# the same method name: `attack`
def start_battle_round(team):
    print("⚔️ Round starts! Everyone attack!")
    for member in team:
        member.attack() # Each member attacks in their own unique way!

start_battle_round(party)


# ================================================================================
# YOUR TURN: EXERCISE 2
# ================================================================================
# Let's expand our RPG game by creating a new character class and testing
# inheritance and polymorphism!
#
# INSTRUCTIONS:
# 1. Create a subclass named `Rogue` that inherits from `Character`.
# 2. Add a subclass-specific attribute:
#    - `critical_chance` (float, representing percentage chance, e.g., 0.30 for 30%)
# 3. Use `super().__init__()` to initialize `name` and `health` (default health: 90).
# 4. Override the `attack` method:
#    - Generate a random check. (Hint: you can use Python's built-in `random` module, 
#      or just simulate it. I've imported `random` for you below).
#    - If it's a critical hit, print "🗡️ Rogue [name] performs a Backstab! CRITICAL HIT!"
#    - Otherwise, print "🗡️ Rogue [name] strikes from the shadows!"
#
# Un-comment the test code below once you've written your class!
# ================================================================================

import random

# WRITE YOUR Rogue CLASS HERE:



# --- TEST CODE (Un-comment below to test your implementation) ---
# rogue = Rogue("Jesper", critical_chance=0.5) # 50% crit chance
# rogue.take_damage(25)
# 
# print("\n--- Testing Polymorphism with Rogue ---")
# party.append(rogue)
# start_battle_round(party) # Jesper should now attack in his own unique rogue way!
