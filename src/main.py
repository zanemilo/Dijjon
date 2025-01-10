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
from systems.core_library import classes, name_list, races, get_valid_class, get_valid_race
from systems.core_library import name_list  
from systems.core_library import races
from systems.ui.text import TextRenderer
from systems.Button import Button
from systems.ButtonManager import ButtonManager
from systems.Quest import Quest
from systems.QuestManager import QuestManager
from systems.a1_tasks import tasks as a1_tasks
from systems.a2_tasks import tasks as a2_tasks
from systems.a3_tasks import tasks as a3_tasks
from world import EnchantedForest as EF

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
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
    bandit.sheet()
    
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
    Used for a means to quickly test fucntionality in main.

    Steps:
    1. Instantiates a bandit player with random race and class.
    2. Displays the bandit's character sheet.
    3. Performs and prints the results of dexterity and investigation checks for the player.
    4. Determines and prints the winner of a strength-based opposing check between the player and the bandit.
    """
    # Instantiate a new bandit player with random race and class, marked as an enemy
    bandit = p.Player('Bandit', r.choice(list(races)), r.choice(list(classes)), is_enemy=True)
    
    # Display the bandit's character sheet using the Master class
    bandit.sheet()
    
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
    new_player.sheet()

# # # _________TESTS__________# # #
# Uncomment the following lines to run tests for skill checks and combat simulation

# test skill check outcomes in main
# skill_check_test()

# test combat scenario in main
# combat_sim()
# # # _________TESTS___END____# # #

# Sample Quest Data
qtype = {
    "find": Quest.find,
    "kill": Quest.kill,
    "skill_check": Quest.skill_check,
}

tasks = a1_tasks

# Instantiate Quest and QuestManager
quest = Quest("Find Finn", "Locate Finn in the town square", qtype, tasks)
quest_manager = QuestManager(quest, text_renderer, screen)

master = m.Master()  # Instantiate the Master class to manage game mechanics and interactions

button_manager = ButtonManager(screen)
button_manager.create_buttons(quest_manager.get_current_options())

player = p.Player(get_name(), get_valid_race(), get_valid_class())  # Instantiate the player by prompting for name, race, and class
player.sheet()  # Display stats to terminal

running = True
text_rendering_complete = False
text_renderer.reset(quest_manager.get_current_narrative())
options = quest_manager.get_current_options()

while running:
    # Ensure player is created before continuing
    if player is None:
        try:
            create_player()
        except Exception as e:
            print(f"Error creating player: {e}")
            running = False
            break

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle button clicks
        button_index = button_manager.handle_event(event)
        if button_index is not None:
            quest_manager.advance_step(button_index)
            prev_options = options
            options = quest_manager.get_current_options()
             # Update buttons only if options change
            if options != prev_options:
                try:
                    button_manager.create_buttons(options)
                except Exception as e:
                    print(f"Error updating buttons: {e}")
            # Update narrative text after advancing quest
            text_renderer.reset(quest_manager.get_current_narrative())
            
    # Clear the screen
    screen.fill((0, 0, 0))
    # Always draw buttons and update display
    button_manager.draw_buttons()
    # Render quest narrative and buttons
    if not quest_manager.is_quest_complete:
            text_renderer.update()
            text_renderer.draw()
    else:
        text_renderer.reset("Quest Complete! Congratulations!")
        text_renderer.update()
        text_renderer.draw()

    pygame.display.flip()

pygame.quit()

