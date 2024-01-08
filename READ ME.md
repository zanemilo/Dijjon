This is the official documentation for Dijjon Beta.
READ ME Last Updated on 1/6/2024







Current Goals of project: priority from high-low as follows(!,H,M,L)

[H]Move away from long single file of spaghetti code. I would like to try to refactor bits of code into dedicated files that will be imported into the main game loop later on. This way code is easier read, review takes much less time and focus maintains on development. Break it down into OOP Classes (ie, Player Class should be dedicated class with sep file)

[M]Small idea for menu functions such as inn_menu... temporarily(once selction is made simply delete the option from the list or dictionary) append table to end with 'quit' or 'back' or 'return' only for sake of adding option to the enumerated output for user to select from. This way user won't assume they are stuck in menu.
-Another idea, showcased in Python crash course is to print('If you would like to quit at anytime, enter 'q'') followed by incorporating that input into the if elif else logic tree for the menu.

[L]Add functionality for quest generation. Start small such as swapping the reward for a rand item on reward table or swapping enemy to be encountered or the total num of enemies in encounter.

[L]Create a dictionary with mad-lib type phrases that each type of commoner job might say. This could include information about other NPCs within town, comments on events (including events triggered by the player)

[L] Player Inventory UI currently displays as "1. Oats - 1" Where the second '1' is the monetary value of the oats. It looks like player has 1 oats. Should change to displayt either quantity or label it as '1 gp'




Bugs to fix:

[M]give_item function is not working properly, work around is to player.inventory.pop(item) this removes the whole key AND value. I want to be able to append/update the value and/or pop if the value reaches 0. This sounds do able with a while loop to check while player.inventory(item) == 0: player.inventory.pop(item)??



Major Change Log:

Integrated DijjonAlphaDevelopment folder with Git for ease of tracking progress. (win+x+i, then cd to alph dev folder, git status, git log git commit -m)

Refactoring player and npc creation to dedicated class files to be referenced in main. Expanded Classes and Races which have been refactored to core library 1/6/2024

[DONE]Find a way to enumerate race, class selection as is done in the menu functions. This way user may either input the name of the selection OR the enumeration corresponding with the selection. Both should be valid.