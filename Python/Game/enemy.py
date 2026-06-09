import random


class Enemy:
    """
    type_of_enemy: str = "Ogre"
    health_points: int = 10
    attack_damage: int = 1
    """

    def __init__(self, type_of_enemy, health_points, attack_damage):
        self.__type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage

    def talk(self):
        print(f"I am an {self.__type_of_enemy} ...WAAAAAAARGH!!!")

    def walk_forward(self):
        print(f"{self.__type_of_enemy} moves closer to you.")

    def attack(self):
        print(f"{self.__type_of_enemy} attacks for {self.attack_damage} damage.")

    def stats(self):
        print(
            f"{self.__type_of_enemy} has {self.health_points} health and {self.attack_damage} attack."
        )

    def get_type_of_enemy(self):
        return self.__type_of_enemy

    def special_attack(self):
        return None


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
