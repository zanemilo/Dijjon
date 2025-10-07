# Dijjon Quest Class
# Developed & designed by: Zane M Deso
# Purpose: Used to handle settings for the game.

from __future__ import annotations
import pygame as pg
from typing import Optional
from SceneManager import Scene, FadeTransition


class Settings:
    """A class to store all settings for Dijjon"""

    def __init__(self, current_difficulty = 2, location_difficulty = 0):
        """Initialize game settings"""
        self.current_difficulty = current_difficulty
        self.location_difficulty = location_difficulty

    
    def get_diff(self):
        """Returns current difficulty"""
        return self.current_difficulty
    
    def set_diff(self, difficulty):
        """Change current difficulty"""

        if difficulty in range(1, 11):
            self.current_difficulty = difficulty
        else:
            print(f'Error: Difficulty arg out of range (1-10)\nDifficulty remains unchanged.')

    def get_loc_diff(self):
        return self.current_difficulty
    
    def set_loc_diff(self, difficulty):
        """Change location difficulty"""

        if difficulty in range(0, 6):
            self.current_difficulty = difficulty
        elif difficulty not in range(0, 6):
            print(f'Error: Location difficulty arg out of range (0-5)\nLocation difficulty remains unchanged.')
        







class SettingsScene(Scene):
    """
    Minimal, dependency-light settings screen.
    Controls:
      - Up/Down: select option
      - Left/Right: change value (for sliders/toggles)
      - Enter/Space: toggle/apply
      - ESC/Backspace: return to previous scene

    Expects (optional) in ctx:
      - ctx['settings']: dict with keys 'music_volume' (0-100), 'sfx_volume' (0-100), 'fullscreen' (bool)
      - ctx['apply_settings']: callable(settings_dict) to actually apply (e.g., mixer volume, toggle display mode)
      - ctx['save_system']: if present, auto-saves settings on exit
    """

    def on_enter(self, ctx):
        self.ctx = ctx
        self.manager = ctx['manager']
        self.font_title = pg.font.SysFont(None, 56)
        self.font_item = pg.font.SysFont(None, 32)
        self.font_hint = pg.font.SysFont(None, 20)
        s = ctx.setdefault('settings', {})
        self.music = int(s.get('music_volume', 70))
        self.sfx = int(s.get('sfx_volume', 80))
        self.fullscreen = bool(s.get('fullscreen', False))
        self.sel = 0
        self.spacing = 50
        self.margin_top = 120

    def on_exit(self):
        # persist settings back to ctx
        settings = self._gather_settings()
        self.ctx['settings'] = settings
        # apply if an applier is available
        applier = self.ctx.get('apply_settings')
        if callable(applier):
            applier(settings)
        # save if save system exists
        save_sys = self.ctx.get('save_system')
        if save_sys:
            try:
                save_sys.save()
            except Exception:
                pass

    # ------------ events ------------
    def handle_event(self, e: pg.event.Event):
        if e.type == pg.KEYDOWN:
            if e.key in (pg.K_ESCAPE, pg.K_BACKSPACE):
                self.manager.pop(FadeTransition(0.2))
                return
            if e.key in (pg.K_UP, pg.K_w):
                self.sel = (self.sel - 1) % 4
            elif e.key in (pg.K_DOWN, pg.K_s):
                self.sel = (self.sel + 1) % 4
            elif e.key in (pg.K_LEFT, pg.K_a):
                self._adjust(-1)
            elif e.key in (pg.K_RIGHT, pg.K_d):
                self._adjust(+1)
            elif e.key in (pg.K_RETURN, pg.K_SPACE):
                self._toggle_or_apply()

    def update(self, dt: float, passive: bool = False):
        pass

    def draw(self, screen: pg.Surface):
        w, h = screen.get_size()
        screen.fill((14, 16, 20))
        title = self.font_title.render("Settings", True, (240, 240, 240))
        screen.blit(title, (w // 2 - title.get_width() // 2, 40))

        items = [
            ("Music Volume", f"{self.music}%"),
            ("SFX Volume", f"{self.sfx}%"),
            ("Fullscreen", "On" if self.fullscreen else "Off"),
            ("Back", "↩"),
        ]
        y = self.margin_top
        for i, (k, v) in enumerate(items):
            hot = (i == self.sel)
            color = (255, 255, 255) if hot else (200, 200, 200)
            left = self.font_item.render(k, True, color)
            right = self.font_item.render(v, True, color)
            screen.blit(left, (w // 2 - 220, y))
            screen.blit(right, (w // 2 + 120 - right.get_width(), y))
            y += self.spacing

        hint = "↑/↓ select  •  ←/→ adjust  •  Enter apply/toggle  •  ESC back"
        hint_surf = self.font_hint.render(hint, True, (190, 190, 190))
        screen.blit(hint_surf, (w // 2 - hint_surf.get_width() // 2, h - 36))

    # ------------ helpers ------------
    def _gather_settings(self):
        return {
            'music_volume': int(max(0, min(100, self.music))),
            'sfx_volume': int(max(0, min(100, self.sfx))),
            'fullscreen': bool(self.fullscreen),
        }

    def _adjust(self, delta: int):
        if self.sel == 0:
            self.music = max(0, min(100, self.music + delta * 5))
        elif self.sel == 1:
            self.sfx = max(0, min(100, self.sfx + delta * 5))
        elif self.sel == 2:
            # toggle on left/right as well
            self.fullscreen = not self.fullscreen
        elif self.sel == 3:
            # Back: leave
            self.manager.pop(FadeTransition(0.2))

    def _toggle_or_apply(self):
        if self.sel == 2:
            self.fullscreen = not self.fullscreen
            settings = self._gather_settings()
            applier = self.ctx.get('apply_settings')
            if callable(applier):
                applier(settings)
        elif self.sel == 3:
            self.manager.pop(FadeTransition(0.2))
           
            
        
