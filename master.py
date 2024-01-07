import Player as p
from core_library import races
from core_library import classes

class Master:
    """Class for actions or deciscions a DM would typically make in the overarching gameplay, story etc."""

    def sheet(character): 
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

    def class_list(self):
        """function with a for loop to print each of the classes dictionary items"""

        num = 1
        for class_type in classes:
            print(f'{num}. {class_type}')
            num += 1

    def race_list(self):
        """function with a for loop to print a each of the races dictionary items"""

        num = 1
        for race_Array in self.races:
            print(f'{num}. {race_Array}')
            num += 1

    # checks if class name input is in the class list
    def get_valid_class(self):
        """checks if class name input is in the class list"""

        valid_class = False
        while not valid_class:
            self.class_List()
            class_name = input(f"Please choose your character's class: \n")
            class_name = class_name.title()
            if class_name in self.classes:
                valid_class = True
            else:
                print(f"Invalid class name: {class_name}\n")
        return class_name
    
    def get_valid_race(self):
        """checks if race name input is in the race list"""
        valid_race = False
        while not valid_race:
            self.race_List()
            race_name = input(f"Choose your character's race:\n")
            race_name = race_name.title()
            if race_name in self.races:
                valid_race = True
            else:
                print(f"Invalid race name: {race_name}\n")
        return race_name

    def create_character(self):
        """method to prompt user for name then resaves the input to title case class choice and race choice"""
         
        name = input("Enter your name:\n")
        name = name.title()
        print('Name Stored as:',name, '\n')
        char_class = self.get_valid_class()
        race = self.get_valid_race()
        character_class = self.classes.get(char_class, None)
        if character_class is None:
            raise ValueError(f"Invalid class name: {char_class}\n")
        return character_class(name, race)