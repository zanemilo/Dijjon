# Dijjon Player Class
# Developed & designed by: Zane M Deso
# Purpose: Used to handle player creation, stats, attributes, status effect, and other associated player centered functions


import core_library as cl
import random as r
import dice_Roll as dr
import master as m


class Player:
    """Main Player Class with Mutators, Accessors, Attributes and other variables"""

    def __init__(self, name, race, char_class, gold = 10, arm_c = 10, hp = 6, hpMax = 6, spd = 30, xp = 0, lvl = 1, str = dr.roll_stats(), dex = dr.roll_stats(), con = dr.roll_stats(), int = dr.roll_stats(), wis = dr.roll_stats(), cha = dr.roll_stats()):
        self.name = name
        self.race = race
        self.char_class = char_class
        self.gold = gold
        self.arm_c = arm_c
        self.hp = hp
        self.hpMax = hpMax
        self.spd = spd
        self.xp = xp
        self.lvl = lvl
        self.str = str
        self.dex = dex
        self.con = con
        self.int = int
        self.wis = wis
        self.cha = cha
        self.inventory = {}
        # FIX ME: Add all player attributes here

    # FIX ME: Add/create player associated methods here 
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_race(self):
        return self.race
    
    def set_race(self, race):
        self.race = race

    def get_char_class(self):
        return self.char_class
    
    def set_char_class(self, char_class):
        self.char_class = char_class

    def get_gold(self):
        return self.gold
    
    def set_gold(self, gold):
        self.gold = gold

    def get_arm_c(self):
        return self.arm_c
    
    def set_arm_c(self, arm_c):
        self.arm_c = arm_c

    def get_hp(self):
        return self.hp
    
    def set_hp(self, hp):
        self.hp = hp

    def get_hpMax(self):
        return self.hpMax
    
    def set_hpMax(self, hpMax):
        self.hpMax = hpMax

    def get_spd(self):
        return self.spd
    
    def set_spd(self, spd):
        self.spd = spd

    def get_xp(self):
        return self.xp
    
    def set_xp(self, xp):
        self.xp = xp

    def get_lvl(self):
        return self.lvl

    def set_lvl(self, lvl):
        self.lvl = lvl

    def get_int(self):
        return self.int
    
    def set_int(self, int):
        self.int = int

    def get_wis(self):
        return self.wis
    
    def set_wis(self, wis):
        self.wis = wis
    
    def get_cha(self):
        return self.cha
    
    def set_cha(self, cha):
        self.cha = cha

    def get_str(self):
        return self.str
    
    def set_str(self, str):
        self.str = str

    def get_dex(self):
        return self.dex
    
    def set_dex(self, dex):
        self.dex = dex

    def get_con(self):
        return self.con
    
    def set_con(self, con):
        self.con = con
        
    def get_item(self, amount, item):
        """add, append the item and amount into the self.inventory"""
        self.inventory[item] = amount
        print(f"{self.name} recieved {amount} {item}!\n")
    
    def give_item(self, action, amount, item):
        """method for user character giving away, selling, dropping, donating an item"""
        if item not in self.inventory:
            print('You do not have enough', item, f'to {action}!\n')
        elif self.inventory[item] < amount or self.inventory[item] == 0:
            print('You do not have enough', item, f'to {action}!\n')
        else:
            self.inventory.pop(item) #this should fix the bug of keeping item in inv but removes all not some 
            print(f"{self.name} {action} {amount} {item}\n")

    def show_inventory(self):
        """Displays player's inventory contents"""
        num = 1
        for item in self.inventory:
            print(f'{num}. {item} - {self.inventory[item]}') # item would be the name (key), self.inventory[item] would be the corresponding value
            num += 1

    def get_modifier(self, stat):
        return (int((stat - 10)/2))
    
    def display_info(self):
        """Display player's info"""
        print(f"Name: {self.get_name()}\nRace: {self.get_race()}\nCharacter class: {self.get_char_class()}\nGold: {self.get_gold()}\nArmor Class: {self.get_arm_c()}\nHP: {self.get_hp()}\nMax HP: {self.get_hpMax()}\nSpeed: {self.get_spd()}\nXP: {self.get_xp()}\nLevel: {self.get_lvl()}\nStr: {self.get_str()}\nDex: {self.get_dex()}\nCon: {self.get_con()}\nInt: {self.get_int()}\nWis: {self.get_wis()}\nCha: {self.get_cha()}\n")

    


# # Test Randomness into Player creation, can be used to build NPCs
# random_name_num = r.randint(0, len(cl.name_list) - 1)
# random_name = cl.name_list[random_name_num]

# random_race_num = r.randint(0, len(cl.races) - 1)
# random_race = cl.races[random_race_num]

# random_class_num = r.randint(0, len(cl.classes) - 1)
# random_class = cl.classes[random_class_num]

# print(f"{random_name_num} {random_race_num} {random_class_num}")

# # Test instatiate testPlayer Player object
# testPlayer = Player(random_name, random_race, random_class)

# testPlayer.display_info()


