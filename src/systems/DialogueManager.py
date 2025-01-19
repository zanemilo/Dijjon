# DialogueManager
# Author: Zane M Deso
# Purpose: Handle Dialogue events in terminal during Dijjon development.


class DialogueManager:
    """
    Handles dialogue events using QuestManager for structured narratives and choices.
    Delivers dialogue text and manages player input for branching options in the terminal.
    """

    def __init__(self, quest_manager):
        """
        Initializes the DialogueManager.

        Args:
            quest_manager (QuestManager): The QuestManager instance for managing quests.
        """
        self.quest_manager = quest_manager  # Reference to QuestManager instance
        self.running = False  # Indicates if the dialogue event is active
        self.selected_option = None  # The player's selected option

    def display_narrative(self):
        """
        Fetches and displays the current narrative text from QuestManager.
        """
        current_narrative = self.quest_manager.get_current_narrative()
        print("\n" + "-" * 80)
        print(current_narrative)
        print("-" * 80)

    def display_options(self):
        """
        Fetches and displays the current options for the dialogue from QuestManager.
        """
        options = self.quest_manager.get_current_options()
        print("\nChoose an option:")
        for i, option in enumerate(options, 1):
            print(f"{i}: {option}")

    def get_player_choice(self):
        """
        Prompts the player to select an option and validates their input.

        Returns:
            int: The index of the player's chosen option.
        """
        options = self.quest_manager.get_current_options()
        valid_choices = range(1, len(options) + 1)
        choice = None

        while choice not in valid_choices:
            try:
                choice = int(input("\nEnter your choice: "))
                if choice not in valid_choices:
                    print("Invalid choice. Please select a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number corresponding to an option.")

        return choice - 1  # Return zero-based index for processing

    def run_script(self, step, choice, player):
        """
        Dynamically calls the script associated with the current narrative step.

        Args:
            step (int): The current narrative step index.

        Returns:
            None
        """
        script = self.quest_manager.quest.tasks[self.quest_manager.current_task_id]["scripts"].get(step)

        if script:
            print(f"Running script for step {step}...")
            # Execute the script function, passing the quest manager and other relevant data
            script(task_id=self.quest_manager.current_task_id, tasks=self.quest_manager.quest.tasks, choice=choice, player=player)
        else:
            print(f"No script defined for step {step}.")

    def run_dialogue_event(self, player=None):
        """
        Manages the full dialogue event, interacting with QuestManager for progression.
        """
        self.running = True
        while self.running and not self.quest_manager.is_quest_complete:
            current_step = self.quest_manager.current_step

            # Display the current narrative
            self.display_narrative()

            # Display and process options if available
            options = self.quest_manager.get_current_options()
            if options:
                self.display_options()
                player_choice_index = self.get_player_choice()
                selected_option = options[player_choice_index]

                print(f"\nYou selected: {selected_option}")

                # Run the script for the current step
                self.run_script(current_step, player_choice_index, player)

                # Pass the player's choice to QuestManager for processing
                next_narrative = self.quest_manager.advance_step(player_choice_index)
                if next_narrative is None:
                    self.running = False

        print("\nDialogue concluded.")