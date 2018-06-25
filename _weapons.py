from item import Weapon

# Format : name, desc, dmg_range, sp_cost, type=1, value
wood_sword = Weapon('Wooden_sword',
                    "A sword made of wood for training",
                    (2,5), sp_cost=5, value=10)

iron_sword = Weapon('Iron_sword',
                    """A sword made of iron. Can cut through flesh so don't swing
                    it around like a wooden sword""",
                    (5,10), sp_cost=10, value=50)

steel_sword = Weapon('Steel_sword',
                     """A sword made of iron mixed with other stuff. Will cut through
                     your iron sword""",
                     (10,15), sp_cost=10, value=100)

iron_dagger = Weapon('Iron_dagger',
                     """Dagger to hide in you cloak and be sneaky.
                     Just like a thief. Cloak and Dagger.""",
                     (3,7), sp_cost=6, value=30)

steel_dagger = Weapon('Steel_dagger',
                      """Steel dagger for quick silent assassinations.""",
                      (8,12), sp_cost=6, value=80)

steel_mace = Weapon('Steel_mace',
                    """A mace to crack open your enemie's head.""",
                    (13,18), sp_cost=8, value=80)
