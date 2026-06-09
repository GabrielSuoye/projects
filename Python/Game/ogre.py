from enemy import *
import random

class Ogre(Enemy):
    def __init__(self, health_points, attack_damage):
        super().__init__(
            type_of_enemy="Ogre",
            health_points=health_points,
            attack_damage=attack_damage,
        )

    def behavoir(self):
        print("Ogre is slamming hands all around.")

    def talk(self):
        print("WAAAAAAARGH!!!")

    def special_attack(self):
        chance = random.random() < 0.20
        if chance:
            self.attack_damage += 5
            print("Ogre's attack damage has increased by 5!")
