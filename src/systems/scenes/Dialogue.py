# Scene: Dialogue

from ..SceneManager import SceneManager, Scene
import pygame as pg
import random as r
import math



class Dialogue(Scene):

    def on_enter(self, ctx):
        self.manager = ctx['manager']
        self.ctx = ctx
        self.egg = False
        self.assets = ctx.get('assets', {})
        self.quest_manager = ctx.get('quest_manager', None)
        self.dialogue_manager = ctx.get('dialogue_manager', None)
        self.button_manager = ctx.get('button_manager', None)
        self.text_renderer = ctx.get('text_renderer', None)
        self.sfx = ctx.get('sfx', {})
        self.screen = ctx.get('screen', None)
        self.text_renderer.reset(self.quest_manager.get_current_narrative())
        self.button_manager.create_buttons(self.quest_manager.get_current_options())
     
        self.overlay = pg.Surface((self.ctx.get('screen_width', 600), (self.ctx.get('screen_height', 800))), pg.SRCALPHA)
        # print(f"Debug: Start.py -> self.manager: {self.manager}\non_enter called with ctx: {ctx}")

        print("Entered Dialogue Road Scene")

    def handle_event(self, e):
        if e.type == pg.KEYDOWN and e.key == pg.K_w:
            print("Switching to Desert_Town Scene")
            from .Desert_Town import Desert_Town
            self.manager.replace(Desert_Town())
        if e.type == pg.KEYDOWN and e.key == pg.K_a:
            print("Switching to Overworld Scene")
            from .Overworld import Overworld
            self.manager.replace(Overworld())
        if e.type == pg.KEYDOWN and e.key == pg.K_s:
            print("Switching to Inn Scene")
            from .Inn import Inn
            self.manager.replace(Inn())


        button_index = self.button_manager.handle_event(e)
        ui_button_index = self.button_manager.handle_UI_event(e)
        if button_index is not None:
            print(f"Button {button_index}(Dia Scene)")
            num = int(r.uniform(1, 6))
            self.sfx[f'btn{num}'].play()
            self.quest_manager.advance_step(button_index)
            self.text_renderer.reset(self.quest_manager.get_current_narrative())
            self.button_manager.create_buttons(self.quest_manager.get_current_options())
        if ui_button_index is not None:
            print(f"UI Button {ui_button_index}(Dia Scene)")
            num = int(r.uniform(1, 6))
            self.sfx[f'btn{num}'].play()
        

    def update(self, dt, passive=False):
        
        if self.egg:
            if not hasattr(self, "_color_phase"):
                self._color_phase = 0.0
                self._color_speed = .0185  # cycles per second
                self._r_offset = 0.0
                self._g_offset = 2 * math.pi / 3
                self._b_offset = 4 * math.pi / 3

            self._color_phase += dt * self._color_speed * 2 * math.pi
            # values oscillate smoothly between 0 and 256
            self.r = (math.sin(self._color_phase + self._r_offset) + 1) * 128
            self.g = (math.sin(self._color_phase + self._g_offset) + 1) * 128
            self.b = (math.sin(self._color_phase + self._b_offset) + 1) * 128
        else:
            self.r = 14
            self.g = 70
            self.b = 30

    def draw(self, screen):


        # print(f"Debug: Overworld.py -> assets in draw(): {self.text_renderer.text}")
        self.assets['dialogue_ui']
        screen.blit(self.assets['dialogue_ui'], (0, 0))

        self.assets['notice_ui']
        screen.blit(self.assets['notice_ui'], (-28, -120))

        img = self.assets['protrait']
        scaled = pg.transform.smoothscale_by(img, .2875)
        screen.blit(scaled, (80, 391))

        self.text_renderer.update()
        self.text_renderer.draw()
        self.button_manager.draw_buttons()


