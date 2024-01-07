import random
import buildMob
import dice_Roll
import Player
import master as m
from settings import Settings as s

# var that stores the value of the last called variable in a new variable:
last_var = None

# Instantiate Master in main
master = m.Master()

main_game_loop = True

while main_game_loop:

    x = master.valid_class(input().title())
    print(f"Passed Test: {x}")
    input() # hold here