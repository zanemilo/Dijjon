


class Item():
    """Item class: think template for items in game"""
    def __init__(self, name, desc, val):
        self.name = name
        self.desc = desc
        self.val = val

class Melee_Item(Item):
    """Melee_Item class: subclass to Item"""
    def __init__(self, name, desc, val, damage, damage_type, poisoned, enchant):
        super().__init__(name, desc, val)
        self.damage = damage
        self.damage_type = damage_type
        self.poisoned = poisoned
        self.enchant = enchant