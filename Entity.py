# Dijjon Player Class
# Developed & designed by: Zane M Deso
# Purpose: Used to handle player creation, stats, attributes, status effect, and other associated player centered functions




class Entity:
    """
    A base class for all entities in the game, such as players, NPCs, and mobs.
    It encapsulates common attributes and functionalities.
    """
    def __init__(self, name, hp, arm_c, spd, xp, lvl):
        self.name = name
        self.hp = hp
        self.arm_c = arm_c
        self.spd = spd
        self.xp = xp
        self.lvl = lvl
        self.status_effects = {}  # Track status effects like 'poisoned', 'stunned', etc.

    def get_name(self):
        """Returns the name of the entity."""
        return self.name
    
    def set_name(self, name):
        """Sets the name of the entity."""
        self.name = name

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

# Example of creating an Entity and manipulating its properties
entity = Entity("Test Entity", 100, 15, 30, 200, 5)
entity.display_info()
entity.modify_hp(-20)  # Entity takes 20 damage
entity.add_status_effect("poisoned", 3)
entity.update_status_effects()  # Updates the status effects
entity.display_info()
