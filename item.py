import random
class Item(object):
    # Base class for 'Weapon' class and 'Potions' class
    # __init__ takes name, desc - description, item_type and value
    # name - for identifying the item in inventory of the player or just
    #      for naming
    # description - provides description of the item. Not necessary
    #      Provided default value to allow quick creation of normal items
    # item_type defaul is 0. For identifying type of item based on number.
    #           Defaults:
    #           0 - default
    #           1 - Weapons
    #           2 - Consumables #(yep i was gonna type that) potion
    # value - value which will be converted to gold on selling at shop
    #      (Not added yet). Type:int
    def __init__(self, name, desc='No description.', item_type=0, value=1):
        self.name = name
        self.description = desc
        self.item_type = item_type
        self.value = value

    # Displays information of the item when called
    def info(self):
        print('Name: ', self.name)
        print('Desc: ',self.description)
        print('Type: ', self.item_type)
        print('Value: ',self.value)

class Weapon(Item):
    #   takes name, desc, value, dmg_range, sta_cost
    #   use super to assign name, desc, item_type, value to prevent repetitive code
    # dmg_range - tuple containing 2 values - min and max damage of the weapon
    # sta_cost  - 'Stamina Cost'. Type:int
    def __init__(self, name, desc, dmg_range, sta_cost, item_type=0, value=1):
        super(Weapon, self).__init__(name, desc, item_type, value)
        # self.min_dmg = min_dmg
        # self.max_dmg = max_dmg
        self.dmg_range = dmg_range
        self.sta_cost = sta_cost

    def __repr__(self):
        return f'{self.name}'

    def info(self):

        super(Weapon, self).info()
        print('Damage: ', self.dmg_range[0], '-', self.dmg_range[1])
        print('Stamina Cost: ', self.sta_cost)

    def inflictDamage(self, player):
       dmg = random.randint(self.dmg_range[0], self.dmg_range[1])
       player.hp -= dmg

    # For providimg upgrades to weapos in game
    # upgradeWeapon - Take 2 args.
    # new_range is Tuple containing new value for dmg_range
    # new_sta_cost is type:int containing new value for sta_cost
    def upgradeWeapon(self, new_range, new_sta_cost):
        self.dmg_range = new_range
        self.sta_cost = new_sta_cost
