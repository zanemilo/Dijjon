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
player = p.Player(master.get_name(), master.get_valid_race(), master.get_valid_class())
# player.display_info() # simple layout player info
master.sheet(player) # character sheet style layout player info
print(master.check('dex', (dr.roll_d20() + player.get_modifier(player.get_dex()))))

while main_game_loop:


    


    input() # hold here