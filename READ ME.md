This is the official documentation for Dijjon Beta.
Author: Zane M Deso
READ ME Last Updated on 5/7/2024

Dijjon (Current working name) is a text based game based on the Fantasy RPG world of Dijjon based on the creative work of John Philip Swanson. The game takes the player through a broken down version of the DnD 5e campaign written by John Philip Swanson. The text based game will showcase dynamics by injecting RNG into every interaction, encounter and outcome. No two play throughs should be the same. 





Current Goals of project: priority from high-low as follows(!,H,M,L)

[H] Refactor Player class to be a child of an Entity class, then set NPCs and Mobs as childs to the Entity class as well.

[H] Finish Implementation of Combat Class, this is an important feature in the over all game play and needs to be functional.

[H] Finish Implementation of First Bandit Quest Prototype to make a functional demo environment to test new features, troubleshoot bugs, and generally demonstrate with.

[H] Move away from long single file of spaghetti code. I would like to try to refactor bits of code into dedicated files that will be imported into the main game loop later on. This way code is easier read, review takes much less time and focus maintains on development. Break it down into OOP Classes (ie, Player Class should be dedicated class with sep file)

[M] Small idea for menu functions such as inn_menu... temporarily(once selction is made simply delete the option from the list or dictionary) append table to end with 'quit' or 'back' or 'return' only for sake of adding option to the enumerated output for user to select from. This way user won't assume they are stuck in menu.
-Another idea, showcased in Python crash course is to print('If you would like to quit at anytime, enter 'q'') followed by incorporating that input into the if elif else logic tree for the menu.

[M] I am going to need to build compositional relationships within Player class to implement character classes to each Player instance. Each ability will also need to be written as a class child of a greator Ability class. Then lastly, I will need to make a CharacterClassFactory to help with NPCs. We will Need to extend it to take into account the instances level at the time to give it the correct abilities that the classes level would have access to. Another layer would be to consider how NPCs will choose prepared spells later in game development.

[L] Use nodes to track map expansion. So as the player goes to areas and discovers them they will be tracked in a  tree and requested to be visualized later for reference or travel. Going to need to build out a map class.

[L] Add functionality for quest generation. Start small such as swapping the reward for a rand item on reward table or swapping enemy to be encountered or the total num of enemies in encounter.

[L] Create a dictionary with mad-lib type phrases that each type of commoner job might say. This could include information about other NPCs within town, comments on events (including events triggered by the player)

[L] Player Inventory UI currently displays as "1. Oats - 1" Where the second '1' is the monetary value of the oats. It looks like player has 1 oats. Should change to displayt either quantity or label it as '1 gp'

[L] Make a list of optional check types based on location of player. For example, location is 'cave' check_type_options = ['perception', 'investigation', etc.] Also can base this off of event type, or action type. For example event is 'dialogue' check_type_options = ['decpetion', 'persuasion', etc.]

[L] Improve roll_stats in dice_Roll file by allowing user to select which stats recieve which values as they are being rolled until all the stats are filled or chosen.

[L] Add Accessors and Mutators to each class.

[L] Correctly implement enchants to Melee_Items class




Bugs to fix:

[M] give_item function is not working properly, work around is to player.inventory.pop(item) this removes the whole key AND value. I want to be able to append/update the value and/or pop if the value reaches 0. This sounds do able with a while loop to check while player.inventory(item) == 0: player.inventory.pop(item)??

ROAD MAP:

    Core Game Mechanics:
        Combat System: Refine the combat mechanics and interactions, ensuring balanced gameplay. Consider integrating AI strategies for non-player characters (NPCs).
        Quest System: Expand the quest system (e.g., BanditQuest.py, quest.py) to include more complex, branching quests with multiple outcomes.

    Character Development:
        Character Classes: Enhance the character class system (char_class.py) by adding unique abilities and progression paths.
        Entities and NPCs: Further develop the entities (Entity.py) to include more detailed attributes and behaviors.

    Item and Inventory Management:
        Items: Continue to refine the item system (Item.py), possibly by adding item durability or special item effects.
        Trading System: Implement or improve the trading system (trade.py) to allow player interactions with NPC vendors and other players.

    World Building:
        Environment: Define more environments and locations that players can explore. Consider different environmental effects on gameplay.
        Mob Generation: Develop the mob generation system (buildMob.py) to dynamically create challenges for players.

    User Interface and Experience:
        Settings and Customization: Update the settings module (settings.py) to allow players more customization options for their gameplay experience.
        Feedback System: Implement a system to collect player feedback to continuously improve the game based on user experience.

    Technical Improvements:
        Code Refactoring: Regularly review and refactor the codebase to improve maintainability and performance.
        Testing and Debugging: Increase the focus on testing all modules extensively to ensure there are minimal bugs and issues.

    Documentation and Help System:
        Game Documentation: Create comprehensive documentation to help new players understand the game mechanics and controls.
        Developer Documentation: Maintain clear and detailed developer documentation to facilitate easier updates and expansions.

Major Change Log:

Integrated DijjonAlphaDevelopment folder with Git for ease of tracking progress. (win+x+i, then cd to alph dev folder, git status, git log git commit -m)

Refactoring player and npc creation to dedicated class files to be referenced in main. Expanded Classes and Races which have been refactored to core library 1/6/2024

[DONE] Find a way to enumerate race, class selection as is done in the menu functions. This way user may either input the name of the selection OR the enumeration corresponding with the selection. Both should be valid.

[DONE] I need to change attribute name convetion for "int" in Player class attributes. It is conflicting with int() function. - ZMD 4/22/2024

Integrated Repo with Github


STORY ARCH PLANS:

1. Branching Choices

Start with defining key decision points in your story where players can choose different paths. These decisions should impact the story significantly. Think about:

    Moral decisions: What ethical choices will players face? How will these choices affect their alignment or relationships with NPCs?
    Strategic decisions: Will they choose safety or risk for potentially greater rewards?
    Information-based decisions: Decisions that depend on the knowledge or secrets they have uncovered.

2. Consequences and Repercussions

Each choice should lead to a different outcome:

    Immediate consequences: Direct results of the player’s actions that are felt right away.
    Delayed consequences: Some choices might not impact the story until later, providing a surprise twist or a revisit to a seemingly minor decision made earlier.
    Subtle changes: Not all effects need to be dramatic; some can subtly alter dialogue, NPC behavior, or available quests.

3. Random Elements

Introduce randomness to keep the game unpredictable. This could be through:

    Random encounters: Depending on where and when they travel, different challenges or opportunities arise.
    Luck-based elements: Certain outcomes, especially in battles or when using magical items, could depend on a dice roll or similar mechanic.

4. Character Development and Relationships

Allow player decisions to impact their relationships with NPCs:

    Friendship, rivalry, or romance: Choices that affect emotional ties, potentially opening or closing quest lines.
    Reputation: How other characters perceive the player can change access to certain areas or alter NPC interactions.

5. Time-Sensitive Quests

Incorporate quests that only become available if the player visits locations at certain times or completes specific tasks within a time frame:

    Seasonal or time-based events: Quests that can only be accessed during certain in-game seasons or times of day.
    Missable quests: Opportunities that disappear if not acted upon quickly.

6. Tracking Past Choices

Use variables to track choices and their outcomes, which can influence later events:

    State tracking: Keep a log of decisions and states that NPCs or environments are in due to past actions.
    Dialogue changes: Alter NPC dialogues based on past interactions or known history.

7. Multiple Endings

Plan multiple endings based on the cumulative effect of the player’s decisions throughout the game. This can range from highly positive outcomes to tragic ones, depending on the paths chosen.
8. Feedback and Adaptation

Allow the game environment to reflect changes based on player actions:

    Environmental changes: Alter the game world visually or functionally based on the story progress, like a town rebuilding after an attack or wilderness growing over an abandoned site.
    NPC adaptations: NPCs could change their strategies or responses based on the player's reputation or past dealings.

By weaving these elements together, you can create a rich, dynamic story that rewards exploration and replayability, giving players a fresh experience each time they play. This not only makes your game more engaging but also encourages deeper emotional investment in the storyline and characters.