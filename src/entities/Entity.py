# Dijjon Player Class
# Developed & designed by: Zane M Deso
# Purpose: Used to handle player creation, stats, attributes, status effect, and other associated player centered functions


class Entity:
    """
    A base class for all entities in the game, such as players, NPCs, and mobs.
    It encapsulates common attributes and functionalities.
    """
    def __init__(self, name, hp, arm_c, spd, xp, lvl, is_enemy = False):
        """
        Initialize a new instance of the Entity class.
        
        :param name: str - The name of the entity.
        :param hp: int - Health points of the entity, determining how much damage it can take before being defeated.
        :param arm_c: int - Armor class of the entity, contributing to its defense against attacks.
        :param spd: int - Speed of the entity, affecting its turn order in combat.
        :param xp: int - Experience points of the entity, used for leveling up.
        :param lvl: int - Current level of the entity, affecting its overall strength and abilities.
        """
        self.name = name
        self.hp = hp
        self.arm_c = arm_c
        self.spd = spd
        self.xp = xp
        self.lvl = lvl
        self.is_enemy = is_enemy  # Used to designate other NPCs as enemies, for use in combat.py
        self.status_effects = {}  # Track status effects like 'poisoned', 'stunned', etc.

    def get_name(self):
        """Returns the name of the entity."""
        return self.name
    
    def set_name(self, name):
        """Sets the name of the entity."""
        self.name = name

    def init_name():  # passed testing in new main
        """
        Prompt the user to enter a name for their character.

        Returns:
            str: The name entered by the user, properly formatted.
        """
        name = input("Enter your name:\n")  # Prompt user for character name
        return name.title()  # Capitalize the first letter of each word in the name

    def get_hp(self):
        """Returns the current hit points of the entity."""
        return self.hp
    
    def set_hp(self, hp):
        """Sets the current hit points of the entity."""
        if hp < 0:
            hp = 0  # Ensure HP does not go below 0
        self.hp = hp

    def modify_hp(self, amount):
        """Modifies the current hit points by a specified amount."""
        self.set_hp(self.hp + amount)
        if amount >= 0:
            print(f"{self.name} gains {amount} HP.")
        else:
            print(f"{self.name} takes {abs(amount)} damage.")

    def is_alive(self):
        """Checks if the entity is alive."""
        return self.hp > 0

    def add_status_effect(self, effect, duration):
        """Adds a status effect to the entity."""
        self.status_effects[effect] = duration
        print(f"{self.name} is now {effect} for {duration} turns.")

    def remove_status_effect(self, effect):
        """Removes a status effect from the entity."""
        if effect in self.status_effects:
            del self.status_effects[effect]
            print(f"{self.name} is no longer {effect}.")

    def update_status_effects(self):
        """Updates the status effects, reducing the duration by 1."""
        expired_effects = []
        for effect, duration in self.status_effects.items():
            self.status_effects[effect] = duration - 1
            if self.status_effects[effect] <= 0:
                expired_effects.append(effect)
        
        for effect in expired_effects:
            self.remove_status_effect(effect)

    def display_info(self):
        """Displays basic information about the entity."""
        print(f"Name: {self.name}, HP: {self.hp}, Armor Class: {self.arm_c}, Speed: {self.spd}, XP: {self.xp}, Level: {self.lvl}")
        if self.status_effects:
            print(f"Status Effects: {', '.join([f'{effect} ({duration} turns)' for effect, duration in self.status_effects.items()])}")
        else:
            print("Status Effects: None")
    
    def sheet(self):  # passed testing in new main
        """
        Generate and display the character sheet for a given character.

        Args:
            character (Player): The player character for whom the sheet is being generated.
        """
        # Dictionary of character instance's stats used for sheet to pull updated info
        stats = {
            "STR": self.str,
            "DEX": self.dex,
            "CON": self.con,
            "INT": self.intel,
            "WIS": self.wis,
            "CHA": self.cha,
            "HP": self.hp,
            "AC": self.arm_c,
            "GP": self.gold,
            "SPD": self.spd,
            "LEVEL": self.lvl,
            "XP": self.xp,
        }

        # Display the character sheet with formatted statistics
        print(f"""\n
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        | NAME: {self.name.upper().center(39)}   |
        | RACE: {self.race.upper().center(39)}   |
        | CLASS: {self.char_class.upper().center(38)}   |
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

# Example of creating an Entity and manipulating its properties
# entity = Entity("Test Entity", 100, 15, 30, 200, 5)
# entity.display_info()
# entity.modify_hp(-20)  # Entity takes 20 damage
# entity.add_status_effect("poisoned", 3)
# entity.update_status_effects()  # Updates the status effects
# entity.display_info()
