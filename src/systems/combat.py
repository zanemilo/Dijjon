# Dijjon combat
# Developed & designed by: Zane M Deso
# Purpose: Combat takes care of all combat related scenarios including turn orders, actions, calling checks, rolls, tie breakers, win condition checking, and state tracking for combat events.

import random
import sys
sys.path.append("..")  # Adds the parent directory to the Python module search path

from systems import dice_Roll as dr
from ..entities import PlayerFactory as pf



class Combat:
    """
    Combat Class to manage all combat-related scenarios in the game.

    Attributes:
        entities (list): A list of all entities participating in the combat.
        team1 (list): A list of friendly entities (not enemies).
        team2 (list): A list of enemy entities.
    """

    def __init__(self, entities):
        """
        Initializes the Combat instance with participating entities.

        Args:
            entities (list): A list of all entities (players and enemies) involved in the combat.
        """
        self.entities = entities
        # Separate entities into team1 (friendly) and team2 (enemies) based on the 'is_enemy' attribute
        self.team1 = [e for e in entities if e.is_enemy is False]
        self.team2 = [e for e in entities if e.is_enemy is True]

    def roll_initiative(self):
        """
        Rolls initiative for all entities to determine the turn order.

        Currently, it assigns a random integer between 1 and 20 to each entity.
        TODO: Implement proper Dexterity (DEX) checks for initiative based on each entity's attributes.

        Returns:
            list: A list of entities sorted in descending order based on their initiative scores.
        """
        # Generate a dictionary mapping each entity to a random initiative score
        initiative_scores = {entity: random.randint(1, 20) for entity in self.entities}  # FIX ME: Implement proper dex calls per entity.
        # Sort entities based on their initiative scores in descending order
        sorted_entities = sorted(self.entities, key=lambda x: initiative_scores[x], reverse=True)
        return sorted_entities

    def start_combat(self):
        """
        Starts the combat loop, managing rounds and turns until one team is defeated.

        The combat continues in rounds, where each entity gets a turn based on initiative order.
        The loop exits when all entities in either team1 or team2 are no longer alive.
        """
        # Determine the turn order by rolling initiative
        turn_order = self.roll_initiative()
        print("Combat begins!")  # Announce the start of combat
        round_number = 1  # Initialize round counter

        # Continue combat while both teams have at least one alive entity
        while any(e.is_alive() for e in self.team1) and any(e.is_alive() for e in self.team2):
            print(f"Round {round_number}")  # Announce the current round
            for entity in turn_order:
                # Check if combat should continue before each entity's turn
                if not (any(e.is_alive() for e in self.team1) and any(e.is_alive() for e in self.team2)):
                    break  # Exit the loop if one team has been defeated
                print(f"{entity.get_name()}'s turn:")  # Announce whose turn it is
                self.entity_turn(entity)  # Handle the entity's turn
            round_number += 1  # Increment the round counter
        print("Combat ends!")  # Announce the end of combat

    def entity_turn(self, entity):
        """
        Handles the actions an entity can perform during their turn.

        Differentiates between player and enemy actions by prompting input for players
        and automating actions for enemies.

        Args:
            entity (Entity): The entity whose turn it is to act.
        """
        while True:  # Loop until a valid action is taken
            # Prompt the entity to choose an action
            action = input(f"{entity.get_name()}, choose an action (attack, defend, etc.): ")
            if action.lower() == "attack":
                # If the action is 'attack', prompt to choose a target
                target = self.choose_target(entity)
                if target:
                    self.attack(entity, target)  # Execute the attack
                    break  # Exit the loop after a successful action
            else:
                # If the action is invalid, notify and prompt again
                print("Invalid action. Choose another action.")

    def enemy_turn(self, enemy):
        """
        Processes an enemy's turn automatically, typically choosing to attack.

        Args:
            enemy (Entity): The enemy entity whose turn it is to act.
        """
        # Determine valid targets (all alive entities excluding the enemy itself)
        valid_targets = [e for e in self.entities if e != enemy and e.is_alive()]
        if valid_targets:
            # Select a random target from the valid targets
            target = random.choice(valid_targets)
            self.attack(enemy, target)  # Execute the attack

    def choose_target(self, entity):
        """
        Prompts the player to choose a target for their action.

        Displays a list of valid targets and returns the selected target based on player input.

        Args:
            entity (Entity): The entity performing the action, used to exclude self from targets.

        Returns:
            Entity or None: The chosen target entity if valid, otherwise None.
        """
        print("Choose a target:")  # Prompt to choose a target
        # List of valid targets (all alive entities excluding the acting entity)
        valid_targets = [e for e in self.entities if e != entity and e.is_alive()]
        for idx, target in enumerate(valid_targets):
            print(f"{idx + 1}. {target.get_name()}")  # Display each target with a number
        choice = input("Enter the number of the target: ")  # Prompt for target selection
        try:
            idx = int(choice) - 1  # Convert input to zero-based index
            if 0 <= idx < len(valid_targets):
                return valid_targets[idx]  # Return the selected target
        except ValueError:
            pass  # If input is not a valid integer, ignore and handle below
        print("Invalid target choice.")  # Notify of invalid choice
        return None  # Return None if no valid target was selected

    def attack(self, attacker, target):
        """
        Executes an attack action from the attacker to the target.

        Rolls to hit and calculates damage based on attacker's and target's attributes.

        Args:
            attacker (Entity): The entity performing the attack.
            target (Entity): The entity being attacked.
        """
        print(f"{attacker.get_name()} prepares to attack {target.get_name()}!")  # Announce the attack
        # Roll to hit: d20 plus attacker's Dexterity modifier
        hit_roll = random.randint(1, 20) + attacker.get_modifier(attacker.get_dex())
        if hit_roll >= target.get_arm_c():
            # If the hit roll meets or exceeds target's armor class, attack hits
            damage = random.randint(1, 6) + attacker.get_modifier(attacker.get_str())  # Calculate damage
            print(f"{attacker.get_name()} hits {target.get_name()} for {damage} damage!")  # Announce damage
            # Deduct damage from target's HP
            target.set_hp(target.get_hp() - damage)  # FIX ME: Simplified damage version for now, plan on passing damage to the target to process (thinking something like target.damage(int, type, crit=False, non_lethal=False))
        else:
            # If the hit roll is below target's armor class, attack misses
            print(f"{attacker.get_name()} misses the attack!")

    def combat_simulation(self, entity_one, entity_two):
        """
        Simulate a turn-based combat scenario between two entities.

        This function handles the flow of combat, alternating turns between the two entities
        until one of them is defeated.

        Args:
            entity_one (Player): The first entity participating in combat.
            entity_two (Player): The second entity participating in combat.
        """
        print("Starting combat simulation...")  # Announce the start of combat simulation
        while entity_one.get_hp() > 0 and entity_two.get_hp() > 0:
            # Entity One's turn
            print(f"{entity_one.get_name()}'s turn:")  # Announce whose turn it is
            action = input("Choose an action (attack): ")  # Prompt for action
            if action.lower() == "attack":
                # Calculate attack roll: d20 + strength modifier
                attack_roll = dr.roll_d20() + entity_one.get_modifier(entity_one.get_str())
                print(f"{entity_one.get_name()} rolls {attack_roll} to attack.")  # Display the attack roll
                # Check if the attack hits based on target's armor class
                if attack_roll >= entity_two.get_arm_c():
                    # Calculate damage: d6 + strength modifier
                    damage = dr.roll_d6() + entity_one.get_modifier(entity_one.get_str())
                    print(f"{entity_one.get_name()} hits {entity_two.get_name()} for {damage} damage!")  # Announce damage
                    entity_two.set_hp(entity_two.get_hp() - damage)  # Deduct damage from target's HP
                else:
                    print(f"{entity_one.get_name()} misses the attack.")  # Announce miss

            # Check if Entity Two is still alive
            if entity_two.get_hp() <= 0:
                print(f"{entity_two.get_name()} has been defeated!")  # Announce defeat
                break  # Exit combat if Entity Two is defeated

            # Entity Two's turn
            print(f"{entity_two.get_name()}'s turn:")  # Announce whose turn it is
            action = input("Choose an action (attack): ")  # Prompt for action
            if action.lower() == "attack":
                # Calculate attack roll: d20 + strength modifier
                attack_roll = dr.roll_d20() + entity_two.get_modifier(entity_two.get_str())
                print(f"{entity_two.get_name()} rolls {attack_roll} to attack.")  # Display the attack roll
                # Check if the attack hits based on target's armor class
                if attack_roll >= entity_one.get_arm_c():
                    # Calculate damage: d6 + strength modifier
                    damage = dr.roll_d6() + entity_two.get_modifier(entity_two.get_str())
                    print(f"{entity_two.get_name()} hits {entity_one.get_name()} for {damage} damage!")  # Announce damage
                    entity_one.set_hp(entity_one.get_hp() - damage)  # Deduct damage from target's HP
                else:
                    print(f"{entity_two.get_name()} misses the attack.")  # Announce miss

            # Check if Entity One is still alive
            if entity_one.get_hp() <= 0:
                print(f"{entity_one.get_name()} has been defeated!")  # Announce defeat
                break  # Exit combat if Entity One is defeated
    
    def combat_sim(self, player):
        """
        Simulates a combat scenario between the player and a bandit.

        Steps:
        1. Instantiates a bandit player with random race and class.
        2. Displays the bandit's character sheet.
        3. Sets up a combat scenario between the player and the bandit.
        4. Initiates and runs the combat.
        """
        # Instantiate a new bandit player with random race and class, marked as an enemy
        bandit = pf.create_player(npc=True, enemy=True)
        
        # Display the bandit's character sheet using the Master class
        bandit.sheet()
        
        # Setup combat scenario with the player and the bandit
        combat = Combat([player, bandit])
        
        # Run the combat simulation
        combat.start_combat()
