import random

class Enemy:
    #Variables
    kind = "Humans"
    name = "Bill"
    weapons = ["Gun", "Melee", "Granade"]

    def __init__(self, name):
        self.name = name
        self.weapons = random.choice(Enemy.weapons)


    def attack(self):
        print("Then enemy attacks")

    def set_attack_mode(self):
        self.__mode = "medium"

    def get_attack_mode(self):
        print(self.__mode)

    def set_description(self):
        self.__des= "This isn't just any ordinary man"

    def get_description(self):
        print(self.__des)

enemy1 = Enemy("Bill")
enemy2 = Enemy("Bob")
enemy1.attack()

print('\n')
print(enemy1.name)
print(enemy1.kind)
print(enemy1.weapons)
enemy1.set_description()
enemy1.get_description()
enemy1.set_attack_mode()
enemy1.get_attack_mode()
print('\n')
print(enemy2.name)
print(enemy2.kind)
print(enemy2.weapons)
enemy2.set_description()
enemy2.get_description()
enemy2.set_attack_mode()
enemy2.get_attack_mode()
print('\n')

print(enemy1.name + " Blah Blah Blah" + enemy2.name + " Blah Blah Blah")
