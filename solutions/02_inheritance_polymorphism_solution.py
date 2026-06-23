#!/usr/bin/env python3
"""
================================================================================
LESSON 2: INHERITANCE AND POLYMORPHISM — SOLUTION
================================================================================
"""
import random

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
        print(f"⚔️ {self.name} performs a basic attack!")


class Warrior(Character):
    def __init__(self, name, health=120, shield=20):
        super().__init__(name, health)
        self.shield = shield

    def take_damage(self, amount):
        if self.shield > 0:
            blocked = min(self.shield, amount // 2)
            self.shield -= blocked
            actual_damage = amount - blocked
            print(f"🛡️ Warrior {self.name}'s shield blocks {blocked} damage!")
        else:
            actual_damage = amount

        super().take_damage(actual_damage)

    def attack(self):
        print(f"🪓 Warrior {self.name} swings a mighty battle-axe!")


class Mage(Character):
    def __init__(self, name, health=80, mana=50):
        super().__init__(name, health)
        self.mana = mana

    def attack(self):
        if self.mana >= 15:
            self.mana -= 15
            print(f"🔥 Mage {self.name} casts a Fireball! (Mana remaining: {self.mana})")
        else:
            print(f"✨ Mage {self.name} is out of mana...")
            super().attack()


# --- SOLUTION CLASS ---
class Rogue(Character):
    def __init__(self, name, health=90, critical_chance=0.30):
        super().__init__(name, health)
        self.critical_chance = critical_chance

    def attack(self):
        # We generate a random float between 0.0 and 1.0.
        # If it's less than critical_chance, it's a critical hit!
        if random.random() < self.critical_chance:
            print(f"🗡️ Rogue {self.name} performs a Backstab! 💥 CRITICAL HIT!")
        else:
            print(f"🗡️ Rogue {self.name} strikes from the shadows!")


# --- TEST CODE ---
print("--- Running Character System Tests ---")
grog = Warrior("Grog the Bold")
elara = Mage("Elara the Wise")
rogue = Rogue("Jesper", critical_chance=0.5)

party = [grog, elara, Character("NPC Villager"), rogue]

def start_battle_round(team):
    print("\n⚔️ Round starts! Everyone attack!")
    for member in team:
        member.attack()

start_battle_round(party)
