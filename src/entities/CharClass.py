# CharClass
# Author: Zane M Deso
# Purpose: Handle class logic for entities in game essentially allowing layered classes for npcs, player in the future.
import sys
sys.path.append("..")  # Adds the parent directory to the Python module search path
from systems.core_library import class_stats

class CharClass:
    """
    Compositional Character Class layers over entities/players.
    Aids in keeping track of each entities class info.
    """

    def __init__(self, char_class, level=1, abilities=[], skills=[], feats=[], spells=[], proficiencies=[], resource_points=0):
        self.char_class = char_class
        self.level = level
        self.abilities = self.get_stat('abilities', char_class)
        self.skills = self.get_stat('skills', char_class)
        self.feats = self.get_stat('feats', char_class)
        self.spells = self.get_stat('spells', char_class)
        self.proficiencies = self.get_stat('proficiencies', char_class)
        self.resource_points = self.get_stat('resource_points', char_class)
        
        self.str = self.get_stat('str', char_class)
        self.dex = self.get_stat('dex', char_class)
        self.con = self.get_stat('con', char_class)
        self.intel = self.get_stat('int', char_class)
        self.wis = self.get_stat('wis', char_class)
        self.cha = self.get_stat('cha', char_class)

    def get_stat(self, stat : str, char_class : str):
        """Returns character classes attributes given params."""
        if char_class in class_stats:
            return class_stats[char_class][stat]
    
test = CharClass('Psion')

print(f"{test.str},{test.dex},{test.con},{test.intel},{test.wis},{test.cha}\n{test.abilities}\n{test.skills}\n{test.proficiencies}")