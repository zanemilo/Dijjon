# Dijjon New Main
# Developed & designed by: Zane M Deso
# Purpose: main will act as the entrance point for the program to run.

import random as r  
import scripts.entity.Mob as mb  
import scripts.game_mechanics.dice_Roll as dr 
import scripts.entity.Player as p 
import master as m  
import scripts.game_mechanics.combat as c 
import resources.quests.EnchantedForest as EF  
from scripts.settings import Settings as s  
from resources.core_library import classes as cls  
from resources.core_library import name_list as nm  
from resources.core_library import races as rc 


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
    bandit = p.Player('Bandit', r.choice(list(rc)), r.choice(list(cls)), is_enemy=True)
    
    # Display the bandit's character sheet using the Master class
    master.sheet(bandit)
    
    # Setup combat scenario with the player and the bandit
    combat = c.Combat([player, bandit])
    
    # Run the combat simulation
    combat.start_combat()


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
    bandit = p.Player('Bandit', r.choice(list(rc)), r.choice(list(cls)), is_enemy=True)
    
    # Display the bandit's character sheet using the Master class
    master.sheet(bandit)
    
    # Perform a dexterity check for the player and print the result
    dex_passed = master.check("dex", player.player_check_roll("dex"))
    print(f'Did {player.get_name()} pass the dex Check?: {dex_passed}')
    
    # Perform an investigation check for the player and print the result
    investigation_passed = master.check("investigation", player.player_check_roll("investigation"))
    print(f'Did {player.get_name()} pass the investigation Check?: {investigation_passed}')
    
    # Conduct an opposing strength check between the player and the bandit and print the winner
    winner = master.opposing_check(player, bandit, "str")
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
    player_name = master.get_name()
    
    # Prompt the user to select a valid race from the available options
    player_race = master.get_valid_race()
    
    # Prompt the user to select a valid class from the available options
    player_class = master.get_valid_class()
    
    # Instantiate a new player with the provided name, race, and class
    new_player = p.Player(player_name, player_race, player_class)
    
    # Display the new player's character sheet using the Master class
    master.sheet(new_player)


# Instantiate the Master class to manage game mechanics and interactions
master = m.Master()

# Initialize the main game loop flag to True to start the game
main_game_loop = True

# Instantiate the player by prompting for name, race, and class
player = p.Player(master.get_name(), master.get_valid_race(), master.get_valid_class())

# Display the player's character sheet using the Master class
master.sheet(player)

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

    # Display the main menu options to the player
    print("This is the hardcoded main menu.")
    print("1. Enter the Enchanted Forest\n ")
    
    # Prompt the player to choose an option from the main menu
    user_choice = input("What would you like to do? (Pick an option above...)\n")
    
    # Inform the player about the available options (currently only one option)
    print("JK there was only one option.")
    
    # Instantiate the EnchantedForest scenario
    forest = EF.EnchantedForest()
    
    # Begin the introduction to the Enchanted Forest with the player character
    forest.intro(player)
    
    # Pause the loop to hold here until the player presses Enter
    input("End of loop reached.")  # Hold here to prevent the loop from restarting immediately
