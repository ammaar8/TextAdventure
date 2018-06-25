from random import randint
# Satmina chantged to sp (Stamin Points)
class Character(object):

    # __repr__ should return str type.
    # def __repr__(self):
    #     name = self.name
    #     return name

    def setInfo(self, name, type, hp):
        self.name = name
        self.type = type
        self.hp = hp

    def isAlive(self):
        if self.type == 1:
            if self.hp > 0:
                #print("You're still Alive")
                return 1
            else:
                print("You is dead. You didn't play well, huh")
                return 0

        elif self.type == 2:
            if self.hp > 0:
                return 1
            else:
                print(f"You defeated {self.name}")
                del(self)
                return 0

    # Is this attack type needed? We'll create a combat function where the
    # player can choose what weapon to use

    #def attack(self, enemy):

    #    if self.type == 1:
    #        print("Select your weapon to attack!\n")

            #for weapons in self.inventory:
            #    print (weapons)

            # print("\n\nWhat do you wanna use?")
            # weapon = input().capitalize()
            # print(weapon)
        #elif self.type == 2:

            #for weapons in self.inventory:
                #print (weapons)
                #print("Enemy's weapon choice", weapon )
        #else:
            #return

class Player(Character):
    """docstring for Player."""

    #inventory = {'Sword': (10,20), 'Gun': (15,30)}

    def setInfo(self):
        inp = input("You-Know-Who needs your name. \n\n>>")
        super(Player, self).setInfo(inp, 1, 100)
        self.sp = 100
        self.inventory = {}


    def info(self):
        print(f"{self.name} hp: {self.hp} sta: {self.sp}")

    # Is this function needed? The player has a default inventory
    #def makeInventory(self):
    #    self.inventory = {}

    # Creates a key, value pair for objects added to inventory
    def addToInventory(self, obj):
        self.inventory[f'{obj.name}'] = obj


    def displayInventory(self):
        print(self.inventory)

    # On using weapon, the sp of player is reduced and the damage value is
    # returned which will be used as damage done to enemy
    # If the player does not have enough stamina then 0 damage will be
    # done to enemy

    def useWeapon(self, weapon):
        if weapon in self.inventory.keys():
            weapon_obj = self.inventory[weapon]
            if self.sp > weapon_obj.sp_cost:
                self.sp -= weapon_obj.sp_cost
                return randint(*weapon_obj.dmg_range)
            else:
                print('Not enough sp')
                return 0
        else:
            print(f'{weapon} not in inventory')

class Enemy(Character):

    #inventory = {'Sword': (5,15), 'Gun': (10,25)}
    def setInfo(self, name, hp, weapon):
        super(Enemy, self).setInfo(name, 2, hp)
        self.sp = 100
        self.weapon = weapon

    def info(self):
        print(f"{self.name} hp: {self.hp}")

    def attack(self, target):
        target.hp -= randint(*self.weapon.dmg_range)

"""player = Player()
player2 = Player()
player2.makeInventory()
player2.addToInventory({'Sword':(10, 20)})
enemy = Enemy()
player.setInfo()
player.info()
player.isAlive()
player.attack(player)
enemy.setInfo()
enemy.isAlive()
enemy.display()
enemy.attack(enemy)
player.makeInventory()
player.addToInventory({'Gun' : (20,30)})
player.displayInventory()
"""
spider = Enemy()
"""print('enter anything >> ')
i = input().capitalize()
print(i)"""
