# DialogueManager
# Author: Zane M Deso
# Purpose: Handle Dialogue events in terminal during Dijjon development.
import textwrap
import time
import os
import platform

class DialogueManager:
    """
    Handles dialogue events using QuestManager for structured narratives and choices.
    Delivers dialogue text and manages player input for branching options in the terminal.
    """

    def __init__(self, game, quest_manager):
        """
        Initializes the DialogueManager.

        Args:
            quest_manager (QuestManager): The QuestManager instance for managing quests.
        """
        self.quest_manager = quest_manager  # Reference to QuestManager instance
        self.running = False  # Indicates if the dialogue event is active
        self.selected_option = None  # The player's selected option
        self.game = game

    def display_narrative(self):
        """
        Fetches and displays the current narrative text from QuestManager.
        Formats the output for better readability in the terminal.
        """
        current_narrative = self.quest_manager.get_current_narrative()
        border = "=" * 72
        wrapped_text = textwrap.fill(current_narrative, width=70)  # Wrap text to 70 chars
        line = ''
        print(f"\n{border}")
        time.sleep(.175)
        # for i in current_narrative:  # FIXME: This is a custome line by line displayer. Needs to have been wrapping before implementation.
        #     if len(line) < 70:
        #         line = line + i
        #     else:
        #         print(line + i)
        #         time.sleep(.175)
        #         line = ''
        print(f"\n{wrapped_text}\n")
        time.sleep(.175)
        print(border)
        time.sleep(.175)

    def clear_terminal(self):
        """
        Clears the terminal screen for a clean display.
        Works on both Windows and Unix-based systems (Linux/MacOS).
        """
        time.sleep(.175)
        if platform.system() == "Windows":
            os.system("cls")  # Windows clear command
        else:
            os.system("clear")  # Unix-based systems clear command

    def display_options(self):
        """
        Fetches and displays the current options for the dialogue from QuestManager.
        """
        options = self.quest_manager.get_current_options()
        print("\nChoose an option:")
        for i, option in enumerate(options, 1):
            print(f"{i}: {option}")
            time.sleep(.175)

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
            dict: The updated tasks dict after running the script.
        """
        try:
            script = self.quest_manager.quest.tasks[self.quest_manager.current_task_id]["scripts"].get(step)
        except KeyError as e:
            print(f"Error: Script for step {step} not found in current task. {e}")
            return
        
        tasks = self.quest_manager.quest.tasks

        # Ensure the quest and tasks are properly initialized
        if not self.quest_manager.quest or not self.quest_manager.quest.tasks:
            print("Error: Quest or tasks are not properly initialized.")
            return
        
        # Ensure the current task ID is valid
        if self.quest_manager.current_task_id not in self.quest_manager.quest.tasks:
            print(f"Error: Task ID {self.quest_manager.current_task_id} is not valid.")
            return
        if not callable(script): # Check if the script is callable
            print(f"Script for step {step} is not callable.")
            return

        # Check if the script exists for the current step
        if not self.quest_manager.quest.tasks[self.quest_manager.current_task_id]["scripts"].get(step):
            print(f"No script defined for step {step}.")
            return
        else:
            tasks = self.quest_manager.quest.tasks
            #print(f"Running script for step {step}...") #DEBUG
            script = self.quest_manager.quest.tasks[self.quest_manager.current_task_id]["scripts"].get(step)
            #print(f"questmanager.quest.tasks: {tasks}") #DEBUG
            # Execute the script function, passing the quest manager and other relevant data
            return script(task_id=self.quest_manager.current_task_id, tasks=tasks, choice=choice, player=player)

        

    def run_dialogue_event(self, player=None):
        """
        Manages the full dialogue event, interacting with QuestManager for progression.
        """
        self.running = True

        while self.running and not self.quest_manager.is_quest_complete:
            current_step = self.quest_manager.current_step

            self.clear_terminal()
            
            self.display_narrative()

            # Display and process options if available
            try:
                options = self.quest_manager.get_current_options()
            except KeyError as e:
                print(f"Error: {e}. No options available for current step.")

            if options:
                self.display_options()
                player_choice_index = self.get_player_choice()
                selected_option = options[player_choice_index]

                print(f"\nYou selected: {selected_option}")
                time.sleep(.3)
                
                try:
                    # Run the script for the current step
                    new_tasks = self.run_script(current_step, player_choice_index, player)

                    if new_tasks:
                        # Invoke Game update_tasks method to update the tasks
                        self.game.update_tasks(new_tasks)
                    
                except Exception as e:
                    print(f"Error running script for step {self.quest_manager.current_step}: {e}\nDefaulting to current Questmanager.tasks...")

                # Pass the player's choice to QuestManager for processing
                next_narrative = self.quest_manager.advance_step(player_choice_index)

                #print(f"next_narrative: {next_narrative}")

                if next_narrative is None: # FIXME: AWT FIX
                    if self.quest_manager.advance_scene(): 
                        # Next Scene Available
                        print(f"\nScene {self.quest_manager.current_task_id} start:")
                        time.sleep(.3)
                    else:
                        print("\nNo more scenes available. Advancing to next act.")
                        if self.game.advance_act():
                            print(f"\nAct advanced. Now at scene {self.quest_manager.current_task_id}.")
                            time.sleep(.3)
                        else:
                            print("\nNo more acts. Ending dialogue.")
                            self.running = False
                        

        print("\nDialogue concluded.")
