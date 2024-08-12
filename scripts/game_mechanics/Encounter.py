# Dijjon Quest Class
# Developed & designed by: Zane M Deso
# Purpose: Used to handle quest instances dynamically as to remove need to hard code quests.


import scripts.game_mechanics.Event as Event

class Encounter(Event):
    def __init__(self, name, description, encounter_data):
        super().__init__(name, description)
        self.encounter_data = encounter_data
        self.current_state = 'start'

    def start(self):
        super().start()
        print("An encounter begins...")
        self.display_current_text()

    def progress(self, choice):
        current_node = self.encounter_data[self.current_state]
        if "options" in current_node and choice in current_node['options']:
            self.current_state = current_node['options'][choice]
            self.display_current_text()
            if "outcome" in self.encounter_data[self.current_state]:
                self.handle_outcome()
        else:
            print("Invalid choice, try again.")

    def display_current_text(self):
        print(self.encounter_data[self.current_state]['text'])

    def handle_outcome(self):
        outcome = self.encounter_data[self.current_state]['outcome']
        # Depending on the outcome, call different methods:
        if outcome == "combat":
            self.initiate_combat()
        elif outcome == "skill_check":
            self.perform_skill_check()
        elif outcome == "narrative":
            self.narrative_event()
        self.update_status(completed=True)

    def initiate_combat(self):
        # Assuming combat logic is managed elsewhere:
        print("Combat starts!")
        # Combat logic would go here, possibly integrating with a combat class

    def perform_skill_check(self):
        # Handle skill check logic:
        print("Performing a skill check...")
        # Skill check logic would go here

    def narrative_event(self):
        # Special narrative event handling:
        print("A special event unfolds...")
        # Narrative logic would go here

    def end(self):
        super().end()
        if self.is_completed:
            print("The encounter has been resolved.")
        elif self.is_failed:
            print("The encounter has failed.")

