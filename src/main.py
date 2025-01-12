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

pygame.init()
# screen = pygame.display.set_mode((800, 600))
screen = None
pygame.display.set_caption('Dijjon')

# TextRenderer setup
# text_renderer = TextRenderer(
#     screen=screen,
#     text="",
#     font_name=None,
#     font_size=24,
#     color=(255, 255, 255),  # White text
#     position=(50, 100),
#     typing_speed=50  # Speed of typing effect
# )
text_renderer = None
    
# Sample Quest Data
qtype = {
    "find": Quest.find,
    "kill": Quest.kill,
    "skill_check": Quest.skill_check,
}

tasks = a1_tasks

# Instantiate Quest and QuestManager
quest = Quest("Act I - Scene I", "The Summit at Hollowreach Citadel", qtype, tasks)
quest_manager = QuestManager(quest, text_renderer, screen)

player_factory = PlayerFactory()

button_manager = ButtonManager(screen)
button_manager.create_buttons(quest_manager.get_current_options())

player = None # FIX ME: TO be replaced when load functionality is implemented.
# running = True
# text_rendering_complete = False
# text_renderer.reset(quest_manager.get_current_narrative())
options = quest_manager.get_current_options()
# Instantiate and run the DialogueManager
dialogue_manager = DialogueManager(quest_manager)
if not player:
        try:
           player = player_factory.create_player()
           player.display_info()
        except Exception as e:
            print(f"Error creating player: {e}")

dialogue_manager.run_dialogue_event()

# while running:
    # Ensure player is created before continuing
    # if not player:
    #     try:
    #        player = player_factory.create_player()
    #        player.display_info()
    #     except Exception as e:
    #         print(f"Error creating player: {e}")
    #         running = False
    #         break

    # # Handle events
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         running = False

    #     # Handle button clicks
    #     button_index = button_manager.handle_event(event)
    #     if button_index is not None:
    #         quest_manager.advance_step(button_index)
    #         prev_options = options
    #         options = quest_manager.get_current_options()
    #          # Update buttons only if options change
    #         if options != prev_options:
    #             try:
    #                 button_manager.create_buttons(options)
    #             except Exception as e:
    #                 print(f"Error updating buttons: {e}")
    #         # Update narrative text after advancing quest
    #         text_renderer.reset(quest_manager.get_current_narrative())
            
    # # Clear the screen
    # screen.fill((0, 0, 0))
    # # Always draw buttons and update display
    # button_manager.draw_buttons()
    # Render quest narrative and buttons
    # if not quest_manager.is_quest_complete:
            # text_renderer.update()
            # text_renderer.draw()
    # else:
        # text_renderer.reset("Quest Complete! Congratulations!")
        # text_renderer.update()
        # text_renderer.draw()

    # pygame.display.flip()

# pygame.quit()
