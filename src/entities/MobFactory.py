"""
Module: MobFactory
Defines the `MobFactory` class for generating `Mob` entities, mirroring the `PlayerFactory` pattern.
Each method delegates attribute defaults and randomization to the `Mob` constructor.
"""

import random
import sys
from typing import List, Optional

# Ensure parent directory is on the search path for imports
sys.path.append("..")

from entities.Mob import Mob
from systems.core_library import monster_dict, name_list


class MobFactory:
    """
    Factory class for creating `Mob` instances.

    Provides methods to:
      - Create a single `Mob` with optional custom stats.
      - Generate encounters (lists of mobs) for game scenarios.
    """

    def __init__(self) -> None:
        """
        Initialize a `MobFactory` instance.

        No internal state is required; all randomness is handled by `Mob`.
        """
        # No initialization state needed; kept for future extensibility
        pass

    def create_mob(
        self,
        name: Optional[str] = None,
        mob: Optional[str] = None,
        hp: Optional[int] = None,
        arm_c: Optional[int] = None,
        spd: Optional[int] = None,
        xp: Optional[int] = None,
        lvl: Optional[int] = None,
        is_enemy: bool = True
    ) -> Mob:
        """
        Create and return a single `Mob` instance.

        Args:
            name: Optional custom name; if omitted, `Mob` picks randomly.
            mob: Optional species key; if omitted, random key from `monster_dict`.
            hp: Optional hit points; if omitted, handled by `Mob` constructor.
            arm_c: Optional armor class; if omitted, handled by `Mob` constructor.
            spd: Optional speed; if omitted, handled by `Mob` constructor.
            xp: Optional experience awarded on defeat; if omitted, handled.
            lvl: Optional level; if omitted, handled by `Mob` constructor.
            is_enemy: Flag indicating if the mob is hostile.

        Returns:
            A new `Mob` instance initialized with the provided or random attributes.
        """
        # Delegate all attribute logic and randomization to Mob.__init__
        return Mob(
            name=name,
            mob=mob,
            hp=hp,
            arm_c=arm_c,
            spd=spd,
            xp=xp,
            lvl=lvl,
            is_enemy=is_enemy
        )

    def create_encounter(self, count: int = 1, **kwargs) -> List[Mob]:
        """
        Generate a list of `Mob` instances for an encounter.

        Args:
            count: Number of mobs to create for this encounter.
            **kwargs: Any keyword arguments forwarded to `create_mob` (e.g., `mob='Goblin'`).

        Returns:
            A list of `Mob` instances of length `count`.
        """
        # Use list comprehension to create multiple mobs with identical settings
        return [self.create_mob(**kwargs) for _ in range(count)]


# Example usage:
# factory = MobFactory()
# single_mob = factory.create_mob()
# goblin_pack = factory.create_encounter(3, mob='Goblin')
# for m in goblin_pack:
#     m.display_info()  # Print each mob's stats
