from enemy import *

Ogre = Enemy("Ogre", 10, 1)

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
