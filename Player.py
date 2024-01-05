
class Player:
    """Main Player Class with Mutators, Accessors, Attributes and other variable"""

    def __init__(self, name, race, char_class, gold = 10, arm_c = 10, hp = 6, hpMax = 6, spd = 30, xp = 0, lvl = 1):
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
            #player.inventory[item] -= amount 
            print(f"{self.name} {action} {amount} {item}\n")

    def show_inventory(self):
        """Displays player's inventory contents"""
        num = 1
        for item in self.inventory:
            print(f'{num}. {item} - {self.inventory[item]}') # item would be the name (key), self.inventory[item] would be the corresponding value
            num += 1