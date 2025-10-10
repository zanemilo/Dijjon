# Scene: Start

from ..SceneManager import SceneManager, Scene
import pygame as pg

class Start(Scene):
        
        def on_enter(self, ctx): 
             self.manager = ctx['manager']
             self.ctx = ctx
             print("Entered Start Scene")

        def handle_event(self, e):
            if e.type == pg.KEYDOWN and e.key == pg.K_c:
                print("Switching to Combat Scene")

        def update(self, dt, passive=False): 
             print(f"Updating Start Scene [dt:", dt, "]")

        def draw(self, screen): 
             screen.fill((24,30,40))

