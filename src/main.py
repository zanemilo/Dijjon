# Dijjon Main
# Developed & designed by: Zane M Deso
# Purpose: Main will act as the entrance point for the program to run.

import random as r  
import pygame

from entities.PlayerFactory import PlayerFactory
from systems.ui.text import TextRenderer
from systems.ButtonManager import ButtonManager
from systems.Quest import Quest
from systems.QuestManager import QuestManager
from systems.DialogueManager import DialogueManager
from systems.a1_tasks import tasks as a1_tasks
from systems.a2_tasks import tasks as a2_tasks
from systems.a3_tasks import tasks as a3_tasks


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Dijjon')

        self.text_renderer = TextRenderer(
            screen=self.screen,
            text="",
            font_name=None,
            font_size=24,
            color=(255, 255, 255),  # White text
            position=(50, 100),
            typing_speed=50 # Typing speed in milliseconds
        )

        self.qtype = {
            "find": Quest.find,
            "kill": Quest.kill,
            "skill_check": Quest.skill_check,
        }

        self.all_tasks = [
            a1_tasks,
            a2_tasks,
            a3_tasks,
        ]

        self.completed_tasks = []

        self.tasks = a1_tasks  # Default tasks
        self.quest = Quest("Act I - Scene I", "The Summit at Hollowreach Citadel", self.qtype, self.tasks)
        self.quest_manager = QuestManager(self.quest, self.text_renderer, self.screen)

        self.player_factory = PlayerFactory()
        self.player = None

        self.button_manager = ButtonManager(self.screen)
        self.button_manager.create_buttons(self.quest_manager.get_current_options())

        self.dialogue_manager = DialogueManager(game=self, quest_manager=self.quest_manager)

    def update_tasks(self, new_tasks):
        """Update the tasks and refresh dependent systems."""
        self.tasks = new_tasks
        self.quest.update_tasks(self.tasks)
        self.quest_manager.update_quest(self.quest)
        
    def advance_act(self):
        """Advance to the next act and update tasks accordingly.
        This method marks the current quest as complete, archives it, and sets up the next act.
        It also updates the quest manager with the new quest instance.
        Returns:
            Quest: The new Quest instance for the next act."""
        ## FIXME: AWT FIX
        # 1) figure out which act we're on
        for task in self.all_tasks:
            if self.quest.tasks == task:
                pass
            else:
                next_act = task
                break
        idx = self.all_tasks.index(self.tasks)
        if idx < len(self.all_tasks) - 1:
            next_act = self.all_tasks[idx + 1]
        else:
            return False   # no more acts

        # 2) swap in the tasks and Quest/QuestManager
        self.update_tasks(next_act)
        self.quest = Quest(
            f"Act {idx+2} – Scene 1",  # FIXME: Need to dynamically set the act name/desc etc
            "…description…",
            self.qtype,
            self.tasks
        )
        self.quest_manager.update_quest(self.quest)

        # reset the QuestManager’s pointers for the new act
        self.quest_manager.current_task_id = 1
        self.quest_manager.current_step   = 1
        self.quest_manager.is_quest_complete = False

        return True


    def run(self):
        """Main game loop."""
        running = True

        # Ensure player is created before continuing
        if not self.player:
            try:
                self.player = self.player_factory.create_player()
                self.player.display_info()
            except Exception as e:
                print(f"Error creating player: {e}")
                running = False

        self.dialogue_manager.run_dialogue_event(self.player)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Handle button clicks
                button_index = self.button_manager.handle_event(event)
                if button_index is not None:
                    self.quest_manager.advance_step(button_index)
                    self.button_manager.create_buttons(self.quest_manager.get_current_options())
                    self.text_renderer.reset(self.quest_manager.get_current_narrative())

            # Clear the screen
            self.screen.fill((0, 0, 0))

            # Render quest narrative and buttons
            if not self.quest_manager.is_quest_complete:
                self.text_renderer.update()
                self.text_renderer.draw()
            else:
                self.text_renderer.reset("Quest Complete! Congratulations!")
                self.text_renderer.update()
                self.text_renderer.draw()

            self.button_manager.draw_buttons()
            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
