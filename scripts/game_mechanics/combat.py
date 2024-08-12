# Dijjon combat
# Developed & designed by: Zane M Deso
# Purpose: Combat takes care of all combat related scenarios including turn orders, actions, calling checks, rolls, tie breakers, win condition checking, and state tracking for comabt events.

import random
from scripts.entity.Player import Player


class Combat:
    def __init__(self, entities):
        self.entities = entities
        self.team1 = [e for e in entities if e.is_enemy is False]
        self.team2 = [e for e in entities if e.is_enemy is True]

    def roll_initiative(self):
        """Roll initiative for all entities"""
        initiative_scores = {entity: random.randint(1, 20) for entity in self.entities} # Currently only calls for a random int between 1 - 20. FIX ME: Implement proper dex calls per entity.
        sorted_entities = sorted(self.entities, key=lambda x: initiative_scores[x], reverse=True)
        return sorted_entities

    def start_combat(self):
        """Start the combat loop, iterating through entities' turns."""
        turn_order = self.roll_initiative()
        print("Combat begins!")
        round_number = 1
        while any(e.is_alive() for e in self.team1) and any(e.is_alive() for e in self.team2):
            print(f"Round {round_number}")
            for entity in turn_order:
                if not (any(e.is_alive() for e in self.team1) and any(e.is_alive() for e in self.team2)):
                    break
                print(f"{entity.get_name()}'s turn:")
                self.entity_turn(entity)
            round_number += 1
        print("Combat ends!")

    def entity_turn(self, entity):
        """Handle a single entity's turn, differentiating between player and enemy actions."""
        while True:  # Keep asking until a valid action is taken
            action = input(f"{entity.get_name()}, choose an action (attack, defend, etc.): ")
            if action.lower() == "attack":
                target = self.choose_target(entity)
                if target:
                    self.attack(entity, target)
                    break  # Exit the loop after a valid action
            else:
                print("Invalid action. Choose another action.")

    def enemy_turn(self, enemy):
        """Automatically process an enemy's turn, choosing to attack."""
        valid_targets = [e for e in self.entities if e != enemy and e.is_alive()]
        if valid_targets:
            target = random.choice(valid_targets)
            self.attack(enemy, target)
  
    def choose_target(self, entity):
        """Prompt the player to choose a target for their action."""
        print("Choose a target:")
        valid_targets = [e for e in self.entities if e != entity and e.is_alive()]
        for idx, target in enumerate(valid_targets):
            print(f"{idx + 1}. {target.get_name()}")
        choice = input("Enter the number of the target: ")
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(valid_targets):
                return valid_targets[idx]
        except ValueError:
            pass
        print("Invalid target choice.")
        return None

    def attack(self, attacker, target):
        """Execute an attack action from attacker to target."""
        print(f"{attacker.get_name()} prepares to attack {target.get_name()}!")
        hit_roll = random.randint(1, 20) + attacker.get_modifier(attacker.get_dex())
        if hit_roll >= target.get_arm_c():
            damage = random.randint(1, 6) + attacker.get_modifier(attacker.get_str())
            print(f"{attacker.get_name()} hits {target.get_name()} for {damage} damage!")
            target.set_hp(target.get_hp() - damage)  # FIX ME: Simplified damage version for now, plan on passing damage to the target to process (thinking something like target.damage(int, type, crit=False, non_lethal=False))
        else:
            print(f"{attacker.get_name()} misses the attack!")




