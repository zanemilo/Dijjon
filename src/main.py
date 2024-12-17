# Dijjon New Main
# Developed & designed by: Zane M Deso
# Purpose: main will act as the entrance point for the program to run.

import random as r  
import pygame
import core.master as m  


from entities import Mob as mb
from entities import Player as p  
from src.core.settings import Settings as settings
from systems.combat import Combat as c
from systems.core_library import classes 
from systems.core_library import name_list  
from systems.core_library import races
from systems.ui.text import TextRenderer
from systems.Quest import Quest
from systems.QuestManager import QuestManager
from world import EnchantedForest as EF

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Dijjon')

# TextRenderer setup
text_renderer = TextRenderer(
    screen=screen,
    text="",
    font_name=None,
    font_size=24,
    color=(255, 255, 255),  # White text
    position=(50, 100),
    typing_speed=50  # Speed of typing effect
)

def class_list():  # passed testing in new main
        """
        Display a numbered list of available character classes.

        This function iterates through the 'classes' dictionary and prints each class with a corresponding number.
        """
        num = 1  # Initialize a counter to number the classes
        for class_type in classes:
            print(f'{num}. {class_type}')  # Print each class with its corresponding number
            num += 1  # Increment the counter

def race_list():  # passed testing in new main
    """
    Display a numbered list of available character races.

    This function iterates through the 'races' dictionary and prints each race with a corresponding number.
    """
    num = 1  # Initialize a counter to number the races
    for race_type in races:
        print(f'{num}. {race_type}')  # Print each race with its corresponding number
        num += 1  # Increment the counter

def get_valid_class():  # passed testing in new main
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

def get_valid_race():  # passed testing in new main
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

def valid_class(class_name):  # passed testing in new main
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

def valid_race(race_name):  # passed testing in new main
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
    
def get_name():  # passed testing in new main
        """
        Prompt the user to enter a name for their character.

        Returns:
            str: The name entered by the user, properly formatted.
        """
        name = input("Enter your name:\n")  # Prompt user for character name
        return name.title()  # Capitalize the first letter of each word in the name

def opposing_check(entity_one, enitity_two, check_type):  # passed testing in new main
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
        e_one_roll = check(check_type, entity_one.player_check_roll(check_type))  # FIX ME: To adjust this once I have used inheritance correctly,
        # Perform a check for entity two using their roll for the specified check type
        e_two_roll = check(check_type, enitity_two.player_check_roll(check_type))  # just use the check_roll method associated from the parent class

        if e_one_roll < e_two_roll:
            return enitity_two.get_name()  # Return entity two's name if they win the check
        elif e_two_roll < e_one_roll:
            return entity_one.get_name()  # Return entity one's name if they win the check
        elif e_one_roll == e_two_roll:
            return opposing_check(entity_one, enitity_two, check_type)  # Repeat the check in case of a tie

def combat_sim():
    """
    Simulates a combat scenario between the player and a bandit.

    Steps:
    1. Instantiates a bandit player with random race and class.
    2. Displays the bandit's character sheet.
    3. Sets up a combat scenario between the player and the bandit.
    4. Initiates and runs the combat.
    """
    # Instantiate a new bandit player with random race and class, marked as an enemy
    bandit = p.Player('Bandit', r.choice(list(races)), r.choice(list(classes)), is_enemy=True)
    
    # Display the bandit's character sheet using the Master class
    sheet(bandit)
    
    # Setup combat scenario with the player and the bandit
    combat = c.Combat([player, bandit])
    
    # Run the combat simulation
    combat.start_combat()

def check(check_type, player_roll, bias=r.randint(1, 18)):  # passed testing in new main
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
            # print(f'Check DC: {check_dc}')  # Debug print statement
            if player_roll >= check_dc:
                passed_check = True  # Player passes the check if roll meets or exceeds DC

            return passed_check  # Return the result of the check

def skill_check_test():
    """
    Tests various skill checks and opposing checks between the player and a bandit.

    Steps:
    1. Instantiates a bandit player with random race and class.
    2. Displays the bandit's character sheet.
    3. Performs and prints the results of dexterity and investigation checks for the player.
    4. Determines and prints the winner of a strength-based opposing check between the player and the bandit.
    """
    # Instantiate a new bandit player with random race and class, marked as an enemy
    bandit = p.Player('Bandit', r.choice(list(races)), r.choice(list(classes)), is_enemy=True)
    
    # Display the bandit's character sheet using the Master class
    sheet(bandit)
    
    # Perform a dexterity check for the player and print the result
    dex_passed = check("dex", player.player_check_roll("dex"))
    print(f'Did {player.get_name()} pass the dex Check?: {dex_passed}')
    
    # Perform an investigation check for the player and print the result
    investigation_passed = check("investigation", player.player_check_roll("investigation"))
    print(f'Did {player.get_name()} pass the investigation Check?: {investigation_passed}')
    
    # Conduct an opposing strength check between the player and the bandit and print the winner
    winner = opposing_check(player, bandit, "str")
    print(f'The winner of the opposing check is: {winner}')


def create_player():
    """
    Creates a new player character by prompting the user for input.

    Steps:
    1. Prompts the user to enter a name.
    2. Prompts the user to select a valid race.
    3. Prompts the user to select a valid class.
    4. Instantiates a new player with the provided information.
    5. Displays the player's character sheet.
    """
    # Prompt the user to enter a name for the character
    player_name = get_name()
    
    # Prompt the user to select a valid race from the available options
    player_race = get_valid_race()
    
    # Prompt the user to select a valid class from the available options
    player_class = get_valid_class()
    
    # Instantiate a new player with the provided name, race, and class
    new_player = p.Player(player_name, player_race, player_class)
    
    # Display the new player's character sheet using the Master class
    sheet(new_player)

def sheet(character):  # passed testing in new main
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


# Sample Quest Data
qtype = {
    "find": Quest.find,
    "kill": Quest.kill,
    "skill_check": Quest.skill_check,
}

tasks = {
    1: {
        "name": "Find Finn",
        "type": "find",
        "complete": False,
        "narrative": {
            1: "You arrive at the bustling town square...",
            2: "Finn is nowhere to be seen.",
        },
        "answers": {1: ["Look around"], 2: ["Ask someone nearby"]},
        "scripts": {1: None, 2: None},
    }
}

# Instantiate Quest and QuestManager
quest = Quest("Find Finn", "Locate Finn in the town square", qtype, tasks)
quest_manager = QuestManager(quest, text_renderer, screen)

# Instantiate the Master class to manage game mechanics and interactions
master = m.Master()

# Initialize the main game loop flag to True to start the game
main_game_loop = True

# Instantiate the player by prompting for name, race, and class
player = p.Player(get_name(), get_valid_race(), get_valid_class())

# Display the player's character sheet using the Master class
sheet(player)

# # # _________TESTS__________# # #
# Uncomment the following lines to run tests for skill checks and combat simulation

# test skill check outcomes in main
# skill_check_test()

# test combat scenario in main
# combat_sim()
# # # _________TESTS___END____# # #

# Start the main game loop
while main_game_loop:
    # Check if the player exists; if not, prompt to create a new player
    if player is None:
        create_player()

    # # Display the main menu options to the player
    # print("This is the hardcoded main menu.")
    # print("--------------------------------")
    # print("1. Enter the Enchanted Forest\n ")
    
    # # Prompt the player to choose an option from the main menu
    # user_choice = input("What would you like to do? (Pick an option above...)\n")
    
    
    # # Instantiate the EnchantedForest scenario
    # forest = EF.EnchantedForest()
    
    # # Begin the introduction to the Enchanted Forest with the player character
    # forest.intro(player)

    # if not quest_manager.is_quest_complete:
    #     quest_manager.render_current_narrative()
    #     pygame.display.flip()
    #     quest_manager.advance_step(1)
    # # Pause the loop to hold here until the player presses Enter
    # input("End of loop reached.")  # Hold here to prevent the loop from restarting immediately



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Check if the quest is complete
    if not quest_manager.is_quest_complete:
        # Render the current quest narrative
        quest_manager.render_current_narrative()
        
        # Simulate user selecting an option (Replace this with button logic)
        
        quest_manager.advance_step(1)
    else:
        text_renderer.reset("Quest Complete! Congratulations!")
        while not text_renderer.finished:
            screen.fill((0, 0, 0))
            text_renderer.update()
            text_renderer.draw()
            pygame.display.flip()
        running = False

    # Update display
    pygame.display.flip()

pygame.quit()
