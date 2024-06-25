# Dijjon ForgottenTombs
# Developed & designed by: Zane M Deso
# Purpose: Placeholder Quest/Event/Location Idea

import random as r
import Mob as mb
import dice_Roll as dr
import Player as p
import master as m
import combat as c
from settings import Settings as s
from core_library import classes as cls
from core_library import name_list as nm
from core_library import races as rc

class EnchantedForest:
    def __init__(self):
        self.tasks_completed = 0
        self.path_found = False

    def display_options(self, options):
        counter = 1
        for i in range(len(options)):
            print(f"\n{counter}. {options[i]}")
            counter += 1
        

    def walk_forest(self, player):
        """Entry Function for this quest. Acts as main function."""
        print("\n\nYou step into the vibrant, living forest, where the trees seem to whisper.")
        options = ['help', 'solve', 'continue']
        while not self.path_found:
            option = input("\n\nChoose to 'help' a creature, 'solve' a forest puzzle, or 'continue' walking? ")
            if option in options:
                if option == 'help':
                    self.help_creature(player)
                elif option == 'solve':
                    print("\n\n solve puzzle AWT IMPLEMENTATION\n\n")
                    self.walk_forest(player)
                    #self.solve_puzzle()
                elif option == 'continue':
                    print("\n\n continue AWT IMPLEMENTATION\n\n")
                    self.walk_forest(player)
                    #self.find_path()
                else:
                    print("Invalid choice. Try again.")

    def help_creature(self, player):
        """Player encounters a creature that they may attempt to help or not"""
        print("\n\nYou hear a faint rustling followed by a soft, distressed mewing from beneath a cluster of ferns.\nAs you approach, the sound grows clearer, and you discover a small Tressym caught in a tangled mess of thorns.\nIts delicate wings flutter weakly, shimmering with a dusting of iridescent scales that catch the light like tiny stars.\nThe Tressym's eyes meet yours, shimmering with a mixture of fear and hope.")
        options = ['help', 'leave it', 'end it']
        #option = input(f"{self.display_options(options)}")
        option = input(f"\n\nChoose to 'help', 'leave', or 'kill' the creature? ")
        if option.lower() in options:
            if option == 'help':
                check = player.player_check_roll('dex')
                print(f"DEX CHECK: {check}")
                if check < 12:
                    self._help_creature_fail()
                elif check >= 12:
                    self._help_creature_pass()

            elif option == 'leave':
                pass
            elif option == 'kill':
                self._help_creature_death()
        else:
            option = input()
        self.tasks_completed += 1

    def _help_creature_fail(self):
        print("\nDespite your efforts, the thorns prove too intricate and pull at the Tressym's delicate wings. With every gentle tug you attempt, the creature lets out a pained cry that tugs at your heart. Realizing that brute force could harm the creature further, you stop and search desperately around for another way to help. As you hesitate, the Tressym gives one desperate flutter and frees itself, though its wings now bear slight tears, marring their perfect symmetry. It gives you a long, sorrowful look before limping away into the underbrush, its trust in you shaken. As it disappears, the forest's shadows seem to deepen, and you can't shake the feeling that your failure has cost you more than just a chance to help.")
        
        input("Press enter to continue...")
        
        self.tasks_completed += 1

    def _help_creature_pass(self):
        print("\nGently, you work to free the creature, mindful of its fragile wings, which resemble the vibrant pattern of a butterfly's. With each careful movement, the Tressym's soft purring grows louder, a sound that warms the cool air of the forest. Finally, it steps free, uninjured and grateful. In a display of gratitude, the Tressym circles above you, casting playful shadows on the ground and leaving a trail of sparkling, magical dust. It lands briefly on your shoulder, nuzzling against your cheek, then leaps into the air and disappears amongst the treetops, leaving behind a feeling of goodwill that seems to lighten the forest's whispering shadows. You gain a small, enchanted feather that glows faintly in your pocket, a token of the forest's magic and mystery.")

        input("Press enter to continue...")
        
        self.tasks_completed += 1

    def _help_creature_death(self):
        print("""\nThe Tressym's soft cries tug at your conscience, yet a part of you steels against the plaintive mewling. The forest around you seems to hold its breath as you approach, the decision weighing heavily in your mind. You realize that freeing the creature might be beyond your current skill, or perhaps the danger of drawing the attention of something more sinister lurking within the forest looms too large in your thoughts.

With a heavy heart, you opt for a merciful end to the Tressym's suffering. As you prepare to act, the creature's eyes meet yours, a glint of understanding—or perhaps resignation—flashing within. The deed is quick, and the Tressym's body relaxes as its spirit escapes the pain-ridden confines of the mortal realm. The air grows chill as the forest's whispers rise in a mournful dirge.

As you stand, the weight of your choice settles around you like a cloak. Shadows seem to draw closer, a silent testament to the gravity of life and death decisions made under the canopy of the Enchanted Forest. You leave the scene with a somber respect for the harsh realities of nature, and perhaps, a reminder of the burdens adventurers must bear.""")
        
        input("Press enter to continue...")
        
        self.tasks_completed += 1

    def solve_puzzle(self):  # FIX ME: Still needs to be wrote out

        print() # Additional Flavor text here
        print("""As you are traveling through the woods you find yourself at the edge of a creek.
               \nAt the edge of the creek a stump sized stone catches your eye. Engravings riddle the face of the stone.
               \nYou carefully brush aside the overgrowth and find these words burrowed into the surface: 
               \n
               \nIn the creek below, redirect the waters flow
               \nSo the water swirls as an otter unfurls
               \nWhat you will find will be worth the time
               \n""")
        puzzle_active = True

        while puzzle_active:

            print(""" 
            \nAs you shift your attention to the creek you notice that the creekbed is made up of large cobblestone.
            \nYou can arrange the stones in one of the below options depicted:
            \n
            \n1.
            \n
            \n |    o   o       |
            \n |    o      o     | 
            \n  |   o   o   o     |
            \n   |  o   o      o   |
            \n    | o          o    |
            \n    | o        o      |
            \n   |  o o    o       |
            \n  |   o     o       |
            \n |    o   o     o  |
            \n      
            \n2.
            \n
            \n
            \n |       o    o   |
            \n |    o    o    o  | 
            \n  |                 |
            \n   |   o    o     o  |
            \n    |                 |
            \n    |  o    o     o   |
            \n   |    o            |
            \n  |         o       |
            \n |    o         o  |
            \n
            \n3.
            \n
            \n |                |
            \n |   o  o    o     | 
            \n  |        o    o   |
            \n   |          o      |
            \n    |  o    o         |
            \n    |            o    |
            \n   |  o  o    o      |
            \n  |         o     o |
            \n |   o             |
            \n
            \n
            \n4.
            \n
            \n |  o    o     o  |
            \n |   o      o   o  | 
            \n  |   o      o   o  |
            \n   |   o    o   o    |
            \n    |  o   o    o     |
            \n    | o   o    o      |
            \n   | o  o     o      |
            \n  | o   o    o      |
            \n |   o   o    o    |
            \n""")

            answer = input()


         
        print("You adjust the stones in a creek, altering the flow and revealing a new path.")
        self.tasks_completed += 1

    def find_path(self):  # FIX ME: Still needs to be wrote out and connected to whatever else it could be connected to
        if self.tasks_completed >= 3:
            print("The heart of the forest opens before you, revealing the ancient being.")
            self.path_found = True
        else:
            print("You need to engage more with the forest to find your way.")

# master = m.Master() # Instantiate Master for testing"""
# dummy_player = p.Player('Bandit', r.choice(list(rc)), r.choice(list(cls)), is_enemy=True) # instantiate a new player for testing
# master.sheet(dummy_player) # character sheet style layout player info

# forest = EnchantedForest()
# forest.walk_forest(dummy_player)
