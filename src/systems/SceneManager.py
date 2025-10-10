"""
SceneManager stack for Pygame
--------------------------------
  - class Scene: lifecycle + typed, reusable interface
  - class SceneManager: push/pop/replace stack with optional fade transitions
  - class FadeTransition: simple midpoint swap fade-in/out

Usage (in main.py):

    import pygame as pg
    from scenes.base import Scene, SceneManager, FadeTransition

    class Overworld(Scene):
        def on_enter(self, ctx): self.manager = ctx['manager']
        def handle_event(self, e):
            if e.type == pg.KEYDOWN and e.key == pg.K_c:
                self.manager.replace(Combat(), FadeTransition(0.35))
        def update(self, dt, passive=False): pass
        def draw(self, screen): screen.fill((24,30,40))

    class Combat(Scene):
        def on_enter(self, ctx): self.manager = ctx['manager']
        def handle_event(self, e):
            if e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE:
                self.manager.replace(Overworld(), FadeTransition(0.3))
        def update(self, dt, passive=False): pass
        def draw(self, screen): screen.fill((40,12,18))

    def main():
        pg.init()
        screen = pg.display.set_mode((960,540))
        clock = pg.time.Clock()
        ctx = {}
        manager = SceneManager(screen, Overworld(), ctx)
        ctx['manager'] = manager
        running = True
        while running:
            dt = clock.tick(60) / 1000.0
            for e in pg.event.get():
                if e.type == pg.QUIT: running = False
                else: manager.handle_event(e)
            manager.update(dt)
            manager.draw()
            pg.display.flip()
        pg.quit()

"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Dict, List
import pygame as pg

# -------------------------
# Core Scene API
# -------------------------
class Scene:
    """Base scene with a small, stable lifecycle.

    Override what you need. Keep per-scene state inside the instance.
    Pull shared/persistent state (player, assets, audio, etc.) from ctx in on_enter.
    """
    # --- Lifecycle hooks ---
    def on_enter(self, ctx: Dict):
        """Called when the scene becomes active (after being pushed/replaced)."""
        pass

    def on_exit(self):
        """Called right before the scene is removed or replaced."""
        pass

    # --- Main loop ---
    def handle_event(self, event: pg.event.Event):
        """Handle a single Pygame event."""
        pass

    def update(self, dt: float, passive: bool = False):
        """Advance simulation.
        `passive=True` means the scene is underneath an active top scene. Use it to run
        light animations without gameplay (optional; ignore if not needed).
        """
        pass

    def draw(self, screen: pg.Surface):
        """Draw the scene. Always draw a complete frame (the manager will overlay transitions)."""
        pass


class SceneManager:
    """Stack-based scene manager with optional transitions.

    Methods:
        push(scene, transition=None)    - modal overlay (Pause, Dialogue, Inventory)
        pop(transition=None)            - close the top scene
        replace(scene, transition=None) - swap the active scene (Overworld -> Combat)

    Notes:
      - If a Transition is active, input is swallowed until it finishes.
      - If `enable_passive_updates` is True, scenes under the top will receive
        update(dt, passive=True). Otherwise only the top scene updates.
    """

    def __init__(self, screen: pg.Surface, initial_scene: Scene, ctx: Optional[Dict] = None, *, enable_passive_updates: bool = False):
        self.screen = screen
        self.stack: List[Scene] = []
        self.ctx = ctx or {}
        self.enable_passive_updates = enable_passive_updates
        self.transition: Optional[_BaseTransition] = None
        # Start with the initial scene
        self.ctx['manager'] = self
        self.replace(initial_scene)
        

    # --- Introspection ---
    def current(self) -> Scene:
        return self.stack[-1]

    # --- Stack operations ---
    def push(self, scene: Scene, transition: Optional['_BaseTransition'] = None):
        if transition:
            self.transition = transition._start(self, 'push', scene)
        else:
            self.stack.append(scene)
            scene.on_enter(self.ctx)

    def pop(self, transition: Optional['_BaseTransition'] = None):
        if not self.stack:
            return
        if transition:
            self.transition = transition._start(self, 'pop', None)
        else:
            top = self.stack.pop()
            top.on_exit()

    def replace(self, scene: Scene, transition: Optional['_BaseTransition'] = None):
        if transition:
            self.transition = transition._start(self, 'replace', scene)
        else:
            if self.stack:
                self.stack[-1].on_exit()
                self.stack.pop()
            self.stack.append(scene)
            scene.on_enter(self.ctx)

    # --- Main loop integration ---
    def handle_event(self, event: pg.event.Event):
        # Block input while a transition is active
        if self.transition and self.transition.active:
            return
        if self.stack:
            self.current().handle_event(event)

    def update(self, dt: float):
        if self.transition and self.transition.active:
            self.transition.update(dt)
            if not self.transition.active:
                self.transition = None
            return

        if not self.stack:
            return

        if self.enable_passive_updates and len(self.stack) > 1:
            # Update all, mark non-top as passive
            for s in self.stack[:-1]:
                try:
                    s.update(dt, passive=True)
                except TypeError:
                    # Scene doesn't support passive arg; call legacy signature
                    s.update(dt)  # type: ignore[arg-type]
            self.current().update(dt, passive=False)
        else:
            self.current().update(dt)

    def draw(self):
        if not self.stack:
            return
        # Always draw the top scene (it may draw underlying visuals if desired)
        self.current().draw(self.screen)
        # Overlay transition visuals last
        if self.transition and self.transition.active:
            self.transition.draw(self.screen)


# -------------------------
# Transition base + fade
# -------------------------
class _BaseTransition:
    """Internal base class for transitions. Users should instantiate concrete subclasses
    like FadeTransition. The SceneManager drives update/draw while active.
    """
    active: bool = False

    def _start(self, manager: SceneManager, mode: str, next_scene: Optional[Scene]):
        raise NotImplementedError

    def update(self, dt: float):
        raise NotImplementedError

    def draw(self, screen: pg.Surface):
        raise NotImplementedError


@dataclass
class FadeTransition(_BaseTransition):
    duration: float = 0.4  # seconds
    _t: float = 0.0
    _mode: str = ''            # 'push' | 'pop' | 'replace'
    _next: Optional[Scene] = None
    _manager: Optional[SceneManager] = None

    def _start(self, manager: SceneManager, mode: str, next_scene: Optional[Scene]):
        self._manager = manager
        self._mode = mode
        self._next = next_scene
        self._t = 0.0
        self.active = True
        return self

    def update(self, dt: float):
        if not self.active:
            return
        self._t += dt
        half = self.duration * 0.5

        # Midpoint swap: perform the stack mutation once
        if self._t >= half and self._next is not None and self._manager:
            if self._mode == 'push':
                self._manager.stack.append(self._next)
                self._next.on_enter(self._manager.ctx)
            elif self._mode == 'replace':
                if self._manager.stack:
                    self._manager.stack[-1].on_exit()
                    self._manager.stack[-1:] = [self._next]
                else:
                    self._manager.stack.append(self._next)
                self._next.on_enter(self._manager.ctx)
            # ensure we don't repeat the mutation
            self._next = None

        if self._t >= self.duration:
            if self._mode == 'pop' and self._manager and self._manager.stack:
                top = self._manager.stack.pop()
                top.on_exit()
            self.active = False

    def draw(self, screen: pg.Surface):
        # Cross-fade to black and back
        w, h = screen.get_size()
        overlay = pg.Surface((w, h), pg.SRCALPHA)
        half = self.duration * 0.5
        if self._t <= half:
            alpha = int(255 * (self._t / max(half, 1e-6)))
        else:
            alpha = int(255 * (1 - (self._t - half) / max(half, 1e-6)))
        overlay.fill((0, 0, 0, max(0, min(255, alpha))))
        screen.blit(overlay, (0, 0))
