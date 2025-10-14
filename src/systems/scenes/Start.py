# Scene: Start

from ..SceneManager import SceneManager, Scene
import pygame as pg
import random as r
import math


class Start(Scene):
        
        def on_enter(self, ctx): 
             self.manager = ctx['manager']
             # print(f"Debug: Start.py -> self.manager: {self.manager}\non_enter called with ctx: {ctx}")
             self.ctx = ctx
             self.egg = False
             self.assets = ctx.get('assets', {})
             
             print("Entered Start Scene")

        def handle_event(self, e):
            if e.type == pg.KEYDOWN and e.key == pg.K_w:
                print("Switching to Overworld Scene")
                from .Overworld import Overworld
                self.manager.replace(Overworld())
                self.egg = False
            if e.type == pg.KEYDOWN and e.key == pg.K_TAB:
                print("Switching to Inventory Scene")
                from .Inventory import Inventory
                self.manager.push(Inventory())
            if e.type == pg.KEYDOWN and e.key == pg.K_v:
                print("Switching to Dialogue Scene")
                from .Dialogue import Dialogue
                self.manager.push(Dialogue())

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
                self.r = 24
                self.g = 30
                self.b = 40

        def draw(self, screen): 
            screen.fill((self.r,self.g,self.b))
            screen.blit(self.assets['bg_desert_road'], (0, 0))


