# Dijjon character class Class
# Developed & designed by: Zane M Deso
# Purpose: This is supposed to emulate the class/job that a player or NPC or enemy can have. It still needs to be implemented fully.

import Player
import dice_Roll

class Fighter(Player):
    """Fighter class, subclass of Player"""
    def __init__(self, name, race):
        super().__init__(name, race, "Fighter")
        self.str = 2 + dice_Roll.roll_stats()
        self.dex = 1 + dice_Roll.roll_stats()
        self.con = 2 + dice_Roll.roll_stats()
        self.int = 0 + dice_Roll.roll_stats()
        self.wis = 0 + dice_Roll.roll_stats()
        self.cha = 0 + dice_Roll.roll_stats()
    # FIX ME: Requires accessors and mutators

class Rogue(Player):
    """Rogue class, subclass of Player"""
    def __init__(self, name, race):
        super().__init__(name, race, "Rogue")
        self.str = 1 + dice_Roll.roll_stats()
        self.dex = 2 + dice_Roll.roll_stats()
        self.con = 1 + dice_Roll.roll_stats()
        self.int = 0 + dice_Roll.roll_stats()
        self.wis = 0 + dice_Roll.roll_stats()
        self.cha = 0 + dice_Roll.roll_stats()
        # FIX ME: Requires accessors and mutators

class Wizard(Player):
    """Wizard class, subclass of Player"""
    def __init__(self, name, race):
        super().__init__(name, race, "Wizard")
        self.str = 0 + dice_Roll.roll_stats()
        self.dex = 0 + dice_Roll.roll_stats()
        self.con = 1 + dice_Roll.roll_stats()
        self.int = 2 + dice_Roll.roll_stats()
        self.wis = 2 + dice_Roll.roll_stats()
        self.cha = 0 + dice_Roll.roll_stats()
        # FIX ME: Requires accessors and mutators