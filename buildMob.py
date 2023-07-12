import random

from core_library import monster_dict as md
from core_library import name_list as nl
from core_library import monster_type_list as mtl
from settings import Settings as s



class Mob:
    """Class that can be called to build random mobs"""



    def __init__(self, name=range(nl), mobtype=range(mtl), hp=range(), arm_c=range(12), spd=range(), xp=range(), lvl=range()):

        self.info = { 'name' : self.name, 'type' : self.mobtype, 'hp' : self.hp, 'arm_c' : self.arm_c, 'spd' : self.spd, 'xp' : self.xp, 'lvl' : self.lvl,}

    


 


   
   