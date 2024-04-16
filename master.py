# Dijjon master Class
# Developed & designed by: Zane M Deso
# Purpose: This class is the main driver and will be the DM in a sense when it comes to making choices behind the scenes.

import Player as p
import settings
import random as r
import dice_Roll as dr
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

    def get_name(self): # passed testing in new main
        """prompt user for a name, returns name"""
        name = input("Enter your name:\n")
        return name.title()
    
    def check(self, check_type, player_roll, bias = r.randint(1, 18)): # passed testing in new main
        """Handles validating check types and calculating DC amount based on randint range and current_difficulty settings"""

        check_type = check_type.lower()
        valid_types = [
        'acrobatics', 'animal_handling', 'arcana', 'athletics', 'deception', 
        'history', 'insight', 'intimidation', 'investigation', 'medicine', 
        'nature', 'perception', 'performance', 'persuasion', 'religion', 'sleight_of_hand', 
        'stealth', 'survival', 'str','dex', 'con', 'int', 'wis', 'cha']

        check_dc = 0
        passed_check = False

        if check_type.lower() in valid_types:
            check_dc = bias + settings.current_difficulty + settings.location_difficulty
            # print(f'Check DC: {check_dc}')
            if player_roll >= check_dc:
                passed_check = True

            return passed_check

    def create_character(self): # passed testing in new main
        """function to prompt user for all information to build a Player class instance as the users character."""
         
        name = input("Enter your name:\n")
        name = name.title()

        char_class = self.get_valid_class()

        race = self.get_valid_race()
    
        player = p(name, race, char_class)
        return player

    def opposing_check(self, entity_one, enitity_two, check_type): # passed testing in new main
        """Take two opposing instances of (currently only) Player class and conduct rolls and checks"""

        e_one_roll = self.check(check_type, entity_one.player_check_roll(check_type)) # FIX ME: To adjust this once I have used inheritance correctly,
        e_two_roll = self.check(check_type, enitity_two.player_check_roll(check_type)) # just use the check_roll method associated from the parent class

        if e_one_roll < e_two_roll:
            return enitity_two.get_name()
        elif e_two_roll < e_one_roll:
            return entity_one.get_name()
        elif e_one_roll == e_two_roll:
            return self.opposing_check(entity_one, enitity_two, check_type)

    def combat_simulation(self, entity_one, entity_two):
        """Simulate turn-based combat between two entities"""
        print("Starting combat simulation...")
        while entity_one.get_hp() > 0 and entity_two.get_hp() > 0:
            # Entity One's turn
            print(f"{entity_one.get_name()}'s turn:")
            action = input("Choose an action (attack): ")
            if action.lower() == "attack":
                # Calculate attack roll
                attack_roll = dr.roll_d20() + entity_one.get_modifier(entity_one.get_str())
                print(f"{entity_one.get_name()} rolls {attack_roll} to attack.")
                # Check if attack hits
                if attack_roll >= entity_two.get_arm_c():
                    damage = dr.roll_d6() + entity_one.get_modifier(entity_one.get_str())
                    print(f"{entity_one.get_name()} hits {entity_two.get_name()} for {damage} damage!")
                    entity_two.set_hp(entity_two.get_hp() - damage)
                else:
                    print(f"{entity_one.get_name()} misses the attack.")

            # Check if Entity Two is still alive
            if entity_two.get_hp() <= 0:
                print(f"{entity_two.get_name()} has been defeated!")
                break

            # Entity Two's turn
            print(f"{entity_two.get_name()}'s turn:")
            action = input("Choose an action (attack): ")
            if action.lower() == "attack":
                # Calculate attack roll
                attack_roll = dr.roll_d20() + entity_two.get_modifier(entity_two.get_str())
                print(f"{entity_two.get_name()} rolls {attack_roll} to attack.")
                # Check if attack hits
                if attack_roll >= entity_one.get_arm_c():
                    damage = dr.roll_d6() + entity_two.get_modifier(entity_two.get_str())
                    print(f"{entity_two.get_name()} hits {entity_one.get_name()} for {damage} damage!")
                    entity_one.set_hp(entity_one.get_hp() - damage)
                else:
                    print(f"{entity_two.get_name()} misses the attack.")

            # Check if Entity One is still alive
            if entity_one.get_hp() <= 0:
                print(f"{entity_one.get_name()} has been defeated!")
                break

# Instance of settings
settings = settings.Settings()
