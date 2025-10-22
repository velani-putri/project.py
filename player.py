import random

class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.hp = 100
        self.max_hp = 100
        self.attack = 10
        self.exp = 0
        self.gold = 0
        self.inventory = []

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, dmg):
        self.hp = max(0, self.hp - dmg)

    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)

    def gain_exp(self, amount):
        self.exp += amount
        print(f"{self.name} mendapatkan {amount} EXP!")
        if self.exp >= self.level * 50:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.max_hp += 20
        self.attack += 5
        self.hp = self.max_hp
        self.exp = 0
        print(f"\n🎉 {self.name} naik ke level {self.level}!")
        print(f"HP meningkat menjadi {self.max_hp}, Attack menjadi {self.attack}\n")
