import Player
import char_class as c

class CharacterCreator(Player):

    races = {
        "Human": "Human",
        "Elf": "Elf",
        "Dwarf": "Dwarf",
    }

    classes = {
        "Fighter": c.Fighter,
        "Rogue": c.Rogue,
        "Wizard": c.Wizard,
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