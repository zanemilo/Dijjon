from __future__ import annotations
import json
import os
from dataclasses import is_dataclass, asdict
from typing import Any, Dict, Iterable


class SaveSystem:
    """
    A tiny JSON save/load helper tied to your shared ctx.

    - Saves a subset of ctx keys (default: 'player', 'inventory', 'world', 'settings').
    - Serializes dataclasses via asdict(), and objects with to_dict() if available.
    - On load, updates existing objects via from_dict() if available; else replaces.

    Example wiring in main.py:

        from systems.save_system import SaveSystem
        ctx = {...}
        save = SaveSystem(ctx, path='saves/slot1.json')
        ctx['save_system'] = save

    Now your Pause menu's Save/Load will work.
    """

    def __init__(self, ctx: Dict[str, Any], path: str = 'saves/slot1.json', keys: Iterable[str] = ("player", "inventory", "world", "settings")):
        self.ctx = ctx
        self.path = path
        self.keys = list(keys)
        os.makedirs(os.path.dirname(self.path), exist_ok=True)

    # ------------- public API -------------
    def save(self):
        data: Dict[str, Any] = {}
        for k in self.keys:
            if k in self.ctx:
                data[k] = self._serialize(self.ctx[k])
        tmp = self.path + ".tmp"
        with open(tmp, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        os.replace(tmp, self.path)
        return self.path

    def load(self):
        if not os.path.exists(self.path):
            raise FileNotFoundError(self.path)
        with open(self.path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for k, v in data.items():
            self._apply(k, v)
        return data

    # ------------- helpers -------------
    def _serialize(self, obj: Any):
        # dataclass
        if is_dataclass(obj):
            return asdict(obj)
        # custom to_dict()
        to_dict = getattr(obj, 'to_dict', None)
        if callable(to_dict):
            try:
                return to_dict()
            except Exception:
                pass
        # simple JSON-friendly types
        if isinstance(obj, (str, int, float, bool)) or obj is None:
            return obj
        if isinstance(obj, (list, tuple)):
            return [self._serialize(x) for x in obj]
        if isinstance(obj, dict):
            return {str(k): self._serialize(v) for k, v in obj.items()}
        # fallback: object __dict__ (shallow)
        d = getattr(obj, '__dict__', None)
        if isinstance(d, dict):
            return {str(k): self._serialize(v) for k, v in d.items() if not k.startswith('_')}
        # last resort: string repr
        return str(obj)

    def _apply(self, key: str, payload: Any):
        # object exists in ctx
        if key in self.ctx:
            target = self.ctx[key]
            # custom from_dict
            from_dict = getattr(target, 'from_dict', None)
            if callable(from_dict):
                try:
                    from_dict(payload)
                    return
                except Exception:
                    pass
            # dict-like → replace contents
            if isinstance(target, dict) and isinstance(payload, dict):
                target.clear()
                target.update(payload)
                return
            # list-like → replace contents
            if isinstance(target, list) and isinstance(payload, list):
                target.clear()
                target.extend(payload)
                return
        # otherwise, or if incompatible: overwrite
        self.ctx[key] = payload
