# Dijjon combat
# Developed & designed by: Zane M Deso
# Purpose: Combat takes care of all combat related scenarios including turn orders, actions, calling checks, rolls, tie breakers, win condition checking, and state tracking for comabt events.

import random
from Player import Player

class Combat:
    def __init__(self, entities):  # FIX ME: Add a list to track teams and team members, might need to implemnet some team classes or simplify it by only allowing two teams at first via two teams lists
        self.entities = entities

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
        while self.check_if_any_enemy_alive():
            print(f"Round {round_number}")
            for entity in turn_order:
                if not self.check_if_any_enemy_alive():
                    break
                print(f"{entity.get_name()}'s turn:")
                self.entity_turn(entity)
            round_number += 1
        print("Combat ends!")

    
    def check_if_any_enemy_alive(self):  
        """Check if combat is over by checking if any enemy is still alive."""
        return any(entity.is_enemy for entity in self.entities)


    def entity_turn(self, entity): # Player param is a reference to the actual Player.py class
        """Handle a single entity's turn, differentiating between player and enemy actions."""
        if isinstance(entity, Player):
            self.player_turn(entity)
        else:
            self.enemy_turn(entity)

    def player_turn(self, player):
        """Process a player's turn, allowing them to choose an action."""
        action = input("Choose an action (e.g., attack, defend, etc.): ") # FIX ME: eventually will be reimplemented to incorporate the player instance list of available actions
        if action.lower() == "attack":
            target = self.choose_target(player)
            if target:
                self.attack(player, target)
            else:
                print("No valid target available.")
        else:
            print("Invalid action. Choose another action.")

    def enemy_turn(self, enemy, Player):
        """Automatically process an enemy's turn, for now simply choosing to attack."""
        # This can be expanded with a more sophisticated AI or strategy pattern
        target = random.choice([e for e in self.entities if e != enemy and isinstance(e, Player)]) # target will be a random choice of one of the enitities in combat only if the target is a Player instance and not itself.
        self.attack(enemy, target)
  
    def choose_target(self, entity):
        """Prompt the player to choose a target for their action."""
        print("Choose a target:")
        valid_targets = [e for e in self.entities if e != entity]
        for idx, target in enumerate(valid_targets):
            print(f"{idx + 1}. {target.get_name()}")
        choice = input("Enter the number of the target: ")
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(valid_targets):
                return valid_targets[idx]
        except ValueError:
            pass
        return None

    def attack(self, attacker, target):
        """Execute an attack action from attacker to target."""
        # For simplicity, let's assume a basic attack
        print(f"{attacker.get_name()} attacks {target.get_name()}!")
        # Calculate hit roll
        hit_roll = random.randint(1, 20) + attacker.get_modifier(attacker.get_str())
        if hit_roll >= target.get_arm_c(): # Hit successful
            damage = random.randint(1, 6) + attacker.get_modifier(attacker.get_str())
            print(f"{attacker.get_name()} hits {target.get_name()} for {damage} damage!")
            target.set_hp(target.get_hp() - damage)
        else:
            print(f"{attacker.get_name()} misses the attack!") # lets make a table somewhere to add spicy quips and descriptions dynamically instead of the same thing everytime




