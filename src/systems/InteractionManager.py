
# File: InteractionManager
# Author: Zane Deso
# Handles skill and opposed checks between entities using game settings and random bias.

import random
from typing import Optional
import sys

# Ensure parent directory is on the search path for imports
sys.path.append("..")

from core.settings import Settings
from entities.PlayerFactory import PlayerFactory
from entities.MobFactory import MobFactory
from entities.Player import Player


class InteractionManager:
    """
    Manages skill checks and opposed checks between Player instances.
    """

    # Valid skill or ability checks
    VALID_CHECKS = {
        'acrobatics', 'animal_handling', 'arcana', 'athletics', 'deception',
        'history', 'insight', 'intimidation', 'investigation', 'medicine',
        'nature', 'perception', 'performance', 'persuasion', 'religion',
        'sleight_of_hand', 'stealth', 'survival',
        'str', 'dex', 'con', 'int', 'wis', 'cha'
    }

    def __init__(self, test=False) -> None:
        """
        Initialize the InteractionManager.
        No internal state is required.
        """
        self.test = test
        self.player_factory = PlayerFactory()
        self.mob_factory = MobFactory()
        self.settings = Settings()
        if test:
            self.player = self.player_factory.create_player()
        


    def check(
        self,
        check_type: str,
        player_roll: int,
        bias: Optional[int] = None
    ) -> bool:
        """
        Perform a skill/ability check against a dynamically calculated DC.

        Args:
            check_type: The name of the check (skill or ability shorthand).
            player_roll: The raw roll value provided by the player.
            bias: Optional random bias to add to DC; if None, selects 1-18 uniformly.

        Returns:
            True if player_roll >= DC, False otherwise.

        Raises:
            ValueError: If `check_type` is not recognized.
        """
        check_key = check_type.lower()
        if check_key not in self.VALID_CHECKS:
            raise ValueError(f"Invalid check type: '{check_type}'")

        # Determine bias for DC calculation
        bias_value = bias if bias is not None else random.randint(1, 18)
        # Compute difficulty class
        dc = bias_value + self.settings.current_difficulty + self.settings.location_difficulty
        return player_roll >= dc

    def opposing_check(
        self,
        entity_one: Player,
        entity_two: Player,
        check_type: str
    ) -> str:
        """
        Perform opposed rolls for two players until one wins.

        Each player rolls via their `player_check_roll` method. The higher roll wins.
        Ties are rerolled until a winner emerges.

        Args:
            entity_one: First Player.
            entity_two: Second Player.
            check_type: The skill or ability to roll.

        Returns:
            The name of the winning entity.
        """
        while True:
            roll_one = entity_one.check_roll(check_type)
            roll_two = entity_two.check_roll(check_type)
            if roll_one > roll_two:
                return entity_one.get_name()
            if roll_two > roll_one:
                return entity_two.get_name()
            # On tie, loop to reroll

    def skill_check_test(self, player: Player) -> None:
        """
        Demo method: creates an NPC bandit and runs example checks.

        This method is for quick functionality testing and prints results.
        """
        # Create a random bandit NPC
        
        bandit = self.player_factory.create_player(npc=True, enemy=True)
        bandit.sheet()

        # Dexterity check
        dex_roll = player.check_roll('dex')
        dex_passed = self.check('dex', dex_roll)
        print(f"{player.get_name()} dex check ({dex_roll}) passed? {dex_passed}")

        # Investigation check
        inv_roll = player.check_roll('investigation')
        inv_passed = self.check('investigation', inv_roll)
        print(f"{player.get_name()} investigation check ({inv_roll}) passed? {inv_passed}")

        # Opposed strength check
        winner = self.opposing_check(player, bandit, 'str')
        print(f"Opposed strength winner: {winner}")

    def _test(self) -> None:
        """
        Run a test of the InteractionManager's functionality.
        This is a placeholder for unit tests or manual testing.
        """
        # Example test case: create a player and run a skill check
        IM = InteractionManager(test=True)
        IM.skill_check_test(IM.player)


    
# Run tests:
# InteractionManager._test(InteractionManager)

