# Dijjon New Main
# Developed & designed by: Zane M Deso
# Content by: John P Swanson
# Purpose: New Main will act as the entrance point for the program to run.


import random
import buildMob as mb
import dice_Roll as dr
import Player as p
import master as m
from settings import Settings as s

# var that stores the value of the last called variable in a new variable:
last_var = None

# Instantiate Master in main
master = m.Master()


main_game_loop = True
player = p.Player(master.get_name(), master.get_valid_race(), master.get_valid_class()) # instantiate a new player
master.sheet(player) # character sheet style layout player info
 
print(f'Passed dex Check?: {master.check("dex", player.player_check_roll("dex"))}') # example dex check
print(f'Passed int Check?: {master.check("int", player.player_check_roll("int"))}') # example int check
print(f'Passed arcana Check?: {master.check("arcana", player.player_check_roll("arcana"))}') # example arcana check
print(f'Passed investigation Check?: {master.check("investigation", player.player_check_roll("investigation"))}') # example investigation check
print(f'Passed sleight of hand Check?: {master.check("sleight_of_hand", player.player_check_roll("sleight_of_hand"))}') # example sleight_of_hand check

while main_game_loop:


    


    input() # hold here