import random
import pygame

class QuestManager:
    """
    Manages the quest, including the current state, task execution,
    branching decisions, and randomization.
    """
    def __init__(self, quest, text_renderer, screen):
        self.quest = quest
        self.current_task_id = 1
        self.current_step = 1
        self.is_quest_complete = False
        self.text_renderer = text_renderer  # Integrate TextRenderer
        self.screen = screen  # Screen for Pygame rendering
    
    def update_quest(self, new_quest=None):
        if new_quest:
            self.quest = new_quest
        return self.quest

    def get_current_narrative(self):
        """
        Retrieves the current narrative step for the active quest and task.
        This method checks if a quest and its associated tasks are available. 
        It then attempts to retrieve the narrative for the current task and 
        ensures the current step is valid within the narrative.
        Returns:
            str: The narrative text for the current step if available. 
                 Returns "No quest or tasks available." if there is no active 
                 quest or tasks. Returns "Invalid narrative step." if the 
                 narrative is not a list or the current step is out of bounds.
        """
        if not self.quest or not self.quest.tasks:
            return "No quest or tasks available."

        # Safely get the task using .get() with a default empty dictionary
        try:
            task = self.quest.tasks.get(self.current_task_id)
        except TypeError as e:
            print(f"Error QuestManager.get_current_narrative() self.quests.tasks.get(self.current_task_id): {e}")
        try:
            narrative = task.get("narrative")
        except TypeError as e:
            print(f"Error QuestManager.get_current_narrative(): {e}")

        # Ensure current_step is within bounds
        if not isinstance(narrative, (list, tuple, dict)) or self.current_step >= len(narrative):
            return "Invalid narrative step."

        return narrative[self.current_step]

    def render_current_narrative(self):
        current_narrative = self.get_current_narrative()
        self.text_renderer.reset(current_narrative)
        while not self.text_renderer.finished:
            self.screen.fill((0, 0, 0))
            self.text_renderer.update()
            self.text_renderer.draw()
            pygame.display.flip()

    def get_current_options(self):
        if not self.quest or not self.quest.tasks:
            raise ValueError("Quest or tasks are not initialized.")
        
        task = self.quest.tasks.get(self.current_task_id, {})
        answers = task.get("answers", {})

        # Safely get the answers for the current step
        options = answers.get(self.current_step, None)
        if not options or not isinstance(options, list):
            raise ValueError(f"Task {self.current_task_id} does not have valid answers for step {self.current_step}.")
        
        return options
    
    def set_current_options(self, options : list):
        """Set the current options for the quest."""
        if options != self.quest.tasks[self.current_task_id]["answers"]:
            self.quest.tasks[self.current_task_id]["answers"][self.current_step] = options
        return self.quest.tasks[self.current_task_id]["answers"][self.current_step]
    
    def advance_step(self, choice, branching=False):
        """
        Advance the step in the current task, handling branching based on player choice.
        Does not currently handle advancing task_ids. Requires implementation.

        Args:
            choice (int): The index of the player's chosen option.
        """
       
       # Check if a random event should occur
        try:
            random_event_chance = self.quest.tasks[self.current_task_id].get("random_event_chance", 0)
            if random.random() < random_event_chance:
                self.trigger_random_event()
                return None
            # Normal branching logic
            branching = self.quest.tasks[self.current_task_id].get("branching", {})
        except TypeError as e:
            print(f"Error QuestManager.advance_step(): {e}")

        if branching:
            if choice in branching:
                self.current_task_id = branching[choice]
                self.current_step = 1
            else:
                self.current_step += 1
        try:
            if self.current_step > len(self.quest.tasks[self.current_task_id]["narrative"]):
                self.complete_task()
                return None
        except TypeError as e:
            print(f"Error QuestManager.advance_step(): {e}")

        return self.get_current_narrative()

    def trigger_random_event(self):
        """Trigger a random event and handle its outcome."""
        random_event = random.choice(self.quest.random_events)
        print(f"Random event: {random_event['description']}")
        if "outcome" in random_event:
            # Apply outcome logic
            random_event["outcome"]()

    def complete_task(self):
        """Mark the current task as complete and check if the quest is finished."""
        self.quest.complete_task(self.current_task_id, self.quest.tasks)
        # Check if there are more tasks or if the quest is complete
        if not any(not t["complete"] for t in self.quest.tasks.values()):
            self.is_quest_complete = True
