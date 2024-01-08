import random
import buildMob
import dice_Roll
import Player as p
import master as m
from settings import Settings as s

# var that stores the value of the last called variable in a new variable:
last_var = None

# Instantiate Master in main
master = m.Master()

def create_character():
        """function to prompt user for all information to build a Player class instance as the users character."""
         
        name = input("Enter your name:\n")
        name = name.title()

        char_class = master.get_valid_class()

        race = master.get_valid_race()
    
        player = p.Player(name, race, char_class)
        return player

main_game_loop = True

while main_game_loop:

    player = create_character() # this makes it so the class instance created inside this function is accessible outside of the fucntions scope
    player.display_info() # simple layout player info
    master.sheet(player) # character sheet style layout player info

    x = master.check('religion')
    print(f'{x}')
        
    input() # hold here