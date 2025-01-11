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
        self.abilities = abilities
        self.skills = skills
        self.feats = feats
        self.spells = spells
        self.proficiencies = proficiencies
        self.resource_points = resource_points
        
        self.str = self.get_attr('str', char_class)
        self.dex = self.get_attr('dex', char_class)
        self.con = self.get_attr('con', char_class)
        self.intel = self.get_attr('int', char_class)
        self.wis = self.get_attr('wis', char_class)
        self.cha = self.get_attr('cha', char_class)

    def get_attr(self, attr : str, char_class : str):
        """Returns character classes attributes given params."""
        if char_class in class_stats:
            return class_stats[char_class][attr]
    
test = CharClass('Psion')

print(f"{test.str},{test.dex},{test.con},{test.intel},{test.wis},{test.cha}\n{test.abilities}\n{test.skills}\n{test.proficiencies}")