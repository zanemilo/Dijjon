# Dijjon Quest Class
# Developed & designed by: Zane M Deso
# Purpose: Used to handle quest instances dynamically as to remove need to hard code quests.

from Event import Event 


class Encounter(Event):
    """
    Encounter Class for managing dynamic quest instances, inheriting from the Event class.

    This class handles the flow of an encounter, including presenting narrative text,
    processing player choices, and handling different outcomes such as combat,
    skill checks, and narrative events.

    Attributes:
        encounter_data (dict): A dictionary containing the structure and data of the encounter.
        current_state (str): The current state or node within the encounter data.
    """

    def __init__(self, name, description, encounter_data):
        """
        Initializes a new Encounter instance with a name, description, and encounter data.

        Args:
            name (str): The name of the encounter.
            description (str): A brief description of the encounter.
            encounter_data (dict): The data structure defining the encounter's flow, choices, and outcomes.
        """
        super().__init__(name, description)  # Initialize the base Event class with name and description
        self.encounter_data = encounter_data  # Store the encounter data for managing flow
        self.current_state = 'start'  # Initialize the encounter's current state to 'start'

    def start(self):
        """
        Starts the encounter by invoking the base class's start method,
        announcing the beginning of the encounter, and displaying the initial text.
        """
        super().start()  # Call the start method from the Event base class
        print("An encounter begins...")  # Announce the start of the encounter
        self.display_current_text()  # Display the narrative text for the current state

    def progress(self, choice):
        """
        Progresses the encounter based on the player's choice.

        Args:
            choice (str): The player's choice input that determines the next state.

        Workflow:
            1. Retrieve the current node's data from encounter_data.
            2. Check if the current node has options and if the player's choice is valid.
            3. Update the current state based on the choice.
            4. Display the narrative text for the new state.
            5. If the new state has an outcome, handle it accordingly.
            6. If the choice is invalid, notify the player.
        """
        current_node = self.encounter_data[self.current_state]  # Get data for the current state
        if "options" in current_node and choice in current_node['options']:
            # Update the current state based on the player's choice
            self.current_state = current_node['options'][choice]
            self.display_current_text()  # Display narrative text for the new state
            if "outcome" in self.encounter_data[self.current_state]:
                self.handle_outcome()  # Handle any outcomes associated with the new state
        else:
            print("Invalid choice, try again.")  # Notify the player of an invalid choice

    def display_current_text(self):
        """
        Displays the narrative text associated with the current state of the encounter.
        """
        print(self.encounter_data[self.current_state]['text'])  # Print the current state's text

    def handle_outcome(self):
        """
        Handles the outcome of the current state based on the encounter data.

        Depending on the outcome type, it calls the corresponding method to handle:
            - Combat scenarios
            - Skill checks
            - Narrative events

        After handling the outcome, it updates the encounter status to completed.
        """
        outcome = self.encounter_data[self.current_state]['outcome']  # Retrieve the outcome type
        # Depending on the outcome, call different handling methods
        if outcome == "combat":
            self.initiate_combat()  # Initiate combat sequence
        elif outcome == "skill_check":
            self.perform_skill_check()  # Perform a skill check
        elif outcome == "narrative":
            self.narrative_event()  # Handle a special narrative event
        self.update_status(completed=True)  # Mark the encounter as completed

    def initiate_combat(self):
        """
        Initiates a combat scenario.

        Notes:
            - Assumes that combat logic is managed elsewhere, possibly integrating with a Combat class.
            - This method can be expanded to include detailed combat initiation steps.
        """
        print("Combat starts!")  # Announce the start of combat
        # Combat logic would go here, possibly integrating with a combat class

    def perform_skill_check(self):
        """
        Performs a skill check scenario.

        Notes:
            - Handles the logic for skill checks, such as rolling dice and determining success.
            - This method can be expanded to include specific skill check mechanics.
        """
        print("Performing a skill check...")  # Announce the skill check
        # Skill check logic would go here

    def narrative_event(self):
        """
        Handles a special narrative event within the encounter.

        Notes:
            - Manages unique narrative-driven events that do not involve combat or skill checks.
            - This method can be expanded to include complex narrative interactions.
        """
        print("A special event unfolds...")  # Announce the narrative event
        # Narrative logic would go here

    def end(self):
        """
        Ends the encounter by invoking the base class's end method and announcing the outcome.

        Depending on whether the encounter was completed or failed, it notifies the player accordingly.
        """
        super().end()  # Call the end method from the Event base class
        if self.is_completed:
            print("The encounter has been resolved.")  # Notify player of successful encounter resolution
        elif self.is_failed:
            print("The encounter has failed.")  # Notify player of failed encounter
