# Dijjon ForgottenTombs
# Developed & designed by: Zane M Deso
# Purpose: Placeholder Quest/Event/Location Idea

import random as r
import sys
sys.path.append("..")  # Adds the parent directory to the Python module search path
from systems.core_library import reward_items_table

class EnchantedForest:
    def __init__(self):
        self.tasks_completed = 0
        self.path_found = False

    def display_options(self, options):
        counter = 1
        for i in range(len(options)):
            print(f"\n{counter}. {options[i]}")
            counter += 1
        
    def intro(self, player):
        """Entry Function for this quest. Acts as main function."""
        print(F"{player.name} . . .")
        input()
        print(F"{player.name} . . . .")
        input()
        print(F"{player.name} wake up!")
        input()
        if player.check_roll('perception') >= 15:
            print(F"From the looming void, light reaches your vision. . . Daylight.\nYou notice a figure above you, humanoid-like.\nYour vision clears and you see a petite gnomish woman. Your know her.\nGreselda.")
            input()
        else:
            print(F"As you stir from the looming darkness your vision remains blurred, you wince at the daylight.")
            input()
        options = ['Swing your fist as hard as you can in the direction of the tugging. [Attack Roll]', 'Take a closer look', 'Lay completely still.', 'Scream as loud as you can!','1','2', '3', '4']
        answer = None
        while answer not in options:
            print(F"You feel something tugging at your body. What do you do?")
            self.display_options(options[0:4])
            answer = input()
            if answer not in options:
                print("Invalid option")
            elif answer == options[0] or answer == '1':
                print("Attack: AWT Implementation")
            elif answer == options[1] or answer == '2':
                print("Closer Look: AWT Implementation")
            elif answer == options[2] or answer == '3':
                print("Stay Still: AWT Implementation")
            elif answer == options[3] or answer == '4':
                print("Scream: AWT Implementation")
            
                
        self.find_path(player)
    
    def old_walk_forest(self, player):
        """"""
        print("\n\nYou step into the vibrant, living forest, where the trees seem to whisper.")
        options = ['help', 'solve', 'continue']
        while not self.path_found:
            option = input("\n\nChoose to 'help' a creature, 'solve' a forest puzzle, or 'continue' walking? ")
            if option in options:
                if option == 'help':
                    self.help_creature(player)
                elif option == 'solve':
                    print("\n\n solve puzzle AWT IMPLEMENTATION\n\n")
                    self.old_walk_forest(player)
                    #self.solve_puzzle()
                elif option == 'continue':
                    print("\n\n continue AWT IMPLEMENTATION\n\n")
                    self.old_walk_forest(player)
                    #self.find_path()
                else:
                    print("Invalid choice. Try again.")

    def help_creature(self, player):
        """Player encounters a creature that they may attempt to help or not"""
        print("\n\nYou hear a faint rustling followed by a soft, distressed mewing from beneath a cluster of ferns.\nAs you approach, the sound grows clearer, and you discover a small Tressym caught in a tangled mess of thorns.\nIts delicate wings flutter weakly, shimmering with a dusting of iridescent scales that catch the light like tiny stars.\nThe Tressym's eyes meet yours, shimmering with a mixture of fear and hope.")
        options = ['help', 'leave', 'kill']
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
                print('leave selected')
                pass
            elif option == 'kill':
                print('kill selected')
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

    def solve_puzzle(self, player):

        print() # Additional Flavor text here
        print("""As you are traveling through the woods you find yourself at the edge of a creek.
               \nAt the edge of the creek a stump sized stone catches your eye. Engravings riddle the face of the stone.
               \nYou carefully brush aside the overgrowth and find these words burrowed into the surface: 
               \n
               \nIn the creek below, redirect the waters flow
               \nMake the water swirl for treasure to unfurl
               \nWhat you will find will be worth the time
               \n""")
        puzzle_active = True
        survival_check = player.player_check_roll('survival')
        nature_check = player.player_check_roll('perception')
        while puzzle_active:
            print("The creek sits at your feet and as you look over the rocks in the creek bed\n")
            if survival_check >= 10:
                print("Your hands move before your mind and you begin to arrange the stones letting your instincs guide you.\nA moment passes and the water begins to slowly but distincly swirl gainiing speed.\n The water continues swirling until it maintains speed and begins to glow a warm golden light.\nFrom the depths of the swirls a small shape emerges and bounces to the surface. A small chest awaits your retrieval.")
                puzzle_active = False
            elif nature_check >= 10:
                print("Your mind aligns with the forest around you, focusing in not on a single thing but in everything at once.\nYour hands find themselves gliding through the creek and guiding the stones into place to create a perfect swirl.\nThe water continues swirling until it maintains speed and begins to glow a warm golden light.\nFrom the depths of the swirls a small shape emerges and bounces to the surface. A small chest awaits your retrieval.")
                puzzle_active = False
            else:
                options = ['1','2','3']
                answer = None
                while answer not in options:
                    answer = input("There seems to be a few manners in which to rearrange the stones. Will you:\n1. Build a partial dam with an opening on one end\n2. Chaotically toss the rocks about and let them fall where they may.\n 3. Create an alternating pattern with the stones.")
                if answer == '1':
                    print("You carefully and precisely place the final stone in place and you take a step back to take in your handy work.\nA moment passes and the water begins to slowly but distincly swirl gainiing speed.\n The water continues swirling until it maintains speed and begins to glow a warm golden light.\nFrom the depths of the swirls a small shape emerges and bounces to the surface. A small chest awaits your retrieval.")
                    puzzle_active = False
                elif answer == '2':
                    lucky_roll = r.randrange(1, 100)
                    if lucky_roll == 100:
                        print("After the chaos settles and you smile in your menical stone tossings, you notice that the water begins to slowly but distincly swirl gainiing speed.\n The water continues swirling until it maintains speed and begins to glow a warm golden light.\nFrom the depths of the swirls a small shape emerges and bounces to the surface. A small chest awaits your retrieval.")
                        puzzle_active = False
                elif answer == '3':
                     print("After you place the last stone in place and examine your work it does not seem to resemble a swirl.")

        rewards = [reward_items_table[r.randint(1, 10)], reward_items_table[r.randint(1, 10)]] 
        
        print("You open the chest and retrieve ")
        for reward in rewards:
            player.get_item(1, reward)
                    


         
        print("After you adjusted the stones in a creek, the flow altered the forest around it revealing a new path.")
        self.tasks_completed += 1

    def find_path(self, player):  # FIX ME: Still needs to be wrote out and connected to whatever else it could be connected to
        print("TO BE IMPLEMENTED")
        if self.tasks_completed >= 3:
            print("The heart of the forest opens before you, revealing the ancient being.")
            self.path_found = True
        else:
            print("You need to engage more with the forest to find your way.")

# consider using below as assert for testing later on
# Otherwise this is deprecated.
# master = m.Master() # Instantiate Master for testing"""
# dummy_player = p.Player('Bandit', r.choice(list(rc)), r.choice(list(cls)), is_enemy=True) # instantiate a new player for testing
# master.sheet(dummy_player) # character sheet style layout player info

# forest = EnchantedForest()
# forest.solve_puzzle(dummy_player)
