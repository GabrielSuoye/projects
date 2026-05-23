from enemy import *
from zombie import *
from ogre import *
from hero import *
from weapon import *

"""
ogre = Enemy("Ogre", 10, 1)

Ogre.talk()
Ogre.walk_forward()
Ogre.attack()
Ogre.stats()
print(Ogre.get_type_of_enemy())

Ogre_Warboss = Enemy("Ogre_Warboss", 100, 20)

Ogre_Warboss.talk()
Ogre_Warboss.walk_forward()
Ogre_Warboss.attack()
Ogre_Warboss.stats()
print(Ogre_Warboss.get_type_of_enemy())
"""


def battle(e1: Enemy, e2: Enemy):
    e1.talk()
    e2.talk()

    while e1.health_points > 0 and e2.health_points > 0:
        print("------------")
        e1.special_attack()
        e2.special_attack()
        print(f"{e1.get_type_of_enemy()}: {e1.health_points} HP left")
        print(f"{e2.get_type_of_enemy()}: {e2.health_points} HP left")
        e2.attack()
        e1.health_points -= e2.attack_damage
        e1.attack()
        e2.health_points -= e1.attack_damage

        print("------------")

        if e1.health_points > 0:
            print(f"{e1.get_type_of_enemy()} wins")
        else:
            print(f"{e2.get_type_of_enemy()} wins")


def hero_battle(hero: Hero, enemy: Enemy):
    enemy.talk()

    while hero.health_points > 0 and enemy.health_points > 0:
        print("------------")
        enemy.special_attack()

        print(f"Hero: {hero.health_points} HP left")
        print(f"{enemy.get_type_of_enemy()}: {enemy.health_points} HP left")
        enemy.attack()
        hero.health_points -= enemy.attack_damage
        hero.attack()
        enemy.health_points -= hero.attack_damage

        print("------------")

        if hero.health_points > 0:
            print("Hero wins")
        else:
            print(f"{enemy.get_type_of_enemy()} wins")


zombie = Zombie(10, 1)
ogre = Ogre(20, 5)
hero = Hero(10, 1)
weapon = Weapon("Sword", 5)
hero.weapon = weapon
hero.equip_weapon()

# battle(zombie, ogre)

# hero_battle(hero, zombie)

hero_battle(hero, ogre)
