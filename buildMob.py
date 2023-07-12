import random as r

from core_library import monster_dict as md
from core_library import name_list as nl
from core_library import monster_type_list as mtl
from settings import Settings as s



class Mob:
    """Class that can be called to build random mobs"""



    def __init__(self, name=r.choice(nl), mob=r.choice(list(md.keys())), hp=r.randint(10,30), arm_c=r.randint(10,30), spd=30, xp=r.randint(10,30), lvl=r.randint(10,30)):
        
    
        # if mob argument is input (always should since it will a randomized default value), 
        # mobtype will be pulled from corresponding monster_dict of mob
        if mob:
            self.mobtype = md[f'{mob}']

        self.info = { 
            'name' : self.name, 
            'mob' : self.mob,
            'type' : self.mobtype, 
            'hp' : self.hp, 
            'arm_c' : self.arm_c, 
            'spd' : self.spd, 
            'xp' : self.xp, 
            'lvl' : self.lvl,
            }

    


 # test instance of Mob class

# tests what the default output for name choice would be
# print(r.choice(nl))

# tests what the default output for mob choice would be
# test_mob = r.choice(list(md.keys()))
# print(test_mob)

# tests what the default output for mobtype choice should be
# mobtype = md[f'{test_mob}']
# print(f'{test_mob} | Monster Type: {mobtype.title()}')

   
   