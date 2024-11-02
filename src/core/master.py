# Dijjon master Class
# Developed & designed by: Zane M Deso
# Purpose: This class is the main driver and will be the DM in a sense when it comes to making choices behind the scenes.



import random as r  


class Master:
    """
    Master Class for managing actions and decisions typically handled by a Dungeon Master (DM) 
    in the overarching gameplay and story. This class facilitates character creation, validations, 
    checks, and combat simulations.
    """

    def sheet(self, character):  # passed testing in new main
        """
        Generate and display the character sheet for a given character.

        Args:
            character (Player): The player character for whom the sheet is being generated.
        """
        # Dictionary of character instance's stats used for sheet to pull updated info
        stats = {
            "STR": character.str,
            "DEX": character.dex,
            "CON": character.con,
            "INT": character.intel,
            "WIS": character.wis,
            "CHA": character.cha,
            "HP": character.hp,
            "AC": character.arm_c,
            "GP": character.gold,
            "SPD": character.spd,
            "LEVEL": character.lvl,
            "XP": character.xp,
        }

        # This may be redundant, will need to test
        # EDIT: This is absolutely redundant, will replace sheet function ahead.
        stats["STR"] = character.str
        stats["DEX"] = character.dex
        stats["CON"] = character.con
        stats["INT"] = character.intel
        stats["WIS"] = character.wis
        stats["CHA"] = character.cha
        stats["HP"] = character.hp
        stats["AC"] = character.arm_c
        stats["GP"] = character.gold
        stats["SPD"] = character.spd
        stats["LEVEL"] = character.lvl
        stats["XP"] = character.xp

        # Display the character sheet with formatted statistics
        print(f"""\n
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        | NAME: {character.name.upper().center(39)}   |
        | RACE: {character.race.upper().center(39)}   |
        | CLASS: {character.char_class.upper().center(38)}   |
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


    def get_name(self):  # passed testing in new main
        """
        Prompt the user to enter a name for their character.

        Returns:
            str: The name entered by the user, properly formatted.
        """
        name = input("Enter your name:\n")  # Prompt user for character name
        return name.title()  # Capitalize the first letter of each word in the name


    # def create_character(self):  # Pending Deprecation
    #     """
    #     Prompt the user for all necessary information to create a new Player character.

    #     This includes name, class, and race. The function validates the inputs and 
    #     constructs a Player instance based on the provided information.

    #     Returns:
    #         Player: The newly created Player instance with the specified attributes.
    #     """
    #     name = input("Enter your name:\n")  # Prompt user for character name
    #     name = name.title()  # Capitalize the first letter of each word in the name

    #     char_class = self.get_valid_class()  # Get a valid class from the user

    #     race = self.get_valid_race()  # Get a valid race from the user
    
    #     player = p(name, race, char_class)  # Create a Player instance with the provided name, race, and class
    #     return player  # Return the created Player instance

    def opposing_check(self, entity_one, enitity_two, check_type):  # passed testing in new main
        """
        Conduct a check between two opposing Player instances based on a specific check type.

        Args:
            entity_one (Player): The first player entity.
            enitity_two (Player): The second player entity.
            check_type (str): The type of check to perform (e.g., 'strength', 'dexterity').

        Returns:
            str: The name of the entity that wins the check.
        """
        # Perform a check for entity one using their roll for the specified check type
        e_one_roll = self.check(check_type, entity_one.player_check_roll(check_type))  # FIX ME: To adjust this once I have used inheritance correctly,
        # Perform a check for entity two using their roll for the specified check type
        e_two_roll = self.check(check_type, enitity_two.player_check_roll(check_type))  # just use the check_roll method associated from the parent class

        if e_one_roll < e_two_roll:
            return enitity_two.get_name()  # Return entity two's name if they win the check
        elif e_two_roll < e_one_roll:
            return entity_one.get_name()  # Return entity one's name if they win the check
        elif e_one_roll == e_two_roll:
            return self.opposing_check(entity_one, enitity_two, check_type)  # Repeat the check in case of a tie




