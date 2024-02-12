# Dijjon combat
# Developed & designed by: Zane M Deso
# Purpose: Combat takes care of all combat related scenarios including turn orders, actions, calling checks, rolls, tie breakers, win condition checking, and state tracking for comabt events.

import random

class Combat:
    def __init__(self, entities):
        self.entities = entities

    def roll_initiative(self):
        """Roll initiative for all entities"""
        initiative_scores = {entity: random.randint(1, 20) for entity in self.entities}
        sorted_entities = sorted(self.entities, key=lambda x: initiative_scores[x], reverse=True)
        return sorted_entities

    def start_combat(self):
        """Start the combat"""
        turn_order = self.roll_initiative()
        print("Combat begins!")
        round_number = 1
        while not self.check_combat_over():
            print(f"Round {round_number}")
            for entity in turn_order:
                if self.check_combat_over():
                    break
                print(f"{entity.get_name()}'s turn:")
                self.entity_turn(entity)
            round_number += 1
        print("Combat ends!")

    def check_combat_over(self):
        """Check if combat is over"""
        # Combat is over if there are no more enemies
        return all(isinstance(entity, Enemy) for entity in self.entities)

    def entity_turn(self, entity): # FIX ME: WIll need to add a parameter to internally check if entity is player if not then make rand actions (better yet create weighted choices dependant on the entity)
        """Handle a single entity's turn"""
        action = input("Choose an action (e.g., attack, defend, etc.): ") # Add in a list of this enities actions (will be implemented later in Player adn other classes, etc.)
        if action.lower() == "attack":
            target = self.choose_target(entity)
            if target:
                self.attack(entity, target)
            else:
                print("No valid target available.")
        else:
            print("Invalid action. Choose another action.")

    def choose_target(self, entity):
        """Choose a target for the entity's attack"""
        print("Choose a target:")
        for idx, target in enumerate(self.entities):
            if target != entity:
                print(f"{idx + 1}. {target.get_name()}")
        choice = input("Enter the number of the target: ")
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(self.entities) and self.entities[idx] != entity:
                return self.entities[idx]
            else:
                return None
        except ValueError:
            return None

    def attack(self, attacker, target):
        """Perform an attack"""
        print(f"{attacker.get_name()} attacks {target.get_name()}!")
        # For simplicity, let's assume a basic attack
        # Calculate hit roll
        hit_roll = random.randint(1, 20) + attacker.get_modifier("str")
        if hit_roll >= target.get_armor_class():
            # Hit successful
            damage = random.randint(1, 6) + attacker.get_modifier("str")
            print(f"{attacker.get_name()} hits {target.get_name()} for {damage} damage!")
            target.take_damage(damage)
        else:
            print(f"{attacker.get_name()} misses the attack!") # lets make a table somewhere to add spicy quips and descriptions dynamically instead of the same thign everytime


# Example usage:
class Entity:
    def __init__(self, name, hp, armor_class):
        self.name = name
        self.hp = hp
        self.armor_class = armor_class

    def get_name(self):
        return self.name

    def get_armor_class(self):
        return self.armor_class

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print(f"{self.name} has been defeated!")


class Player(Entity):
    pass  # Implement Player class as needed


class Enemy(Entity):
    pass  # Implement Enemy class as needed


# Create player and enemy instances
player = Player("Player", 10, 12)
enemy1 = Enemy("Enemy 1", 8, 10)
enemy2 = Enemy("Enemy 2", 6, 8)

# Start combat
combat = Combat([player, enemy1, enemy2])
combat.start_combat()
