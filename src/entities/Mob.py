"""
Module: Mob
Defines the `Mob` class, a subclass of `Entity`, representing non-player creatures with RPG attributes.
"""

import random
from typing import Optional, Dict

from entities.Entity import Entity
from systems.core_library import monster_dict as md, name_list as nl


class Mob(Entity):
    """
    Represents a non-player creature with RPG-style attributes.

    Attributes:
        name (str): The given or randomly chosen name of the mob.
        mob (str): The key identifying the species of the creature.
        mob_type (Any): Metadata or type information fetched from `monster_dict`.
        lvl (int): Level of the mob, affecting difficulty and stats.
        max_hp (int): Maximum health points.
        hp (int): Current health points.
        arm_c (int): Armor class, reducing incoming damage.
        spd (int): Movement speed.
        xp (int): Experience awarded when defeated.
        is_enemy (bool): Flag indicating hostility.
    """

    def __init__(
        self,
        name: Optional[str] = None,
        mob: Optional[str] = None,
        hp: Optional[int] = None,
        arm_c: Optional[int] = None,
        spd: Optional[int] = None,
        xp: Optional[int] = None,
        lvl: Optional[int] = None,
        is_enemy: bool = True
    ) -> None:
        """
        Initialize a `Mob` instance, randomizing any attributes not provided.

        Args:
            name: Custom name; defaults to a random choice from `name_list`.
            mob: Species key; defaults to a random key from `monster_dict`.
            hp: Initial and maximum HP; defaults to a random value.
            arm_c: Armor class; defaults to a random value.
            spd: Speed; defaults to base speed if not provided.
            xp: Experience value; defaults to a random value.
            lvl: Creature level; defaults to a small random level.
            is_enemy: Hostility flag.
        """
        # Assign a random name if none is provided
        self.name = name or random.choice(nl)
        # Assign a random species key if none is provided
        self.mob = mob or random.choice(list(md.keys()))
        # Retrieve species metadata from the dictionary
        self.mob_type = md[self.mob]

        # Determine level, defaulting to 1–3 randomly
        self.lvl = lvl or random.randint(1, 3)
        # Determine maximum HP, then set current HP to max
        self.max_hp = hp or random.randint(10, 30)
        self.hp = self.max_hp
        # Determine armor class, defaulting to 10–15 randomly
        self.arm_c = arm_c or random.randint(10, 15)
        # Set movement speed, defaulting to 30
        self.spd = spd or 30
        # Determine XP reward, defaulting to 10–30 randomly
        self.xp = xp or random.randint(10, 30)
        # Set hostility flag
        self.is_enemy = is_enemy

        # Initialize base Entity with these attributes
        super().__init__(
            name=self.name,
            hp=self.hp,
            arm_c=self.arm_c,
            spd=self.spd,
            xp=self.xp,
            lvl=self.lvl,
            is_enemy=self.is_enemy
        )

    def __repr__(self) -> str:
        """
        Return an unambiguous string representation for debugging.
        """
        return (
            f"<Mob name={self.name!r} species={self.mob!r} "
            f"type={self.mob_type!r} lvl={self.lvl} "
            f"hp={self.hp}/{self.max_hp} arm_c={self.arm_c} "
            f"spd={self.spd} xp={self.xp} enemy={self.is_enemy}>"
        )

    @property
    def is_alive(self) -> bool:
        """
        Check if the mob is still alive.

        Returns:
            True if HP > 0, False otherwise.
        """
        return self.hp > 0

    def take_damage(self, amount: int) -> None:
        """
        Inflict damage on the mob, reducing HP but not below zero.

        Args:
            amount: The amount of damage to apply.
        """
        # Ensure HP doesn't go negative
        self.hp = max(self.hp - amount, 0)

    def heal(self, amount: int) -> None:
        """
        Heal the mob, increasing HP but not above `max_hp`.

        Args:
            amount: The amount of HP to restore.
        """
        # Ensure HP doesn't exceed maximum
        self.hp = min(self.hp + amount, self.max_hp)

    def to_dict(self) -> Dict[str, object]:
        """
        Serialize the mob's stats to a dictionary.

        Returns:
            A dict containing key attributes for inspection or storage.
        """
        return {
            "name": self.name,
            "species": self.mob,
            "type": self.mob_type,
            "level": self.lvl,
            "hp": self.hp,
            "max_hp": self.max_hp,
            "armor_class": self.arm_c,
            "speed": self.spd,
            "xp": self.xp,
            "is_enemy": self.is_enemy,
        }

    def display_info(self) -> None:
        """
        Print a formatted summary of the mob's current stats to stdout.
        """
        info = self.to_dict()
        for key, val in info.items():
            print(f"{key:12}: {val}")
