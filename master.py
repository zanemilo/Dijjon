# Dijjon master Class
# Developed & designed by: Zane M Deso
# Purpose: This class is the main driver and will be the DM in a sense when it comes to making choices behind the scenes.

import Player as p
import settings
import random as r
from core_library import races
from core_library import classes

class Master:
    """Class for actions or deciscions a DM would typically make in the overarching gameplay, story etc."""

    def sheet(self, character):  # passed testing in new main
        """Generate and display the character sheet"""
    
        #dictionary of character instance's stats used for sheet to pull updated info
        stats = {
        "STR": character.str,
        "DEX": character.dex,
        "CON": character.con,
        "INT": character.int,
        "WIS": character.wis,
        "CHA": character.cha,
        "HP": character.hp,
        "AC": character.arm_c,
        "GP": character.gold,
        "SPD": character.spd,
        "LEVEL": character.lvl,
        "XP" : character.xp,
        }

        # This may be redundant, will need to test
        stats["STR"] = character.str
        stats["DEX"] = character.dex
        stats["CON"] = character.con
        stats["INT"] = character.int
        stats["WIS"] = character.wis
        stats["CHA"] = character.cha
        stats["HP"] = character.hp
        stats["AC"] = character.arm_c
        stats["GP"] = character.gold
        stats["SPD"] = character.spd
        stats["LEVEL"] = character.lvl
        stats["XP"] = character.xp

        print(f"""\n
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        | NAME: {character.name.upper().center(39)}   |
        | RACE: {character.race.upper().center(39)}   |
        | CLASS: {character.char_class.upper().center(38)}   |
        | LEVEL: {stats['LEVEL']}{' '*(2-len(str(stats['LEVEL'])))}                                       |
        |                                                 |
        | STR: {stats['STR']}{' '*(2-len(str(stats['STR'])))} | DEX: {stats['DEX']}{' '*(2-len(str(stats['DEX'])))} | CON: {stats['CON']}{' '*(2-len(str(stats['CON'])))} | INT: {stats['INT']}{' '*(2-len(str(stats['INT'])))} | WIS: {stats['WIS']}{' '*(2-len(str(stats['WIS'])))} | 
        | CHA: {stats['CHA']}{' '*(2-len(str(stats['CHA'])))} |                                       |
        | ARMOR CLASS: {stats['AC']}{' '*(2-len(str(stats['AC'])))} | SPEED: {stats['SPD']}{' '*(2-len(str(stats['SPD'])))}                     |
        |                                                 |
        | HIT POINTS: {stats['HP']}{' '*(2-len(str(stats['HP'])))} | SPELL SLOTS: {'0'+' '*(2-len('2'))}                |
        |                                                 |
        | GOLD: {stats['GP']}{' '*(2-len(str(stats['GP'])))} | XP: {stats['XP']}{' '*(2-len(str(stats['XP'])))}                               |
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        \n\n\n\n""")

    def class_list(self): # passed testing in new main
        """function with a for loop to print each of the classes dictionary items"""

        num = 1
        for class_type in classes:
            print(f'{num}. {class_type}')
            num += 1

    def race_list(self): # passed testing in new main
        """function with a for loop to print a each of the races dictionary items"""

        num = 1
        for race_type in races:
            print(f'{num}. {race_type}')
            num += 1

    def get_valid_class(self): # passed testing in new main
        """Prompt user for class against list of avaiable classes then validates input and returns class name"""

        valid = False
        while not valid:
            self.class_list()
            class_name = input(f"Type in your character's class from the options above:\n")
            class_name = class_name.title()
            if class_name in classes:
                valid = True
            else:
                print(f"Invalid class name: {class_name}\n")
        return class_name
    
    def get_valid_race(self): # passed testing in new main
        """Prompt user for race against list of avaiable racees then validates input and returns race name"""

        valid = False
        while not valid:
            self.race_list()
            race_name = input(f"Type in your character's race from the options above:\n")
            race_name = race_name.title()
            if race_name in races:
                valid = True
            else:
                print(f"Invalid race name: {race_name}\n")
        return race_name
    
    def valid_class(self, class_name): # passed testing in new main
        """checks if class name arg is in the class list"""

        if class_name in classes:
            return True
        elif class_name not in classes:
            return False 
    
    def valid_race(self, race_name): # passed testing in new main
        """checks if race name arg is in the race list"""
        
        if race_name in races:
            return True
        elif race_name not in races:
            return False

    def get_name(self):
        """prompt user for a name, returns name"""
        name = input("Enter your name:\n")
        return name.title()
    
    def check(self, check_type): 
        """Handles validating check types and calculating DC amount based on randint range and current_difficulty settings"""

        valid_types = [
        'acrobatics', 'animal_handling', 'arcana', 'athletics', 'deception', 
        'history', 'insight', 'intimidation', 'investigation', 'medicine', 
        'nature', 'perception', 'performance', 'persuasion', 'religion', 'sleight_of_hand', 
        'stealth', 'survival', 'str','dex', 'con', 'int', 'wis', 'cha']

        check_dc = 0

        if check_type.lower() in valid_types:
            check_dc = r.randint(5, 13) + settings.current_difficulty + settings.location_difficulty
            return check_dc

    def create_character(self):
        """function to prompt user for all information to build a Player class instance as the users character."""
         
        name = input("Enter your name:\n")
        name = name.title()

        char_class = self.get_valid_class()

        race = self.get_valid_race()
    
        player = p(name, race, char_class)
        return player

# Instance of settings
settings = settings.Settings()
