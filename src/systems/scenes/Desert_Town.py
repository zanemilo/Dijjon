# Scene: Desert_Town

from ..SceneManager import SceneManager, Scene
import pygame as pg
import random as r
import math



class Desert_Town(Scene):
    def on_enter(self, ctx):
        self.manager = ctx['manager']
        self.ctx = ctx
        self.egg = False
        self.assets = ctx.get('assets', {})

        print("Entered Desert Town Scene")

    def handle_event(self, e):
        if e.type == pg.KEYDOWN and e.key == pg.K_d:
            print("Switching to Desert Trade Scene")
            from .Desert_Trade import Desert_Trade
            self.manager.replace(Desert_Trade())
        if e.type == pg.KEYDOWN and e.key == pg.K_s:
            print("Switching to Desert Road Scene")
            from .Desert_Road import Desert_Road
            self.manager.replace(Desert_Road())
        if e.type == pg.KEYDOWN and e.key == pg.K_TAB:
            print("Switching to Inventory Scene")
            from .Inventory import Inventory
            self.manager.push(Inventory())        

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

        # print(f"Debug: Overworld.py -> assets in draw(): {self.assets}")
        screen.blit(self.assets['bg_desert_town'], (0, 0))
        screen.blit(self.assets['dialogue_ui'], (0, 0))

