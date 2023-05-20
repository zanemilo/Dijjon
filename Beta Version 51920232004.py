import random

#var that stores the value of the last called variable in a new variable:
last_var = None

# Function to roll the character's stats
def roll_stats():
    rolls = [random.randint(1, 6) for i in range(4)]
    rolls.remove(min(rolls))
    return sum(rolls)

# dice roll functions
def roll_d4():
    return random.randint(1, 4)

def roll_d6():
    return random.randint(1, 6)

def roll_d8():
    return random.randint(1, 8)

def roll_d10():
    return random.randint(1, 10)

def roll_d12():
    return random.randint(1, 12)

def roll_d20():
    return random.randint(1, 20)

def spc_brk():
    print("")



# Base class for all characters
class Character:
    def __init__(self, name, race, char_class):
        self.name = name
        self.race = race
        self.char_class = char_class
    gold = 10
    arm_c = 10
    hp = 6
    spd = 30
    xp = 0
    lvl = 1

    def get_item(player, amount, item):
        print(f"{player.name} recieved {amount} {item}")

    def give_item(player, action, amount, item):
        print(f"{player.name} {action} {amount} {item}")

# Fighter class, subclass of Character
class Fighter(Character):
    def __init__(self, name, race):
        super().__init__(name, race, "Fighter")
        self.str = 2 + roll_stats()
        self.dex = 1 + roll_stats()
        self.con = 2 + roll_stats()
        self.int = 0 + roll_stats()
        self.wis = 0 + roll_stats()
        self.cha = 0 + roll_stats()
# Rogue class, subclass of Character
class Rogue(Character):
    def __init__(self, name, race):
        super().__init__(name, race, "Rogue")
        self.str = 1 + roll_stats()
        self.dex = 2 + roll_stats()
        self.con = 1 + roll_stats()
        self.int = 0 + roll_stats()
        self.wis = 0 + roll_stats()
        self.cha = 0 + roll_stats()
# Wizard class, subclass of Character
class Wizard(Character):
    def __init__(self, name, race):
        super().__init__(name, race, "Wizard")
        self.str = 0 + roll_stats()
        self.dex = 0 + roll_stats()
        self.con = 1 + roll_stats()
        self.int = 2 + roll_stats()
        self.wis = 2 + roll_stats()
        self.cha = 0 + roll_stats()

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
            print(f"Generating level {playerOne.level} quest for {playerOne.name}")


        elif playerOne.level == 2:
            print("LEVEL 2 DETECTED")
            print(f"Generating level {playerOne.level} quest for {playerOne.name}")


        else:
            print("LEVEL 3 or greator DETECTED")
            print(f"Generating level {playerOne.level} quest for {playerOne.name}")


        
        

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

    # creates function with a for loop to print a each of the classes dictionary items
    def class_List(self):
        for class_Array in self.classes:
            print(class_Array) 

    # creates function with a for loop to print a each of the races dictionary items
    def race_List(self):
        for race_Array in self.races:
            print(race_Array) 

    #checks if class name input is in the class list
    def get_valid_class(self):
        valid_class = False
        while not valid_class:
            class_name = input(f"Please choose your character's class {self.class_List()}: ")
            if class_name in self.classes:
                valid_class = True
            else:
                print(f"Invalid class name: {class_name}")
        return class_name
    
    #checks if race name input is in the race list
    def get_valid_race(self):
        valid_race = False
        while not valid_race:
            race_name = input(f"Choose your character's race {self.race_List()}: ")
            if race_name in self.races:
                valid_race = True
            else:
                print(f"Invalid race name: {race_name}")
        return race_name

    # method to prompt user for name, class choice and race choice
    def create_character(self):
        spc_brk()
        name = input("Enter your name: ")
        char_class = self.get_valid_class()
        race = self.get_valid_race()
        character_class = self.classes.get(char_class, None)
        if character_class is None:
            raise ValueError(f"Invalid class name: {char_class}")
        return character_class(name, race)

creator = CharacterCreator(None, None, None)

playerOne = creator.create_character()


def modifier(stat):
    (playerOne.stat - 10)/2
    return sum

def modifier(stat):
    return (stat - 10)/2


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
"Sword" : Item("Sword","A sword, a radiant emblem of timeless valor and ardent passion.",5,roll_d6(),"Slashing",False,None),
"Axe" : Item("Axe","An axe, a rugged embodiment of unyielding strength and untamed spirit.",8,roll_d8(),"Slashing",False,None),
"Spear" : Item("Spear","A spear, a poised extension of precision and swiftness.",6,roll_d6(),"Piercing",False,None),
"Dagger" : Item("Dagger","A dagger, a clandestine whisper in the night, wields both elegance and treachery.",4,roll_d4(),False,None),
"Fist" : Item("Fist","A fist, an embodiment of raw power",0,1,False,None),
"Hammer" : Item("Hammer","A hammer, a mighty embodiment of thunderous strength and unrelenting force",8,roll_d8(),False,None),

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

    print(f"""
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
""")


#Call playerOne character sheet function
spc_brk()
sheet()
spc_brk()
spc_brk()
spc_brk()
spc_brk()



# Print out the player's information
#print(playerOne.hp)
#print(f"Player Name: {playerOne.name}")
#print(f"Class: {playerOne.char_class}")
#print(f"Race: {playerOne.race}")
#print(f"Str: {playerOne.str}")
#print(f"Dex: {playerOne.dex}")
#print(f"Con: {playerOne.con}")
#print(f"Int: {playerOne.int}")
#print(f"Wis: {playerOne.wis}")
#print(f"Cha: {playerOne.cha}")

def resume():
    if last_var is not None:
        last_var()
        spc_brk()
    elif last_var is None:
        print("There was an unexpected error trying to return to the last menu")
        spc_brk()
        print("By default you will be returned to the Main Menu, aka 'start_menu()'")
        start_menu()
        spc_brk()

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
perception_Difficulty = 10 + roll_d4()

# rolls a check against the player's wis modifier to see if they can discover an inn nearby
def search_for_inn():
    if roll_d20() + modifier(playerOne.wis) >= perception_Difficulty:
        print("As you wander forth, your eyes eventually catch sight of a quaint inn nestled snugly amongst the area, beckoning you with its warm glow and welcoming atmosphere.")
        inn_menu()
        spc_brk()
    else:
        print("After an extended amount of searching you are unable to find an Inn nearby...")
        start_menu()
        spc_brk()

# Start menu function
def start_menu():
    #indicate global variable outside function
    global last_var
    
    # Display the menu options
    print("1. Resume\n2. Player Stats\n3. Find an Inn\n4. Quit")
    
    # Get the player's choice
    choice = input("Input the number of your selection: ")
    spc_brk()
    
    # Handle the player's choice
    if choice == "1":
        if last_var is not None:
            resume()
            spc_brk()
        elif last_var is None:
            print("You have yet to embark on a journey. Please select a valid option.")
            spc_brk()
            start_menu()
            spc_brk()
    elif choice == "2":
        sheet()
        spc_brk()
        start_menu()    
    elif choice == "3":
        search_for_inn()
        last_var = start_menu()
        spc_brk()
    elif choice == "4":
        quit()
    else:
        print("Invalid choice. Please try again: ")
        start_menu()
        spc_brk()

# defines rent a room function for future implementation
def rent_a_room():
    global last_var
    print("You rent a room for the rest of the day...")
    spc_brk()
    last_var()


# starts order function using an item list as an arguement
def order(item_list):
    spc_brk()
    print("Buy:")
    spc_brk()
    for i, (name, item) in enumerate(item_list.items()):
        print(f"{i+1}. {item.name} - {item.val} gp")
    spc_brk()
    choice = input("What would you like to purchase? ")
    # while loop checks if input is digit or integer that is in the range of enumerated item_list options
    while not choice.isdigit() or int(choice) not in range(1, len(item_list)+1):
        print("Invalid choice. Please select a valid option. ")
        spc_brk()
        order(item_list)
    chosen_item = list(item_list.values())[int(choice)-1]
    if has_gold_check(chosen_item.val) == True:
        playerOne.gold -= chosen_item.val
        print(f"You have purchased {chosen_item.name} for {chosen_item.val} gold.\nNew Gp Total: {playerOne.gold}")
        return chosen_item
    else:
        print(f"You do not have enough gp to purchase {chosen_item.name}")
        order(item_list)
        
# rat quest TBC
def quest_menu1():
    spc_brk()
    print(f"Too Be Continued...")
    quit()
    
# Inn menu function
def inn_menu():
    spc_brk()
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
        last_var = inn_menu()
        rent_a_room()
    elif choice == "3":
        if rumors_selected_prev == True:
            print("You listen to the lively chatter of the inn, but don't hear any new rumors.")
        else:
            print("You spend the next hours or so easedropping and conversing with patrons. ")
            print("Three conversations, an arguement about local politics and small talk about the rise in cost of hay leads you to a meet a rough looking man. ")
            print("The rough looking man explains his concern for the inn and how the rat infestation has gotten out of hand. He was hired to extreminate them himself but he has an irrational fear of basements. ")
            print("He gives you half of the payment upfront")
            spc_brk()
            playerOne.gold += 10
            spc_brk()
            print(f"{playerOne.name}'s Gold Total: {playerOne.gold}")
            spc_brk()
            rumors_selected_prev = True
            stats["GP"] = playerOne.gold
            quest_menu1() # requires new menu func
    elif choice == "4":
        start_menu() # requires new menu func
    else:
        print("Invalid choice. Please try again: ")
        inn_menu()


start_menu()


