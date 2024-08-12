# Dijjon New Main
# Developed & designed by: Zane M Deso
# Content by: John P Swanson
# Purpose: New Main will act as the entrance point for the program to run.


import random as r
import scripts.entity.Mob as mb
import scripts.mechanics.dice_Roll as dr
import scripts.entity.Player as p
import master as m
import scripts.mechanics.combat as c
import resources.quests.EnchantedForest as EF
from scripts.settings import Settings as s
from resources.core_library import classes as cls
from resources.core_library import name_list as nm
from resources.core_library import races as rc

last_var = None # var that stores the value of the last called variable in a new variable:

def combat_sim(): # tested and works in main
    bandit = p.Player('Bandit', r.choice(list(rc)), r.choice(list(cls)), is_enemy=True) # instantiate a new player
    master.sheet(bandit) # character sheet style layout player info
    # Setup combat scenario
    combat = c.Combat([player, bandit])
    # Run the combat
    combat.start_combat()

def skill_check_test():
    bandit = p.Player('Bandit', r.choice(list(rc)), r.choice(list(cls)), is_enemy=True) # instantiate a new player
    master.sheet(bandit) # character sheet style layout player info
    print(f'Did {player.get_name()} pass the dex Check?: {master.check("dex", player.player_check_roll("dex"))}') # example dex check
    print(f'Did {player.get_name()} pass the investigation Check?: {master.check("investigation", player.player_check_roll("investigation"))}') # example investigation check
    print(f'The winner of the opposing check is: {master.opposing_check(player, bandit, "str")}') # example opposing check

def create_player():
    player = p.Player(master.get_name(), master.get_valid_race(), master.get_valid_class()) # instantiate a new player
    master.sheet(player) # character sheet style layout player info

master = m.Master() # Instantiate Master in main

main_game_loop = True

player = p.Player(master.get_name(), master.get_valid_race(), master.get_valid_class()) # instantiate a new player
master.sheet(player) # character sheet style layout player info
 
# # # _________TESTS__________# # # 
# test skill check outcomes in main
# skill_check_sim()

# test combat scenario in main
# combat_sim()
# # # _________TESTS___END____# # #


while main_game_loop:
    if player is None:
        create_player()

    print("This is the hardcoded main menu.")
    print("1. Enter the Enchanted Forest\n ")
    input("What would you like to do? (Pick an option above...)")
    print("JK there was only one option.")
    forest = EF.EnchantedForest()
    forest.walk_forest(player)

    
    input("End of loop reach.") # hold here