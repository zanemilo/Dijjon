# Dijjon Player Class
# Developed & designed by: Zane M Deso
# Purpose: Used to handle player creation, stats, attributes, status effect, and other associated player centered functions



import random as r
from ...master import Master as m
from ...scripts.game_mechanics import Item as i
from ...scripts.game_mechanics import dice_Roll as dr
from scripts.environment.Visibility import Visibility
from scripts.entity.Entity import Entity  # using 'from Entity' due to probable cause of being mistaken as a module.
from ...resources import core_library as cl


class Player(Entity):
    """Player Class to generate User's character instance as well as NPC instances."""

    def __init__(self, name, race, char_class, gold = 10, arm_c = 10, spd = 30, xp = 0, lvl = 1, str = 0, dex = 0, con = 0, intel = 0, wis = 0, cha = 0,  hp = 6, hpMax = 6, is_enemy = False, visibility_conditions=None, special_senses=[], **kwargs):
        super().__init__(name, hp, arm_c, spd, xp, lvl, is_enemy)
        self.name = name
        self.race = race
        self.char_class = char_class
        self.gold = gold
        self.arm_c = arm_c
        self.spd = spd
        self.xp = xp
        self.lvl = lvl
        self.str = str + dr.roll_stats() + r.randint(-1, 2)
        self.dex = dex + dr.roll_stats() + r.randint(-1, 2)
        self.con = con + dr.roll_stats() + r.randint(-1, 2)
        self.intel = intel + dr.roll_stats() + r.randint(-1, 2)
        self.wis = wis + dr.roll_stats() + r.randint(-1, 2)
        self.cha = cha + dr.roll_stats() + r.randint(-1, 2)
        self.hp = hp + self.get_modifier(self.con)
        self.hpMax = hpMax + self.get_modifier(self.con)
        self.is_enemy = is_enemy
        self.special_senses = special_senses
        self.visibility_conditions = visibility_conditions
        self.visibility = Visibility(special_senses=special_senses)
        self.inventory = {}
        self.equipment_slots = {
            'head': None,
            'chest': None,
            'feet': None,
            'weapon': None,
            'shield': None,
            # Add more equipment slots as needed
        }
        # FIX ME: Add all player attributes here

    # FIX ME: Add/create player associated methods here

    def weather_effect(self, weather, intensity):
        """Apply effects based on the weather condition and its intensity using a dictionary with lambda functions."""
        effects = {
            'rain': lambda i: (setattr(self, 'spd', self.spd - i * 5),
                               setattr(self, 'hp', self.hp - 5) if i == 3 else None),

            'rain_storm': lambda i: (setattr(self, 'spd', self.spd - i * 10),
                                     setattr(self, 'hp', self.hp - 10) if i == 3 else None),

            'lightning': lambda i: setattr(self, 'hp', self.hp - 20) if i == 3 else None,

            'fog': lambda i: self.visibility.update_visibility({'fog': True}),

            'blizzard': lambda i: (setattr(self, 'spd', self.spd - i * 7),
                                   setattr(self, 'hp', self.hp - i * 5)),

            'sandstorm': lambda i: self.visibility.update_visibility({'sandstorm': True}),

            'hurricane': lambda i: (setattr(self, 'spd', self.spd - i * 15),
                                    setattr(self, 'hp', self.hp - i * 15)),

            'heatwave': lambda i: setattr(self, 'hp', self.hp - i * 5),

            'cold_snap': lambda i: setattr(self, 'hp', self.hp - i * 5),

            'dust_devil': lambda i: self.visibility.update_visibility({'dust_devil': True}),

            'hailstorm': lambda i: setattr(self, 'hp', self.hp - i * 10),

            'sleet': lambda i: (setattr(self, 'spd', self.spd - i * 8),
                                self.visibility.update_visibility({'sleet': True})),

            'tornado': lambda i: setattr(self, 'hp', self.hp - i * 30)
        }

        # Call the corresponding effect function if the weather condition is found
        effect_func = effects.get(weather)
        if effect_func:
            effect_func(intensity)
            self.display_updated_status()

    def display_updated_status(self):
        """Display the updated player status."""
        print(f"Updated Player Status - HP: {self.hp}, Speed: {self.spd}, Visibility: {self.visibility.check_visibility()}")

    def apply_environment_effect(self, condition):
        self.visibility.update_visibility(condition)
        print(f"{self.name}'s current visibility: {self.visibility.check_visibility()}")

    def equip_item(self, item):
        """Equip an item to the appropriate equipment slot"""
        # Check if the item is equippable
        if item.slot not in self.equipment_slots:
            print(f"{item.name} is not equippable.")
            return
        # Check if the slot is already occupied
        if self.equipment_slots[item.slot] is not None:
            print(f"{self.name} already has an item equipped in the {item.slot} slot.")
            return
        # Equip the item
        self.equipment_slots[item.slot] = item
        print(f"{self.name} equipped {item.name}.")

    def unequip_item(self, slot):
        """Unequip an item from the specified slot"""
        if slot not in self.equipment_slots:
            print(f"Invalid equipment slot: {slot}.")
            return
        if self.equipment_slots[slot] is None:
            print(f"No item equipped in {slot} slot.")
            return
        # Unequip the item
        unequipped_item = self.equipment_slots[slot]
        self.equipment_slots[slot] = None
        print(f"{self.name} unequipped {unequipped_item.name} from {slot}.")

    def display_equipment(self):
        """Display the items currently equipped"""
        print("Equipment:")
        for slot, item in self.equipment_slots.items():
            if item:
                print(f"{slot}: {item.name}")
            else:
                print(f"{slot}: Empty")

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

    def get_intel(self):
        return self.intel
    
    def set_intel(self, intel):
        self.intel = intel

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
        self.inventory.update({str(item.name) : str(amount)})
        print(f"{self.name} recieved {amount} {item.name}!\n")
    
    def give_item(self, action, amount, item):
        """method for user character giving away, selling, dropping, donating an item"""
        if item not in self.inventory:
            print('You do not have enough', item.name, f'to {action}!\n')
        elif self.inventory[str(item.name)] < amount or self.inventory[str(item.name)] <= 0:
            print('You do not have enough', item.name, f'to {action}!\n')
        else:
            self.inventory[str(item.name)] -= amount #this should fix the bug of keeping item in inv but removes all not some 
            print(f"{self.name} {action} {amount} {item}\n")

    def show_inventory(self):
        """Displays player's inventory contents"""
        num = 1
        for item in self.inventory:
            print(f'{num}. {item} - {self.inventory[item]}') # item would be the name (key), self.inventory[item] would be the corresponding value
            num += 1

    def get_modifier(self, stat):
        return (stat - 10) //2
    
    def get_stat(self, stat):
        """Takes stat as an args and returns instances stats value"""
        
        stat = stat.lower()
        valid_types = ['str','dex', 'con', 'intel', 'wis', 'cha']

        if stat in valid_types:
            if stat == 'str':
                return self.get_str()
            elif stat == 'dex':
                return self.get_dex()
            elif stat == 'con':
                return self.get_con()
            elif stat == 'intel':
                return self.get_intel()
            elif stat == 'wis':
                return self.get_wis()
            elif stat == 'cha':
                return self.get_cha()
            else:
                print(f'Error: An unexpected error occured while attempting to find stat args matching stat for instance\nstat: {stat}')
        
    def get_skill_stat(self, skill):
        """Takes skill as an args and returns instances stats value"""
        
        stat_mapping = {
            'acrobatics': self.get_dex(),  # Dexterity for Acrobatics
            'animal_handling': self.get_wis(),  # Wisdom for Animal Handling
            'arcana': self.get_intel(),  # Intelligence for Arcana
            'athletics': self.get_str(),  # Strength for Athletics
            'deception': self.get_cha(),  # Charisma for Deception
            'history': self.get_intel(),  # Intelligence for History
            'insight': self.get_wis(),  # Wisdom for Insight
            'intimidation': self.get_cha(),  # Charisma for Intimidation
            'investigation': self.get_intel(),  # Intelligence for Investigation
            'medicine': self.get_wis(),  # Wisdom for Medicine
            'nature': self.get_intel(),  # Intelligence for Nature
            'perception': self.get_wis(),  # Wisdom for Perception
            'performance': self.get_cha(),  # Charisma for Performance
            'persuasion': self.get_cha(),  # Charisma for Persuasion
            'religion': self.get_intel(),  # Intelligence for Religion
            'sleight_of_hand': self.get_dex(),  # Dexterity for Sleight of Hand
            'stealth': self.get_dex(),  # Dexterity for Stealth
            'survival': self.get_wis(),  # Wisdom for Survival
        }

        # Convert skill to lowercase for case-insensitive comparison
        skill = skill.lower()

        if skill in stat_mapping:
            # Call the corresponding method based on the skill
            return stat_mapping[skill]
        else:
            print(f'Error: Skill "{skill}" not found in the mapping.')

    def display_info(self):
        """Display player's info"""
        print(f"Name: {self.get_name()}\nRace: {self.get_race()}\nCharacter class: {self.get_char_class()}\nGold: {self.get_gold()}\nArmor Class: {self.get_arm_c()}\nHP: {self.get_hp()}\nMax HP: {self.get_hpMax()}\nSpeed: {self.get_spd()}\nXP: {self.get_xp()}\nLevel: {self.get_lvl()}\nStr: {self.get_str()}\nDex: {self.get_dex()}\nCon: {self.get_con()}\nInt: {self.get_intel()}\nWis: {self.get_wis()}\nCha: {self.get_cha()}\n")

    def check_roll(self, check_type):
        """Takes stat as an args and rolls a d20 + the instances stat associated modifier. -> int of sum of entity roll"""

        check_type = check_type.lower()
        valid_types = [
        'acrobatics', 'animal_handling', 'arcana', 'athletics', 'deception', 
        'history', 'insight', 'intimidation', 'investigation', 'medicine', 
        'nature', 'perception', 'performance', 'persuasion', 'religion', 'sleight_of_hand', 
        'stealth', 'survival', 'str','dex', 'con', 'intel', 'wis', 'cha']

        sum_of_player_roll = 0

        if check_type in valid_types[:valid_types.index('survival')+1]:
            sum_of_player_roll = dr.roll_d20() + self.get_modifier(self.get_skill_stat(check_type))
        elif check_type in valid_types:
            sum_of_player_roll = dr.roll_d20() + self.get_modifier(self.get_stat(check_type))
        
        return int(sum_of_player_roll)



# Test Randomness into Player creation, can be used to build NPCs
random_name_num = r.randint(0, len(cl.name_list) - 1)
random_name = cl.name_list[random_name_num]

random_race_num = r.randint(0, len(cl.races) - 1)
random_race = cl.races[random_race_num]

random_class_num = r.randint(0, len(cl.classes) - 1)
random_class = cl.classes[random_class_num]

# print(f"{random_name} {random_race} {random_class}")

# Test instatiate testPlayer Player object
testPlayer = Player(random_name, random_race, random_class)

testPlayer.get_item(1, i.Item("Coins","Shiny gold coins", 1))
testPlayer.inventory.update({"Apple" : "Turds"})
testPlayer.show_inventory()


