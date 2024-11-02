# Dijjon master Class
# Developed & designed by: Zane M Deso
# Purpose: This class is the main driver and will be the DM in a sense when it comes to making choices behind the scenes.

import scripts.entities.Player as p 
import src.core.settings as settings 
import random as r  
import scripts.game_mechanics.dice_Roll as dr 
from core.core_library import races 
from core.core_library import classes 


class Master:
    """
    Master Class for managing actions and decisions typically handled by a Dungeon Master (DM) 
    in the overarching gameplay and story. This class facilitates character creation, validations, 
    checks, and combat simulations.
    """

    def sheet(self, character):  # passed testing in new main
        """
        Generate and display the character sheet for a given character.

        Args:
            character (Player): The player character for whom the sheet is being generated.
        """
        # Dictionary of character instance's stats used for sheet to pull updated info
        stats = {
            "STR": character.str,
            "DEX": character.dex,
            "CON": character.con,
            "INT": character.intel,
            "WIS": character.wis,
            "CHA": character.cha,
            "HP": character.hp,
            "AC": character.arm_c,
            "GP": character.gold,
            "SPD": character.spd,
            "LEVEL": character.lvl,
            "XP": character.xp,
        }

        # This may be redundant, will need to test
        # EDIT: This is absolutely redundant, will replace sheet function ahead.
        stats["STR"] = character.str
        stats["DEX"] = character.dex
        stats["CON"] = character.con
        stats["INT"] = character.intel
        stats["WIS"] = character.wis
        stats["CHA"] = character.cha
        stats["HP"] = character.hp
        stats["AC"] = character.arm_c
        stats["GP"] = character.gold
        stats["SPD"] = character.spd
        stats["LEVEL"] = character.lvl
        stats["XP"] = character.xp

        # Display the character sheet with formatted statistics
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

    def class_list(self):  # passed testing in new main
        """
        Display a numbered list of available character classes.

        This function iterates through the 'classes' dictionary and prints each class with a corresponding number.
        """
        num = 1  # Initialize a counter to number the classes
        for class_type in classes:
            print(f'{num}. {class_type}')  # Print each class with its corresponding number
            num += 1  # Increment the counter

    def race_list(self):  # passed testing in new main
        """
        Display a numbered list of available character races.

        This function iterates through the 'races' dictionary and prints each race with a corresponding number.
        """
        num = 1  # Initialize a counter to number the races
        for race_type in races:
            print(f'{num}. {race_type}')  # Print each race with its corresponding number
            num += 1  # Increment the counter

    def get_valid_class(self):  # passed testing in new main
        """
        Prompt the user to select a valid character class from the available options.

        This function repeatedly prompts the user until a valid class name is entered.

        Returns:
            str: The validated class name selected by the user.
        """
        valid = False  # Flag to indicate if a valid class has been chosen
        while not valid:
            self.class_list()  # Display the list of available classes
            class_name = input(f"Type in your character's class from the options above:\n")  # Prompt user for input
            class_name = class_name.title()  # Capitalize the first letter of each word in the class name
            if class_name in classes:
                valid = True  # Set flag to True if class is valid
            else:
                print(f"Invalid class name: {class_name}\n")  # Inform the user of invalid input
        return class_name  # Return the valid class name

    def get_valid_race(self):  # passed testing in new main
        """
        Prompt the user to select a valid character race from the available options.

        This function repeatedly prompts the user until a valid race name is entered.

        Returns:
            str: The validated race name selected by the user.
        """
        valid = False  # Flag to indicate if a valid race has been chosen
        while not valid:
            self.race_list()  # Display the list of available races
            race_name = input(f"Type in your character's race from the options above:\n")  # Prompt user for input
            race_name = race_name.title()  # Capitalize the first letter of each word in the race name
            if race_name in races:
                valid = True  # Set flag to True if race is valid
            else:
                print(f"Invalid race name: {race_name}\n")  # Inform the user of invalid input
        return race_name  # Return the valid race name

    def valid_class(self, class_name):  # passed testing in new main
        """
        Check if the provided class name is valid.

        Args:
            class_name (str): The class name to validate.

        Returns:
            bool: True if the class name is valid, False otherwise.
        """
        if class_name in classes:
            return True  # Return True if class name is valid
        elif class_name not in classes:
            return False  # Return False if class name is invalid

    def valid_race(self, race_name):  # passed testing in new main
        """
        Check if the provided race name is valid.

        Args:
            race_name (str): The race name to validate.

        Returns:
            bool: True if the race name is valid, False otherwise.
        """
        if race_name in races:
            return True  # Return True if race name is valid
        elif race_name not in races:
            return False  # Return False if race name is invalid

    def get_name(self):  # passed testing in new main
        """
        Prompt the user to enter a name for their character.

        Returns:
            str: The name entered by the user, properly formatted.
        """
        name = input("Enter your name:\n")  # Prompt user for character name
        return name.title()  # Capitalize the first letter of each word in the name

    def check(self, check_type, player_roll, bias=r.randint(1, 18)):  # passed testing in new main
        """
        Handle validating different types of checks and calculate the Difficulty Class (DC).

        This function determines whether a player's roll meets or exceeds the DC required for a specific check type.

        Args:
            check_type (str): The type of check being performed (e.g., 'acrobatics', 'strength').
            player_roll (int): The result of the player's roll.
            bias (int, optional): A bias value added to the DC. Defaults to a random integer between 1 and 18.

        Returns:
            bool: True if the player's roll is sufficient to pass the check, False otherwise.
        """
        check_type = check_type.lower()  # Convert check type to lowercase for consistency
        valid_types = [
            'acrobatics', 'animal_handling', 'arcana', 'athletics', 'deception', 
            'history', 'insight', 'intimidation', 'investigation', 'medicine', 
            'nature', 'perception', 'performance', 'persuasion', 'religion', 'sleight_of_hand', 
            'stealth', 'survival', 'str','dex', 'con', 'int', 'wis', 'cha']  # List of valid check types

        check_dc = 0  # Initialize difficulty class
        passed_check = False  # Initialize check result

        if check_type.lower() in valid_types:
            # Calculate the difficulty class (DC) based on bias and settings
            check_dc = bias + settings.current_difficulty + settings.location_difficulty
            # print(f'Check DC: {check_dc}')  # Debug print statement (commented out)
            if player_roll >= check_dc:
                passed_check = True  # Player passes the check if roll meets or exceeds DC

            return passed_check  # Return the result of the check

    def create_character(self):  # passed testing in new main
        """
        Prompt the user for all necessary information to create a new Player character.

        This includes name, class, and race. The function validates the inputs and 
        constructs a Player instance based on the provided information.

        Returns:
            Player: The newly created Player instance with the specified attributes.
        """
        name = input("Enter your name:\n")  # Prompt user for character name
        name = name.title()  # Capitalize the first letter of each word in the name

        char_class = self.get_valid_class()  # Get a valid class from the user

        race = self.get_valid_race()  # Get a valid race from the user
    
        player = p(name, race, char_class)  # Create a Player instance with the provided name, race, and class
        return player  # Return the created Player instance

    def opposing_check(self, entity_one, enitity_two, check_type):  # passed testing in new main
        """
        Conduct a check between two opposing Player instances based on a specific check type.

        Args:
            entity_one (Player): The first player entity.
            enitity_two (Player): The second player entity.
            check_type (str): The type of check to perform (e.g., 'strength', 'dexterity').

        Returns:
            str: The name of the entity that wins the check.
        """
        # Perform a check for entity one using their roll for the specified check type
        e_one_roll = self.check(check_type, entity_one.player_check_roll(check_type))  # FIX ME: To adjust this once I have used inheritance correctly,
        # Perform a check for entity two using their roll for the specified check type
        e_two_roll = self.check(check_type, enitity_two.player_check_roll(check_type))  # just use the check_roll method associated from the parent class

        if e_one_roll < e_two_roll:
            return enitity_two.get_name()  # Return entity two's name if they win the check
        elif e_two_roll < e_one_roll:
            return entity_one.get_name()  # Return entity one's name if they win the check
        elif e_one_roll == e_two_roll:
            return self.opposing_check(entity_one, enitity_two, check_type)  # Repeat the check in case of a tie

    def combat_simulation(self, entity_one, entity_two):
        """
        Simulate a turn-based combat scenario between two entities.

        This function handles the flow of combat, alternating turns between the two entities
        until one of them is defeated.

        Args:
            entity_one (Player): The first entity participating in combat.
            entity_two (Player): The second entity participating in combat.
        """
        print("Starting combat simulation...")  # Announce the start of combat simulation
        while entity_one.get_hp() > 0 and entity_two.get_hp() > 0:
            # Entity One's turn
            print(f"{entity_one.get_name()}'s turn:")  # Announce whose turn it is
            action = input("Choose an action (attack): ")  # Prompt for action
            if action.lower() == "attack":
                # Calculate attack roll: d20 + strength modifier
                attack_roll = dr.roll_d20() + entity_one.get_modifier(entity_one.get_str())
                print(f"{entity_one.get_name()} rolls {attack_roll} to attack.")  # Display the attack roll
                # Check if the attack hits based on target's armor class
                if attack_roll >= entity_two.get_arm_c():
                    # Calculate damage: d6 + strength modifier
                    damage = dr.roll_d6() + entity_one.get_modifier(entity_one.get_str())
                    print(f"{entity_one.get_name()} hits {entity_two.get_name()} for {damage} damage!")  # Announce damage
                    entity_two.set_hp(entity_two.get_hp() - damage)  # Deduct damage from target's HP
                else:
                    print(f"{entity_one.get_name()} misses the attack.")  # Announce miss

            # Check if Entity Two is still alive
            if entity_two.get_hp() <= 0:
                print(f"{entity_two.get_name()} has been defeated!")  # Announce defeat
                break  # Exit combat if Entity Two is defeated

            # Entity Two's turn
            print(f"{entity_two.get_name()}'s turn:")  # Announce whose turn it is
            action = input("Choose an action (attack): ")  # Prompt for action
            if action.lower() == "attack":
                # Calculate attack roll: d20 + strength modifier
                attack_roll = dr.roll_d20() + entity_two.get_modifier(entity_two.get_str())
                print(f"{entity_two.get_name()} rolls {attack_roll} to attack.")  # Display the attack roll
                # Check if the attack hits based on target's armor class
                if attack_roll >= entity_one.get_arm_c():
                    # Calculate damage: d6 + strength modifier
                    damage = dr.roll_d6() + entity_two.get_modifier(entity_two.get_str())
                    print(f"{entity_two.get_name()} hits {entity_one.get_name()} for {damage} damage!")  # Announce damage
                    entity_one.set_hp(entity_one.get_hp() - damage)  # Deduct damage from target's HP
                else:
                    print(f"{entity_two.get_name()} misses the attack.")  # Announce miss

            # Check if Entity One is still alive
            if entity_one.get_hp() <= 0:
                print(f"{entity_one.get_name()} has been defeated!")  # Announce defeat
                break  # Exit combat if Entity One is defeated


# Instance of settings
settings = settings.Settings()  # Creating an instance of the Settings class from the settings module
