# Dijjon Mob Class
# Developed & designed by: Zane M Deso
# Purpose: This class is in charge of building and tearing down Mobs as needed for encounters, battle, filling dungeons, etc.
# EDIT: Refactoring to be child to Entity class.

import random as r

from core_library import monster_dict as md
from core_library import name_list as nl
from core_library import monster_type_list as mtl
from settings import Settings as s
from Entity import Entity


class Mob(Entity):
    """Mob Class handles Mob instances and random generation"""

    # if no arguement is given, the mob will have the default randomized name, mob, mob type, etc.
    def __init__(self, name=None, mob=None, hp=None, arm_c=None, spd=30, xp=None, lvl=None, is_enemy=True):
        super().__init__(name, hp, arm_c, spd, xp, lvl, is_enemy)

        # instastiate the variables so we can pass them to the self.info dictionary below
        # also we must use the __init__ method to choose each new isntances variables uniquely
        # as the class arguments are only checked once when the class itself if initialized
        self.name = name if name is not None else r.choice(nl)
        self.mob = mob if mob is not None else r.choice(list(md.keys()))
        self.hp = hp if hp is not None else r.randint(10, 30)
        self.arm_c = arm_c if arm_c is not None else r.randint(10, 15) 
        self.spd = spd
        self.xp = xp if xp is not None else r.randint(10, 30)
        self.lvl = lvl if lvl is not None else r.randint(1, 3)
        self.mobtype = md[f'{self.mob}']  # mob type based of mob selected
        self.max_hp = self.hp  # set max health (maybe make this a tuple? not sure if I need to)
        self.is_enemy = is_enemy  # Default to enemy
        
        # FIX ME: Mob Class requires accessors and mutators.

    def get_hp(self):
        return super().get_hp()
    
    def get_name(self):
        return super().get_name()
    
    def set_hp(self, hp):
        return super().set_hp(hp)
    
    def set_name(self, name):
        return super().set_name(name)


# test instances of Mob class

# yuan_ti = Mob(mob='Yuan-ti', hp=60, arm_c=25)

# print(f'{yuan_ti.name, yuan_ti.info}')

# new_mob1 = Mob()

# print(new_mob1.info)

# new_mob2 = Mob()

# print(new_mob2.info)

# tests what the default output for name choice would be
# print(r.choice(nl))

# tests what the default output for mob choice would be
# test_mob = r.choice(list(md.keys()))
# print(test_mob)

# tests what the default output for mobtype choice should be
# mobtype = md[f'{test_mob}']
# print(f'{test_mob} | Monster Type: {mobtype.title()}')

   
   