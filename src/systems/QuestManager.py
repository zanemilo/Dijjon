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

    def get_current_narrative(self):
        """Get the current narrative text for the quest."""
        return self.quest.tasks[self.current_task_id]["narrative"][self.current_step]

    def render_current_narrative(self):
        current_narrative = self.get_current_narrative()
        self.text_renderer.reset(current_narrative)
        while not self.text_renderer.finished:
            self.screen.fill((0, 0, 0))
            self.text_renderer.update()
            self.text_renderer.draw()
            pygame.display.flip()

    def get_current_options(self):
        """Get the current options for the quest."""
        return self.quest.tasks[self.current_task_id]["answers"][self.current_step]
    
    def advance_step(self, choice):
        """
        Advance the step in the current task, handling branching based on player choice.
        
        Args:
            choice (int): The index of the player's chosen option.
        """
        # Check if a random event should occur
        random_event_chance = self.quest.tasks[self.current_task_id].get("random_event_chance", 0)
        if random.random() < random_event_chance:
            self.trigger_random_event()
            return None

        # Normal branching logic
        branching = self.quest.tasks[self.current_task_id].get("branching", {})
        if choice in branching:
            self.current_task_id = branching[choice]
            self.current_step = 1
        else:
            self.current_step += 1

        if self.current_step > len(self.quest.tasks[self.current_task_id]["narrative"]):
            self.complete_task()
            return None
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
