# Scene: Start

from ..SceneManager import SceneManager, Scene
import pygame as pg
import random as r
import math

class Start(Scene):
        
        def on_enter(self, ctx): 
             self.manager = ctx['manager']
             self.ctx = ctx
             self.egg = False
             
             print("Entered Start Scene")

        def handle_event(self, e):
            if e.type == pg.KEYDOWN and e.key == pg.K_c:
                print("Switching to Combat Scene")
                self.egg = True

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

