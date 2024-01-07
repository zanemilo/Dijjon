import random
import buildMob
import dice_Roll
import Player
import master
from settings import Settings as s

# var that stores the value of the last called variable in a new variable:
last_var = None


main_game_loop = True

while main_game_loop:
    master.class_list()