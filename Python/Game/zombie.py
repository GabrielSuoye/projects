from enemy import *
import random


class Zombie(Enemy):
    def __init__(self, health_points, attack_damage):
        super().__init__(
            type_of_enemy="Zombie",
            health_points=health_points,
            attack_damage=attack_damage,
        )

    def talk(self):
        print("Grumbling")

    def spread_disease(self):
        print("The Zombie is trying to spread disease.")

    def special_attack(self):
        chance = random.random() < 0.50
        if chance:
            self.health_points += 2
            print("Zombie has regenerated 2HP!")
