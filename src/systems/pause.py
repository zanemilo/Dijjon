from __future__ import annotations
import pygame as pg
from dataclasses import dataclass
from typing import Callable, List, Tuple, Optional

# Import your base classes
from SceneManager import Scene, FadeTransition


@dataclass
class MenuItem:
    label: str
    action: Callable[[], None]


class PauseMenuScene(Scene):
    """
    Pause menu with keyboard & mouse support.
    Items: Resume, Save, Load, Settings, Exit

    Expected keys in ctx (optional but recommended):
      - ctx['manager'] : SceneManager (set in bootstrap)
      - ctx['save_system'] : object with .save() and .load() methods (optional)
      - ctx['settings_scene_factory'] : Callable[[], Scene] that returns a Settings scene (optional)

    Behavior:
      - ESC / Resume -> pop with fade
      - Save/Load -> calls into ctx['save_system'] if present; shows toast on success/failure
      - Settings -> push settings scene if provided
      - Exit -> replace with a fresh Overworld or call ctx['on_exit_to_title'] if provided
    """

    def __init__(self, *, title: str = "Paused"):
        self.title = title
        self.font_title: Optional[pg.font.Font] = None
        self.font_item: Optional[pg.font.Font] = None
        self.font_hint: Optional[pg.font.Font] = None
        self.items: List[MenuItem] = []
        self.sel: int = 0
        self.mouse_hot: Optional[int] = None
        self.toast_text: Optional[str] = None
        self.toast_timer: float = 0.0
        self.spacing = 54
        self.margin_top = 140
        self.disabled_color = (130, 130, 130)

    # -------------- lifecycle --------------
    def on_enter(self, ctx):
        self.ctx = ctx
        self.manager = ctx['manager']
        # Fonts
        self.font_title = pg.font.SysFont(None, 64)
        self.font_item = pg.font.SysFont(None, 36)
        self.font_hint = pg.font.SysFont(None, 22)

        # Build menu
        self.items = [
            MenuItem("Resume", self._act_resume),
            MenuItem("Save", self._act_save),
            MenuItem("Load", self._act_load),
            MenuItem("Settings", self._act_settings),
            MenuItem("Exit", self._act_exit),
        ]
        self.sel = 0
        self.mouse_hot = None
        self.toast_text = None
        self.toast_timer = 0.0

    def on_exit(self):
        pass

    # -------------- actions --------------
    def _act_resume(self):
        self.manager.pop(FadeTransition(0.2))

    def _act_save(self):
        save_sys = self.ctx.get('save_system')
        if not save_sys:
            self._toast("No save system bound")
            return
        try:
            save_sys.save()
            self._toast("Game saved")
        except Exception as e:
            self._toast(f"Save failed: {e}")

    def _act_load(self):
        save_sys = self.ctx.get('save_system')
        if not save_sys:
            self._toast("No save system bound")
            return
        try:
            save_sys.load()
            self._toast("Game loaded")
        except Exception as e:
            self._toast(f"Load failed: {e}")

    def _act_settings(self):
        factory = self.ctx.get('settings_scene_factory')
        if factory is None:
            self._toast("No settings scene configured")
            return
        self.manager.push(factory(), FadeTransition(0.2))

    def _act_exit(self):
        # Allow caller to override exit behavior
        on_exit_cb = self.ctx.get('on_exit_to_title')
        if callable(on_exit_cb):
            on_exit_cb()
            return
        # Fallback: quit the app (you may want to swap to TitleScene instead)
        pg.event.post(pg.event.Event(pg.QUIT))

    # -------------- events --------------
    def handle_event(self, e: pg.event.Event):
        if e.type == pg.KEYDOWN:
            if e.key in (pg.K_ESCAPE, pg.K_RETURN, pg.K_SPACE) and self.sel == 0:
                self._act_resume()
                return
            if e.key in (pg.K_ESCAPE,) and self.sel != 0:
                # ESC always resumes quickly
                self._act_resume()
                return
            if e.key in (pg.K_UP, pg.K_w):
                self.sel = (self.sel - 1) % len(self.items)
            elif e.key in (pg.K_DOWN, pg.K_s):
                self.sel = (self.sel + 1) % len(self.items)
            elif e.key in (pg.K_RETURN, pg.K_SPACE):
                self.items[self.sel].action()

        elif e.type == pg.MOUSEMOTION:
            mx, my = e.pos
            self.mouse_hot = self._hit_test(mx, my)
            if self.mouse_hot is not None:
                self.sel = self.mouse_hot

        elif e.type == pg.MOUSEBUTTONDOWN and e.button == 1:
            mx, my = e.pos
            idx = self._hit_test(mx, my)
            if idx is not None:
                self.items[idx].action()

    # -------------- update/draw --------------
    def update(self, dt: float, passive: bool = False):
        if self.toast_text:
            self.toast_timer -= dt
            if self.toast_timer <= 0:
                self.toast_text = None

    def draw(self, screen: pg.Surface):
        w, h = screen.get_size()
        # dim background
        dim = pg.Surface((w, h), pg.SRCALPHA)
        dim.fill((0, 0, 0, 160))
        screen.blit(dim, (0, 0))

        # title
        assert self.font_title and self.font_item and self.font_hint
        title_surf = self.font_title.render(self.title, True, (240, 240, 240))
        screen.blit(title_surf, (w // 2 - title_surf.get_width() // 2, 60))

        # menu items
        x = w // 2
        y = self.margin_top
        for i, item in enumerate(self.items):
            hot = (i == self.sel)
            color_fg = (255, 255, 255) if hot else (200, 200, 200)

            # background pill
            padx, pady = 18, 10
            text_surf = self.font_item.render(item.label, True, color_fg)
            rect = text_surf.get_rect()
            rect.centerx = x
            rect.y = y + i * self.spacing
            bg_rect = rect.inflate(padx * 2, pady * 2)

            pill = pg.Surface(bg_rect.size, pg.SRCALPHA)
            radius = 14
            _rounded_rect(pill, pill.get_rect(), (30, 30, 34, 220 if hot else 160), radius)
            screen.blit(pill, bg_rect)

            # draw text
            screen.blit(text_surf, (bg_rect.x + (bg_rect.w - rect.w) // 2, bg_rect.y + (bg_rect.h - rect.h) // 2))

        # footer hint
        hint = "↑/↓ or W/S to select • Enter/Space to confirm • ESC to resume"
        hint_surf = self.font_hint.render(hint, True, (200, 200, 200))
        screen.blit(hint_surf, (w // 2 - hint_surf.get_width() // 2, h - 40))

        # toast
        if self.toast_text:
            toast_surf = self.font_item.render(self.toast_text, True, (255, 255, 255))
            tw, th = toast_surf.get_size()
            pad = 12
            box = pg.Surface((tw + pad * 2, th + pad * 2), pg.SRCALPHA)
            _rounded_rect(box, box.get_rect(), (20, 20, 20, 220), 12)
            bx = w // 2 - box.get_width() // 2
            by = h - 90
            screen.blit(box, (bx, by))
            screen.blit(toast_surf, (bx + pad, by + pad))

    # -------------- helpers --------------
    def _hit_test(self, mx: int, my: int) -> Optional[int]:
        # Mirror draw layout to compute hot index
        w, h = pg.display.get_surface().get_size()
        x = w // 2
        for i, item in enumerate(self.items):
            text_surf = self.font_item.render(item.label, True, (0, 0, 0))
            rect = text_surf.get_rect()
            rect.centerx = x
            rect.y = self.margin_top + i * self.spacing
            bg_rect = rect.inflate(36, 20)
            if bg_rect.collidepoint(mx, my):
                return i
        return None

    def _toast(self, msg: str, seconds: float = 1.6):
        self.toast_text = msg
        self.toast_timer = seconds


# -------- drawing utility --------

def _rounded_rect(surf: pg.Surface, rect: pg.Rect, color_rgba: Tuple[int, int, int, int], radius: int):
    """Draw a filled rounded rectangle on the given surface (RGBA)."""
    # Pygame's draw module supports border_radius for filled rects.
    shape = pg.Surface((rect.w, rect.h), pg.SRCALPHA)
    pg.draw.rect(shape, color_rgba, shape.get_rect(), border_radius=radius)
    surf.blit(shape, rect)
