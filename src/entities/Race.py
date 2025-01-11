# Race
# Author: Zane M Deso
# Purpose: Handle race logic for entities in the game, including racial traits, resistances, and base dispositions.

import sys
sys.path.append("..")  # Adds the parent directory to the Python module search path
from systems.core_library import race_stats

class Race:
    """
    Compositional Race Class layers over entities/players.
    Aids in keeping track of each entity's racial traits and modifiers.
    """

    def __init__(self, race, abilities=[], skills=[], feats=[], spells=[], resistances={}, proficiencies=[], movement=30, visibility=None, disposition={}):
        self.race = race
        self.abilities = self.get_stat('abilities', race)
        self.skills = self.get_stat('skills', race)
        self.feats = self.get_stat('feats', race)
        self.spells = self.get_stat('spells', race)
        self.resistances = self.get_stat('resistances', race)
        self.proficiencies = self.get_stat('proficiencies', race)
        self.movement = self.get_stat('movement', race)
        self.visibility = self.get_stat('visibility', race)
        self.disposition = self.get_stat('disposition', race)

    def get_stat(self, stat: str, race: str):
        """Returns race-specific attributes given params."""
        if race in race_stats:
            return race_stats[race].get(stat, None)  # Returns None if the stat is not defined

# test_race = Race('Humara')

# print(f"Race: {test_race.race}\nAbilities: {test_race.abilities}\nSkills: {test_race.skills}\nResistances: {test_race.resistances}")
# print(f"Movement: {test_race.movement}\nVisibility: {test_race.visibility}\nDisposition: {test_race.disposition}")
