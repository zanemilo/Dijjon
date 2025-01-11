
import random as r
import sys
sys.path.append("..")  # Adds the parent directory to the Python module search path

from entities.Player import Player
from systems.core_library import race_list, class_list, races, classes, name_list

class PlayerFactory:

    def __init__(self):
        pass

    def create_player(self, npc=False, enemy=False):
        """
        Creates a new player character by prompting the user for input.

        Alternatively allows for factory building of NPC players if npc
        param is True.

        Steps:
        1. Prompts the user to enter a name.
        2. Prompts the user to select a valid race.
        3. Prompts the user to select a valid class.
        4. Instantiates a new player with the provided information.
        5. Displays the player's character sheet.

        Returns:
            Player: Instance
        """
        if not npc:
            # Prompt the user to enter a name for the character
            player_name = self.get_init_name()
            
            # Prompt the user to select a valid race from the available options
            player_race = self.get_valid_race()
            
            # Prompt the user to select a valid class from the available options
            player_class = self.get_valid_class()
            
            # Instantiate a new player with the provided name, race, and class
            new_player = Player(player_name, player_race, player_class)
        if npc:
            if enemy:
                # Instantiate a new enemy npc with the randomly selected name, race, and class
                new_player = Player(r.choice(list(name_list)), r.choice(list(races)), r.choice(list(classes)), is_enemy=True)
            else:
                # Instantiate a new npc with the randomly selected name, race, and class
                new_player = Player(r.choice(list(name_list)), r.choice(list(races)), r.choice(list(classes)))
        
        return new_player
    
    def get_init_name(self):
        """
        Prompt the user to enter the name for their character.

        Does a verification step check to ensure player is satisfied with name.

        Returns:
            str: Name of player
        """
        choices = ['y', 'yes', '1', 1, 'n', 'no', '2', 2]
        valid = False
        
        while not valid:
            name = input("Please enter a name for your character:\n")
            if name:
                choice = None
                while choice not in choices:
                    print(f"Please confirm that you would like your character to be named {name}:\n")
                    choice = input("\n1. Yes\n2. No\n")
                if choice.lower() in choices[:4]:
                    valid = True
            else:
                print(f"Invalid name: {name}, please enter a valid name.")
        return name

    def get_valid_class(self):  # passed testing in new main
        """
        Prompt the user to select a valid character class from the available options.

        This function repeatedly prompts the user until a valid class name is entered.

        Returns:
            str: The validated class name selected by the user.
        """
        valid = False  # Flag to indicate if a valid class has been chosen
        while not valid:
            class_list()  # Display the list of available classes
            class_name = input(f"Type in your character's class or input the number the your selection from the list above:\n")  # Prompt user for input
            class_name = class_name.title()  # Capitalize the first letter of each word in the class name
            if class_name in classes:
                valid = True  # Set flag to True if class is valid
            elif len(classes) - int(class_name) >= 0:
                class_name = classes[int(class_name) - 1]
                valid = True  # Set flag to True if correct race option number is entered
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
            race_list()  # Display the list of available races
            race_name = input(f"Type in your character's race or input the number the your selection from the list above:\n")  # Prompt user for input
            race_name = race_name.title()  # Capitalize the first letter of each word in the race name
            if race_name in races:
                valid = True  # Set flag to True if race is valid
            elif len(races) - int(race_name) >= 0:
                race_name = races[int(race_name) - 1]
                valid = True  # Set flag to True if correct race option number is entered
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
        