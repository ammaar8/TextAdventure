from Character import *
from item import *

player = Player()
player.setInfo()

#name, desc, item_type=0, value=1, dmg_range, sta_cost
claws = Weapon('claws', 'Made with Goblin Iron', (10,20), 2, 1, 2)
spidy = Enemy()
spidy.setInfo('Spidy', 70, claws)
player.addToInventory(claws)
player.info()
spidy.info()

while(player.isAlive() and spidy.isAlive()):

    print('\n\n')
    spidy.hp -= player.useWeapon('claws')
    spidy.attack(player)

    player.info()
    spidy.info()


# Info class is showing too much info
# Can't use in combat
# Check the combat options
