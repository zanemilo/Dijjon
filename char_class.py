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