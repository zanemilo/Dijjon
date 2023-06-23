import random
import buildMob
import dice_Roll

#var that stores the value of the last called variable in a new variable:
last_var = None


# Base class for all characters
#think about storing info into dictionary with corresponding key : value
class Character:
    def __init__(self, name, race, char_class):
        self.name = name
        self.race = race
        self.char_class = char_class
    gold = 10
    arm_c = 10
    hp = 6
    hpMax = 6
    spd = 30
    xp = 0
    lvl = 1

    inventory = {}

    def get_item(player, amount, item):
        player.inventory[item] = amount
        print(f"{player.name} recieved {amount} {item}!\n")
        #add, append the item and amount into the player.inventory
    def give_item(player, action, amount, item):
        if item not in player.inventory:
            print('You do not have enough', item, f'to {action}!\n')
        elif player.inventory[item] < amount or player.inventory[item] == 0:
            print('You do not have enough', item, f'to {action}!\n')
        else:
            player.inventory.pop(item) #this should fix the bug of keeping item in inv but removes all not some
            #player.inventory[item] -= amount 
            print(f"{player.name} {action} {amount} {item}\n")
    def show_inventory(player):
        num = 1
        for item in player.inventory:
            print(f'{num}. {item} - {player.inventory[item]}') # item would be the name (key), player.inventory[item] would be the corresponding value
            num += 1

        # Fighter class, subclass of Character
class Fighter(Character):
    def __init__(self, name, race):
        super().__init__(name, race, "Fighter")
        self.str = 2 + dice_Roll.roll_stats()
        self.dex = 1 + dice_Roll.roll_stats()
        self.con = 2 + dice_Roll.roll_stats()
        self.int = 0 + dice_Roll.roll_stats()
        self.wis = 0 + dice_Roll.roll_stats()
        self.cha = 0 + dice_Roll.roll_stats()
# Rogue class, subclass of Character
class Rogue(Character):
    def __init__(self, name, race):
        super().__init__(name, race, "Rogue")
        self.str = 1 + dice_Roll.roll_stats()
        self.dex = 2 + dice_Roll.roll_stats()
        self.con = 1 + dice_Roll.roll_stats()
        self.int = 0 + dice_Roll.roll_stats()
        self.wis = 0 + dice_Roll.roll_stats()
        self.cha = 0 + dice_Roll.roll_stats()
# Wizard class, subclass of Character
class Wizard(Character):
    def __init__(self, name, race):
        super().__init__(name, race, "Wizard")
        self.str = 0 + dice_Roll.roll_stats()
        self.dex = 0 + dice_Roll.roll_stats()
        self.con = 1 + dice_Roll.roll_stats()
        self.int = 2 + dice_Roll.roll_stats()
        self.wis = 2 + dice_Roll.roll_stats()
        self.cha = 0 + dice_Roll.roll_stats()

# Item class: think template for items in game
class Item():
    def __init__(self, name, desc, val):
        self.name = name
        self.desc = desc
        self.val = val

class Melee_Item(Item):
    def __init__(self, name, desc, val, damage, damage_type, poisoned, enchant):
        super().__init__(name, desc, val)
        self.damage = damage
        self.damage_type = damage_type
        self.poisoned = poisoned
        self.enchant = enchant


class Quest():
    def __init__(self, name, objectives, reward, completion_status):
        self.name = name
        self.objectives = objectives
        self.reward = reward
        self.completion_status = completion_status

    def create_quest():  #Quest Generation: Create a function that generates quests based on certain criteria, such as the player's level, location, and faction affiliation. This function can randomly select a quest template from a pool of pre-defined quests and fill in the details based on the criteria.
        if playerOne.level == 1:
            print("LEVEL 1 DETECTED")
            print(f"Generating level {playerOne.level} quest for {playerOne.name}\n")


        elif playerOne.level == 2:
            print("LEVEL 2 DETECTED")
            print(f"Generating level {playerOne.level} quest for {playerOne.name}\n")


        else:
            print("LEVEL 3 or greator DETECTED")
            print(f"Generating level {playerOne.level} quest for {playerOne.name}\n")


        
        

class CharacterCreator(Character):

    races = {
        "Human": "Human",
        "Elf": "Elf",
        "Dwarf": "Dwarf",
    }

    classes = {
        "Fighter": Fighter,
        "Rogue": Rogue,
        "Wizard": Wizard,
    }

    # creates function with a for loop to print each of the classes dictionary items
    def class_List(self):
        num = 1
        for class_Array in self.classes:
            print(f'{num}. {class_Array}')
            num += 1

    # creates function with a for loop to print a each of the races dictionary items
    def race_List(self):
        num = 1
        for race_Array in self.races:
            print(f'{num}. {race_Array}')
            num += 1

    #checks if class name input is in the class list
    def get_valid_class(self):
        valid_class = False
        while not valid_class:
            self.class_List()
            class_name = input(f"Please choose your character's class: \n")
            class_name = class_name.title()
            if class_name in self.classes:
                valid_class = True
            else:
                print(f"Invalid class name: {class_name}\n")
        return class_name
    
    #checks if race name input is in the race list
    def get_valid_race(self):
        valid_race = False
        while not valid_race:
            self.race_List()
            race_name = input(f"Choose your character's race:\n")
            race_name = race_name.title()
            if race_name in self.races:
                valid_race = True
            else:
                print(f"Invalid race name: {race_name}\n")
        return race_name

    # method to prompt user for name then resaves the input to title case
    # class choice and race choice
    def create_character(self):
         
        name = input("Enter your name:\n")
        name = name.title()
        print('Name Stored as:',name, '\n')
        char_class = self.get_valid_class()
        race = self.get_valid_race()
        character_class = self.classes.get(char_class, None)
        if character_class is None:
            raise ValueError(f"Invalid class name: {char_class}\n")
        return character_class(name, race)

creator = CharacterCreator(None, None, None)

playerOne = creator.create_character()


     

def modifier(stat):
    return (int((stat - 10)/2))


#creates instance of Items class name, description and value as arguments
inn_items = {
"Oats" : Item("Oats","As you observe the oats, their small and unassuming appearance belies the nourishing and hearty sustenance they provide, a testament to the adage that good things come in small packages.",1),
"Bread" : Item("Bread","As the aroma of freshly baked inn bread wafts towards you, its unpretentious and humble exterior masks the warm, comforting sustenance it promises, a tribute to the saying that true beauty lies in simplicity.",2),
"Pie" : Item("Pie","As your eyes settle on the apple pie, the aroma of freshly baked cinnamon and butter wafts towards you, enticing your taste buds with the promise of a warm and flaky crust enveloping sweet and tangy apples, a quintessential treat that evokes memories of home and comfort.",3),
"Ale" : Item("Ale","The inn's modest ale is a simple yet satisfying drink, with a smooth taste that lingers on the tongue.",1),
"Milk" : Item("Milk","As you obtain a glass of milk, the creamy white liquid provides a soothing and wholesome taste, evoking a sense of comfort and simplicity.",2),
"Water Mug" : Item("Water Mug","The clear and unremarkable appearance of the water in the mug was a refreshing contrast to the chaos of the world around it.",0),


}


#creates instance of Items class with self, name, desc, val, damage, damage_type, poisoned, enchant as arguments
melee_items = {
"Sword" : Melee_Item("Sword","A sword, a radiant emblem of timeless valor and ardent passion.",5,dice_Roll.roll_d6(),"Slashing",False,None),
"Axe" : Melee_Item("Axe","An axe, a rugged embodiment of unyielding strength and untamed spirit.",8,dice_Roll.roll_d8(),"Slashing",False,None),
"Spear" : Melee_Item("Spear","A spear, a poised extension of precision and swiftness.",6,dice_Roll.roll_d6(),"Piercing",False,None),
"Dagger" : Melee_Item("Dagger","A dagger, a clandestine whisper in the night, wields both elegance and treachery.",4,dice_Roll.roll_d4(),"Piercing",False,None),
"Fist" : Melee_Item("Fist","A fist, an embodiment of raw power",0,1,"Blunt",False,None),
"Hammer" : Melee_Item("Hammer","A hammer, a mighty embodiment of thunderous strength and unrelenting force",8,dice_Roll.roll_d8(),"Blunt",False,None),

}


#dictionary of playerOne instance's stats used for sheet to pull updated info
stats = {
    "STR": playerOne.str,
    "DEX": playerOne.dex,
    "CON": playerOne.con,
    "INT": playerOne.int,
    "WIS": playerOne.wis,
    "CHA": playerOne.cha,
    "HP": playerOne.hp,
    "AC": playerOne.arm_c,
    "GP": playerOne.gold,
    "SPD": playerOne.spd,
    "LEVEL": playerOne.lvl,
    "XP" : playerOne.xp,
}

 # Generate and display the character sheet
def sheet(): 
    stats["STR"] = playerOne.str
    stats["DEX"] = playerOne.dex
    stats["CON"] = playerOne.con
    stats["INT"] = playerOne.int
    stats["WIS"] = playerOne.wis
    stats["CHA"] = playerOne.cha
    stats["HP"] = playerOne.hp
    stats["AC"] = playerOne.arm_c
    stats["GP"] = playerOne.gold
    stats["SPD"] = playerOne.spd
    stats["LEVEL"] = playerOne.lvl
    stats["XP"] = playerOne.xp

    print(f"""\n
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
| NAME: {playerOne.name.upper().center(39)}   |
| RACE: {playerOne.race.upper().center(39)}   |
| CLASS: {playerOne.char_class.upper().center(38)}   |
| LEVEL: {stats['LEVEL']}{' '*(2-len(str(stats['LEVEL'])))}                                       |
|                                                 |
| STR: {stats['STR']}{' '*(2-len(str(stats['STR'])))} | DEX: {stats['DEX']}{' '*(2-len(str(stats['DEX'])))} | CON: {stats['CON']}{' '*(2-len(str(stats['CON'])))} | INT: {stats['INT']}{' '*(2-len(str(stats['INT'])))} | WIS: {stats['WIS']}{' '*(2-len(str(stats['WIS'])))} | 
| CHA: {stats['CHA']}{' '*(2-len(str(stats['CHA'])))} |                                       |
| ARMOR CLASS: {stats['AC']}{' '*(2-len(str(stats['AC'])))} | SPEED: {stats['SPD']}{' '*(2-len(str(stats['SPD'])))}                     |
|                                                 |
| HIT POINTS: {stats['HP']}{' '*(2-len(str(stats['HP'])))} | SPELL SLOTS: {'0'+' '*(2-len('2'))}                |
|                                                 |
| GOLD: {stats['GP']}{' '*(2-len(str(stats['GP'])))} | XP: {stats['XP']}{' '*(2-len(str(stats['XP'])))}                               |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
\n\n\n\n""")


#Call playerOne character sheet function
sheet()


def resume():
    if last_var is not None:
        last_var()
    elif last_var is None:
        print(f"\nThere was an unexpected error trying to return to the last menu\n")
        print(f"\nBy default you will be returned to the Main Menu, aka 'start_menu()'\n")
        start_menu()

# set placeholder value for item check var used in has_gold_check() function
item_cost = 0

# function called to check if the player has sufficient gold to pay for an item/service/interaction
def has_gold_check(item_cost):
    if playerOne.gold >= item_cost:
        item_cost = 0
        return True
    else:
        item_cost = 0
        return False



# updatable var for perception difficulty. Determines if player will find something. consider adding a difficulty function to make this adjustable from one place later on
perception_Difficulty = 10 + dice_Roll.roll_d4()

# rolls a check against the player's wis modifier to see if they can discover an inn nearby
# idea for future, create instead a 'search' function that can use 'inn','cave',etc. as an argument
# def search_for(thing):
#   if dice_Roll.roll_d20() + modifier(playerOne.wis) >= perception_Difficulty:

def search_for_inn():
    answer = dice_Roll.roll_d20() + modifier(playerOne.wis) 
    print(f'You rolled:',answer, 'and needed atleast:',perception_Difficulty, 'to succeed the check!\n')
    if answer >= perception_Difficulty:
        print("As you wander forth, your eyes eventually catch sight of a quaint inn nestled snugly amongst the area, beckoning you with its warm glow and welcoming atmosphere.\n")
        inn_menu()
    else:
        print(f"\nAfter an extended amount of searching you are unable to find an Inn nearby...\n")
        start_menu()

# Start menu function
def start_menu():
    #indicate global variable outside function
    global last_var
    
    if last_var is None:
        print(f"\n1. R̶e̶s̶u̶m̶e\n2. Player Stats\n3. Find an Inn\n4. Quit\n5. Get Sword\n6. Give Sword\n7. Inventory\n8. Damage(1-3)\n")
    else:
        # Display the menu options
        print(f"\n1. Resume\n2. Player Stats\n3. Find an Inn\n4. Quit\n5. Get Sword\n6. Give Sword\n7. Inventory\n8. Damage(1-3)\n")
    
    # Get the player's choice
    choice = input(f"\nInput the number of your selection: \n")
    
    # Handle the player's choice
    if choice == "1":
        if last_var is not None:
            resume()
        elif last_var is None:
            print(f"\nYou have yet to embark on a journey. Please select a valid option.\n")
            start_menu()
    elif choice == "2":
        sheet()
        start_menu()    
    elif choice == "3":
        search_for_inn()
        last_var = start_menu()
    elif choice == "4":
        quit()
    elif choice == "5":
        playerOne.get_item(1, 'Sword')
        start_menu()
    elif choice == "6":
        playerOne.give_item('gave away', 1, 'Sword')
        start_menu()
    elif choice == "7":
        playerOne.show_inventory()
        start_menu()
    elif choice == "8":
        damage = random.randint(1,3)
        playerOne.hp -= damage
        print(f"{playerOne.name} takes {damage}!\n",f"{playerOne.name}'s HP: {playerOne.hp}/{playerOne.hpMax}\n")
        start_menu()    
    else:
        print(f"\nInvalid choice. Please try again: \n")
        start_menu()

# defines rent a room function, needs to be tested to see if hp is restored properly
def rent_a_room():
    print("rent_a_room() function start")
    print(f"\nYou rent a room for the rest of the day...\n")
    if playerOne.hp < playerOne.hpMax:
        playerOne.hp = playerOne.hpMax
        print('Hp restored to\n')
        print(playerOne.hp)
    # global last_var
    # last_var()
    print("rent_a_room() function end")


# starts order(think salesperson) function using an item list as an arguement
def order(item_list):
    global last_var

    print(f"Buy:\n\nYour GP: {playerOne.gold}")

    for i, (name, item) in enumerate(item_list.items()):
        print(f"{i+1}. {item.name} - {item.val} gp")

    choice = input("What would you like to purchase?\n")
    # while loop checks if input is digit or integer that is in the range of enumerated item_list options
    while not choice.isdigit() or int(choice) not in range(1, len(item_list)+1):
        invalid_choice = input(f"Invalid choice. Please select a valid option. \nWould you like to leave?\nInput the number of your choice\n\n1. Yes\n2. No")

        if int(invalid_choice()) == 1:
            last_var()
        elif int(invalid_choice()) == 2:
            order(item_list)
        else:
            print(f"\nInvalid input. Returning to last screen and returning input as error to logs.\n")
            order(item_list)
        order(item_list)
    chosen_item = list(item_list.values())[int(choice)-1]
    if has_gold_check(chosen_item.val) == True:
        playerOne.gold -= chosen_item.val
        print(f"You have purchased {chosen_item.name} for {chosen_item.val} gold.")
        temp_dict1 = {chosen_item.name : chosen_item.val}
        playerOne.inventory.update(temp_dict1) # this would overwrite the value
        #playerOne.inventory.update(name=f'{chosen_item.name}')# not working as intended, might need to simplify or refactor this code
        temp_dict1.pop(chosen_item.name) # deletes temp_dict1 key and value
        #print(temp_dict1, "\n")
        print(playerOne.inventory, "\n")
    else:
        print(f"You do not have enough gp to purchase {chosen_item.name}")
        order(item_list)
        
# rat quest TBC
def quest_menu1():
    print(f"\nToo Be Continued...\n")
    quit()
    
# Inn menu function
def inn_menu():

    global last_var
    rumors_selected_prev = False
    
    # Display the menu options
    print("1. Order food and drink\n2. Rent a room\n3. Listen for rumors\n4. Leave the inn")
    
    # Get the player's choice
    choice = input("What would you like to do? ")
    
    # Handle the player's choice
    if choice == "1":
        order(inn_items)
        inn_menu()  
    elif choice == "2":
        print(f"\nchoice == 2 start\n")
        last_var = inn_menu
        print(f"last_var set to inn_menu()")
        rent_a_room()
        print(f"\nchoice == 2 end\nAttempting to execute last_var...\n")
        last_var()
    elif choice == "3":
        if rumors_selected_prev == True:
            print("You listen to the lively chatter of the inn, but don't hear any new rumors.\n")
        else:
            print("You spend the next hours or so easedropping and conversing with patrons.\n ")
            print("Three conversations, an arguement about local politics and small talk about the rise in cost of hay leads you to a meet a rough looking man.\n ")
            print("The rough looking man explains his concern for the inn and how the rat infestation has gotten out of hand. He was hired to extreminate them himself but he has an irrational fear of basements.\n")
            print("He gives you half of the payment upfront\n")

            #refactor this section using the class functions for get/ give
            playerOne.gold += 10
            print(f"{playerOne.name}'s Gold Total: {playerOne.gold}\n")
            rumors_selected_prev = True
            stats["GP"] = playerOne.gold
            quest_menu1() # requires new menu func
    elif choice == "4":
        start_menu() # requires new menu func
    else:
        print(f"\nInvalid choice. Returning to Inn Menu \n")
        inn_menu()

print(f"\nEnd of code reach... returning to Main Menu aka 'start_menu()'\n")
start_menu()


