# Dijjon Core Library File
# Developed & designed by: Zane M Deso
# Purpose: Used to store all in-game content.


import sys
sys.path.append("..")  # Adds the parent directory to the Python module search path
from systems import Item as i
from systems import dice_Roll


def class_list():  # passed testing in new main
        """
        Display a numbered list of available character classes.

        This function iterates through the 'classes' dictionary and prints each class with a corresponding number.
        """
        num = 1  # Initialize a counter to number the classes
        for class_type in classes:
            print(f'{num}. {class_type}')  # Print each class with its corresponding number
            num += 1  # Increment the counter

def race_list():  # passed testing in new main
    """
    Display a numbered list of available character races.

    This function iterates through the 'races' dictionary and prints each race with a corresponding number.
    """
    num = 1  # Initialize a counter to number the races
    for race_type in races:
        print(f'{num}. {race_type}')  # Print each race with its corresponding number
        num += 1  # Increment the counter



# Creates instances of Items class with name, description, and value as arguments
inn_items = {
    "Oats": i.Item(
        "Oats",
        "As you observe the oats, their small and unassuming appearance belies the nourishing and hearty sustenance they provide, a testament to the adage that good things come in small packages.",
        1
    ),
    "Bread": i.Item(
        "Bread",
        "As the aroma of freshly baked inn bread wafts towards you, its unpretentious and humble exterior masks the warm, comforting sustenance it promises, a tribute to the saying that true beauty lies in simplicity.",
        2
    ),
    "Pie": i.Item(
        "Pie",
        "As your eyes settle on the apple pie, the aroma of freshly baked cinnamon and butter wafts towards you, enticing your taste buds with the promise of a warm and flaky crust enveloping sweet and tangy apples, a quintessential treat that evokes memories of home and comfort.",
        3
    ),
    "Ale": i.Item(
        "Ale",
        "The inn's modest ale is a simple yet satisfying drink, with a smooth taste that lingers on the tongue.",
        1
    ),
    "Milk": i.Item(
        "Milk",
        "As you obtain a glass of milk, the creamy white liquid provides a soothing and wholesome taste, evoking a sense of comfort and simplicity.",
        2
    ),
    "Water Mug": i.Item(
        "Water Mug",
        "The clear and unremarkable appearance of the water in the mug was a refreshing contrast to the chaos of the world around it.",
        0
    ),
    "Cheese": i.Item(
        "Cheese",
        "A wedge of aged cheese, its rich aroma hints at a sharp and tangy flavor.",
        2
    ),
    "Stew": i.Item(
        "Stew",
        "A hearty bowl of stew filled with tender meat and root vegetables, warming you from within.",
        4
    ),
    "Fruit": i.Item(
        "Fruit",
        "A selection of fresh fruits, their vibrant colors and sweet scents inviting a taste.",
        1
    ),
    "Mead": i.Item(
        "Mead",
        "A honeyed mead that offers a sweet and smooth drinking experience.",
        3
    ),
}

# List of available races
races = [
    "Drakari",
    "Stonekin",
    "Sylphari",
    "Frostling",
    "Halfian",
    "Minfolk",
    "Orcane",
    "Humara",
    "Shadeborn",
    "Aetherborn",
    "Lumidar",
    "Feykin",
    "Tauren",
    "Merfolk",
]

race_stats = {
    "Drakari": {
        "abilities": ["Dragon's Breath", "Scales of Protection"],
        "skills": ["Intimidation", "Survival"],
        "feats": ["Draconic Heritage"],
        "spells": ["Burning Hands", "Dragon's Roar"],
        "resistances": {"fire": 0.5},
        "proficiencies": ["Heavy Armor", "Greatswords"],
        "movement": 30,
        "visibility": {"darkvision": 120},
        "disposition": {
            "Stonekin": 5,
            "Sylphari": -10,
            "Frostling": -5
        }
    },
    "Stonekin": {
        "abilities": ["Stone Form", "Earthen Resilience"],
        "skills": ["Athletics", "Nature"],
        "feats": ["Earthbound"],
        "spells": [],
        "resistances": {"bludgeoning": 0.5},
        "proficiencies": ["Heavy Armor", "Hammers"],
        "movement": 25,
        "visibility": {"darkvision": 60},
        "disposition": {
            "Drakari": 5,
            "Frostling": 0,
            "Humara": -5
        }
    },
    "Sylphari": {
        "abilities": ["Wind Step", "Aerial Grace"],
        "skills": ["Acrobatics", "Perception"],
        "feats": [],
        "spells": ["Gust", "Feather Fall"],
        "resistances": {"lightning": 0.5},
        "proficiencies": ["Light Armor", "Bows"],
        "movement": 35,
        "visibility": {"darkvision": 30},
        "disposition": {
            "Drakari": -10,
            "Frostling": 5,
            "Minfolk": 10
        }
    },
    "Frostling": {
        "abilities": ["Frozen Resilience", "Glacial Presence"],
        "skills": ["Arcana", "Athletics"],
        "feats": [],
        "spells": ["Ice Knife", "Frost Shield"],
        "resistances": {"cold": 0.5},
        "proficiencies": ["Light Armor", "Spears"],
        "movement": 30,
        "visibility": {"darkvision": 60},
        "disposition": {
            "Drakari": -5,
            "Humara": 0,
            "Merfolk": 10
        }
    },
    "Halfian": {
        "abilities": ["Lucky", "Nimble"],
        "skills": ["Stealth", "Deception"],
        "feats": [],
        "spells": [],
        "resistances": {},
        "proficiencies": ["Simple Weapons", "Shortswords"],
        "movement": 25,
        "visibility": {"darkvision": 0},
        "disposition": {
            "Sylphari": 10,
            "Tauren": -5,
            "Shadeborn": 5
        }
    },
    "Minfolk": {
        "abilities": ["Quick Reflexes", "Agile Mind"],
        "skills": ["Acrobatics", "Sleight of Hand"],
        "feats": [],
        "spells": [],
        "resistances": {},
        "proficiencies": ["Daggers", "Crossbows"],
        "movement": 30,
        "visibility": {"darkvision": 0},
        "disposition": {
            "Sylphari": 10,
            "Humara": 5,
            "Orcane": -5
        }
    },
    "Orcane": {
        "abilities": ["Savage Attack", "Unyielding"],
        "skills": ["Athletics", "Intimidation"],
        "feats": [],
        "spells": [],
        "resistances": {"poison": 0.5},
        "proficiencies": ["Heavy Weapons", "Medium Armor"],
        "movement": 30,
        "visibility": {"darkvision": 60},
        "disposition": {
            "Drakari": 5,
            "Shadeborn": -10,
            "Humara": -5
        }
    },
    "Humara": {
        "abilities": ["Adaptable", "Resilient"],
        "skills": ["Any"],
        "feats": [],
        "spells": [],
        "resistances": {},
        "proficiencies": ["Any"],
        "movement": 30,
        "visibility": {"darkvision": 0},
        "disposition": {
            "Drakari": 0,
            "Frostling": 0,
            "Merfolk": 0
        }
    },
    "Shadeborn": {
        "abilities": ["Shadowmeld", "Silent Step"],
        "skills": ["Stealth", "Perception"],
        "feats": [],
        "spells": ["Darkness", "Shadow Blade"],
        "resistances": {"necrotic": 0.5},
        "proficiencies": ["Daggers", "Light Armor"],
        "movement": 30,
        "visibility": {"darkvision": 120},
        "disposition": {
            "Drakari": -5,
            "Humara": 5,
            "Orcane": -10
        }
    },
    "Aetherborn": {
        "abilities": ["Ethereal Step", "Void Resistance"],
        "skills": ["Arcana", "Insight"],
        "feats": [],
        "spells": ["Blink", "Misty Step"],
        "resistances": {"force": 0.5},
        "proficiencies": ["Light Armor", "Staffs"],
        "movement": 30,
        "visibility": {"darkvision": 60},
        "disposition": {
            "Shadeborn": -10,
            "Lumidar": 5,
            "Feykin": 0
        }
    },
    "Lumidar": {
        "abilities": ["Radiant Aura", "Light Manipulation"],
        "skills": ["Perception", "Stealth"],
        "feats": [],
        "spells": ["Daylight", "Illusory Light"],
        "resistances": {"radiant": 0.5, "necrotic": 1.5},
        "proficiencies": ["Light Armor", "Shortbows"],
        "movement": 35,
        "visibility": {"darkvision": 60},
        "disposition": {
            "Drakari": -10,
            "Humara": 5,
            "Merfolk": 0
        }
    },
    "Feykin": {
        "abilities": ["Fey Charm", "Trickster"],
        "skills": ["Deception", "Nature"],
        "feats": [],
        "spells": ["Charm Person", "Invisibility"],
        "resistances": {"charm": 0.5},
        "proficiencies": ["Bows", "Daggers"],
        "movement": 30,
        "visibility": {"darkvision": 60},
        "disposition": {
            "Drakari": 0,
            "Humara": 10,
            "Sylphari": 5
        }
    },
    "Tauren": {
        "abilities": ["Horns", "Stampede"],
        "skills": ["Athletics", "Intimidation"],
        "feats": [],
        "spells": [],
        "resistances": {"bludgeoning": 0.5},
        "proficiencies": ["Heavy Armor", "Maces"],
        "movement": 30,
        "visibility": {"darkvision": 30},
        "disposition": {
            "Drakari": 5,
            "Humara": 0,
            "Halfian": -5
        }
    },
    "Merfolk": {
        "abilities": ["Aquatic Adaptation", "Underwater Breathing"],
        "skills": ["Athletics", "Perception"],
        "feats": [],
        "spells": ["Water Breathing", "Create Water"],
        "resistances": {"cold": 0.5},
        "proficiencies": ["Spears", "Nets"],
        "movement": 30,
        "visibility": {"darkvision": 60},
        "disposition": {
            "Drakari": 0,
            "Frostling": 10,
            "Sylphari": 5
        }
    }
}


# List of available classes
classes = [
    "Berserker",
    "Minstrel",
    "Diviner",
    "Naturebinder",
    "Warrior",
    "Ascetic",
    "Knight",
    "Pathfinder",
    "Shadow",
    "Mage",
    "Enchanter",
    "Spellbinder",
    "Artificer",
    "Warden",
    "Shaman",
    "Psion",
    "Reaver",
]

class_stats = {
    "Berserker": {
        "str": 2,
        "dex": 1,
        "con": 1,
        "int": 0,
        "wis": 0,
        "cha": 0,
        "abilities": ["Rage", "Unstoppable"],
        "skills": ["Athletics", "Intimidation"],
        "feats": [],
        "spells": [],
        "proficiencies": ["Martial Weapons", "Heavy Armor"],
        "resource_points": 3
    },
    "Minstrel": {
        "str": 0,
        "dex": 1,
        "con": 0,
        "int": 1,
        "wis": 0,
        "cha": 2,
        "abilities": ["Inspiring Song", "Lyrical Charm"],
        "skills": ["Performance", "Persuasion"],
        "feats": [],
        "spells": ["Song of Inspiration"],
        "proficiencies": ["Light Armor", "Instruments"],
        "resource_points": 2
    },
    "Diviner": {
        "str": 0,
        "dex": 0,
        "con": 0,
        "int": 2,
        "wis": 1,
        "cha": 0,
        "abilities": ["Future Sight", "Arcane Knowledge"],
        "skills": ["Arcana", "Insight"],
        "feats": [],
        "spells": ["Augury", "Detect Magic"],
        "proficiencies": ["Light Armor", "Arcane Focus"],
        "resource_points": 3
    },
    "Naturebinder": {
        "str": 0,
        "dex": 0,
        "con": 1,
        "int": 0,
        "wis": 2,
        "cha": 0,
        "abilities": ["Summon Familiar", "Nature's Wrath"],
        "skills": ["Nature", "Survival"],
        "feats": [],
        "spells": ["Entangle", "Goodberry"],
        "proficiencies": ["Simple Weapons", "Druidic Focus"],
        "resource_points": 4
    },
    "Warrior": {
        "str": 2,
        "dex": 1,
        "con": 1,
        "int": 0,
        "wis": 0,
        "cha": 0,
        "abilities": ["Power Strike", "Shield Block"],
        "skills": ["Athletics", "Perception"],
        "feats": [],
        "spells": [],
        "proficiencies": ["Martial Weapons", "Medium Armor"],
        "resource_points": 2
    },
    "Ascetic": {
        "str": 1,
        "dex": 2,
        "con": 1,
        "int": 0,
        "wis": 1,
        "cha": 0,
        "abilities": ["Inner Focus", "Self-Heal"],
        "skills": ["Acrobatics", "Religion"],
        "feats": [],
        "spells": [],
        "proficiencies": ["Unarmed Combat", "Simple Weapons"],
        "resource_points": 3
    },
    "Knight": {
        "str": 2,
        "dex": 0,
        "con": 2,
        "int": 0,
        "wis": 0,
        "cha": 1,
        "abilities": ["Shield Wall", "Inspiring Presence"],
        "skills": ["History", "Athletics"],
        "feats": [],
        "spells": [],
        "proficiencies": ["Heavy Armor", "Martial Weapons"],
        "resource_points": 4
    },
    "Pathfinder": {
        "str": 1,
        "dex": 2,
        "con": 1,
        "int": 0,
        "wis": 1,
        "cha": 0,
        "abilities": ["Trailblazer", "Trapper"],
        "skills": ["Survival", "Stealth"],
        "feats": [],
        "spells": [],
        "proficiencies": ["Light Armor", "Ranged Weapons"],
        "resource_points": 3
    },
    "Shadow": {
        "str": 0,
        "dex": 2,
        "con": 0,
        "int": 1,
        "wis": 0,
        "cha": 1,
        "abilities": ["Shadow Step", "Backstab"],
        "skills": ["Stealth", "Deception"],
        "feats": [],
        "spells": [],
        "proficiencies": ["Light Armor", "Daggers"],
        "resource_points": 2
    },
    "Mage": {
        "str": 0,
        "dex": 0,
        "con": 0,
        "int": 2,
        "wis": 0,
        "cha": 1,
        "abilities": ["Fireball", "Arcane Shield"],
        "skills": ["Arcana", "History"],
        "feats": [],
        "spells": ["Magic Missile", "Shield"],
        "proficiencies": ["Light Armor", "Wands"],
        "resource_points": 5
    },
    "Enchanter": {
        "str": 0,
        "dex": 0,
        "con": 0,
        "int": 1,
        "wis": 1,
        "cha": 2,
        "abilities": ["Charm", "Suggestion"],
        "skills": ["Persuasion", "Arcana"],
        "feats": [],
        "spells": ["Charm Person", "Enthrall"],
        "proficiencies": ["Light Armor", "Instruments"],
        "resource_points": 3
    },
    "Spellbinder": {
        "str": 0,
        "dex": 1,
        "con": 0,
        "int": 2,
        "wis": 0,
        "cha": 1,
        "abilities": ["Mana Lock", "Counterspell"],
        "skills": ["Arcana", "Insight"],
        "feats": [],
        "spells": ["Dispel Magic", "Counterspell"],
        "proficiencies": ["Light Armor", "Arcane Focus"],
        "resource_points": 4
    },
    "Artificer": {
        "str": 0,
        "dex": 1,
        "con": 0,
        "int": 2,
        "wis": 0,
        "cha": 1,
        "abilities": ["Craft Magic Item", "Tinker"],
        "skills": ["Arcana", "Investigation"],
        "feats": [],
        "spells": ["Identify", "Magic Weapon"],
        "proficiencies": ["Medium Armor", "Tools"],
        "resource_points": 3
    },
    "Warden": {
        "str": 2,
        "dex": 0,
        "con": 2,
        "int": 0,
        "wis": 1,
        "cha": 0,
        "abilities": ["Defender's Shield", "Fortress"],
        "skills": ["Athletics", "Survival"],
        "feats": [],
        "spells": [],
        "proficiencies": ["Heavy Armor", "Martial Weapons"],
        "resource_points": 4
    },
    "Shaman": {
        "str": 0,
        "dex": 0,
        "con": 1,
        "int": 0,
        "wis": 2,
        "cha": 1,
        "abilities": ["Totem Call", "Spirit Walk"],
        "skills": ["Nature", "Insight"],
        "feats": [],
        "spells": ["Healing Wave", "Lightning Bolt"],
        "proficiencies": ["Light Armor", "Totems"],
        "resource_points": 4
    },
    "Psion": {
        "str": 0,
        "dex": 0,
        "con": 0,
        "int": 2,
        "wis": 1,
        "cha": 1,
        "abilities": ["Telekinesis", "Mind Blast"],
        "skills": ["Arcana", "Deception"],
        "feats": [],
        "spells": ["Mind Spike", "Psychic Scream"],
        "proficiencies": ["Light Armor", "Psychic Focus"],
        "resource_points": 5
    },
    "Reaver": {
        "str": 2,
        "dex": 1,
        "con": 2,
        "int": 0,
        "wis": 0,
        "cha": 0,
        "abilities": ["Life Drain", "Blood Fury"],
        "skills": ["Athletics", "Intimidation"],
        "feats": [],
        "spells": [],
        "proficiencies": ["Martial Weapons", "Medium Armor"],
        "resource_points": 3
    }
}


# Creates instances of Melee_Item class with name, description, value, damage, damage_type, poisoned, enchant as arguments
melee_items = {
    "Sword": i.Melee_Item(
        "Sword",
        "A sword, a radiant emblem of timeless valor and ardent passion.",
        5,
        dice_Roll.roll_d6(),
        "Slashing",
        False,
        None
    ),
    "Axe": i.Melee_Item(
        "Axe",
        "An axe, a rugged embodiment of unyielding strength and untamed spirit.",
        8,
        dice_Roll.roll_d8(),
        "Slashing",
        False,
        None
    ),
    "Spear": i.Melee_Item(
        "Spear",
        "A spear, a poised extension of precision and swiftness.",
        6,
        dice_Roll.roll_d6(),
        "Piercing",
        False,
        None
    ),
    "Dagger": i.Melee_Item(
        "Dagger",
        "A dagger, a clandestine whisper in the night, wields both elegance and treachery.",
        4,
        dice_Roll.roll_d4(),
        "Piercing",
        False,
        None
    ),
    "Fist": i.Melee_Item(
        "Fist",
        "A fist, an embodiment of raw power.",
        0,
        1,
        "Blunt",
        False,
        None
    ),
    "Hammer": i.Melee_Item(
        "Hammer",
        "A hammer, a mighty embodiment of thunderous strength and unrelenting force.",
        8,
        dice_Roll.roll_d8(),
        "Bludgeoning",
        False,
        None
    ),
    "Flail": i.Melee_Item(
        "Flail",
        "A flail, a weapon of unpredictable arcs and crushing blows.",
        7,
        dice_Roll.roll_d8(),
        "Bludgeoning",
        False,
        None
    ),
    "Halberd": i.Melee_Item(
        "Halberd",
        "A halberd, combining the reach of a spear with the chopping power of an axe.",
        10,
        dice_Roll.roll_d10(),
        "Slashing",
        False,
        None
    ),
    "Rapier": i.Melee_Item(
        "Rapier",
        "A rapier, slender and sharp, perfect for swift and precise strikes.",
        6,
        dice_Roll.roll_d8(),
        "Piercing",
        False,
        None
    ),
    "Warhammer": i.Melee_Item(
        "Warhammer",
        "A warhammer, designed to crush armor and bone alike.",
        9,
        dice_Roll.roll_d8(),
        "Bludgeoning",
        False,
        None
    ),
    "Quarterstaff": i.Melee_Item(
        "Quarterstaff",
        "A quarterstaff, simple yet versatile, favored by monks and travelers.",
        2,
        dice_Roll.roll_d6(),
        "Bludgeoning",
        False,
        None
    ),
}

# Random names
name_list = [
    "Aarav", "Ada", "Aelius", "Aiko", "Aisling", "Akari", "Amara", "Ananda",
    "Anders", "Anika", "Aruna", "Aya", "Bastian", "Camila", "Cassia",
    "Ciaran", "Dalia", "Darian", "Eamon", "Eira", "Eirik", "Eliana",
    "Enara", "Esme", "Finnian", "Freya", "Giselle", "Hakan", "Hiroshi",
    "Idris", "Iliana", "Inara", "Isolde", "Jasmin", "Kai", "Kaia",
    "Kamila", "Kiran", "Lakshmi", "Leif", "Lilja", "Lucien", "Maeve",
    "Malik", "Maya", "Milan", "Mira", "Nadia", "Nikola", "Nina", "Orion",
    "Paloma", "Ravi", "Rhea", "Rohan", "Rosalind", "Sana", "Sasha",
    "Soren", "Suri", "Tara", "Tavian", "Thalia", "Uma", "Veda", "Vikram",
    "Xander", "Yara", "Yusuf", "Zara", "Zia", "Alessio", "Amaya",
    "Ananya", "Anouk", "Ari", "Asher", "Astrid", "Avi", "Azalea", "Bijan",
    "Bodhi", "Cassian", "Chiara", "Daliah", "Darius", "Elara", "Elina",
    "Emil", "Emira", "Eva", "Felix", "Flora", "Gia", "Gwyn", "Hiro",
    "Iris", "Isra", "Jaya", "Juno", "Kaden", "Kaya", "Keira", "Khalil",
    "Lana", "Lev", "Lilith", "Linnea", "Lucia", "Lyra", "Marin", "Milo",
    "Nadia", "Niamh", "Nyla", "Orin", "Pasha", "Rafael", "Raya", "Ren",
    "Rhian", "Sage", "Selene", "Seren", "Sylvan", "Talia", "Tavi", "Vera",
    "Wren", "Zayn",
    "Zephyr", "Rowan", "Kieran", "Elowen", "Arwen", "Lysander", "Evander",
    "Cassiopeia", "Orla", "Lucius", "Cyrus", "Daphne", "Evelyn", "Gideon",
    "Isadora", "Julian", "Leona", "Magnus", "Naomi", "Oliver", "Penelope",
    "Quentin", "Rosalie", "Sebastian", "Thea", "Ulric", "Viola", "Willem",
    "Xanthe", "Yvette", "Zachariah",
]

# Commoner jobs
jobs = [
    'Farmer', 'Blacksmith', 'Carpenter', 'Baker', 'Tailor', 'Fisherman',
    'Miner', 'Woodcutter', 'Merchant', 'Innkeeper', 'Barber', 'Miller',
    'Potter', 'Brewer', 'Butcher', 'Mason', 'Scribe', 'Tanner',
    'Herbalist', 'Messenger', 'Stablehand', 'Servant', 'Street Vendor',
    'Town Crier', 'Cartographer', 'Guard', 'Town Guard', 'Jeweler',
    'Weaver', 'Bard', 'Sailor', 'Alchemist', 'Chandler', 'Chronicler',
    'Clothier', 'Cobbler', 'Fletcher', 'Glassblower', 'Locksmith',
    'Silversmith', 'Wainwright', 'Apothecary', 'Bookbinder', 'Dyer',
    'Falconer', 'Goldsmith', 'Shepherd', 'Spice Trader', 'Tax Collector',
    'Tutor',
]

# Monster types
monster_type_list = [
    "aberration", "beast", "celestial", "construct", "dragon",
    "elemental", "fey", "giant", "humanoid", "monstrosity",
    "ooze", "undead", "plant", "fiend",
]

# Monsters with types as values
monster_dict = {
    # Aberrations
    "Zyphor": "aberration",
    "Mindlurker": "aberration",
    "Glimmering Eye": "aberration",
    "Whisperfiend": "aberration",
    "Abyssal Spawn": "aberration",
    "Thoughtweaver": "aberration",
    "Shadowspawn": "aberration",
    "Voidwalker": "aberration",
    "Deep Echo": "aberration",
    "Lumifluff": "aberration",
    # Beasts
    "Dire Wolf": "beast",
    "Saber-Toothed Tiger": "beast",
    "Giant Eagle": "beast",
    "Giant Spider": "beast",
    "Mammoth": "beast",
    "Rhinoceros": "beast",
    "Polar Bear": "beast",
    "Giant Crocodile": "beast",
    "Giant Scorpion": "beast",
    "Giant Constrictor Snake": "beast",
    # Celestials
    "Solaris": "celestial",
    "Planetar": "celestial",
    "Devac": "celestial",
    "Couatl": "celestial",
    "Unicorn": "celestial",
    "Pegasus": "celestial",
    "Ki-rin": "celestial",
    "Hound Archon": "celestial",
    "Lammasu": "celestial",
    "Eagle Archon": "celestial",
    # Constructs
    "Iron Golem": "construct",
    "Shield Guardian": "construct",
    "Clay Golem": "construct",
    "Flesh Golem": "construct",
    "Stone Golem": "construct",
    "Animated Armor": "construct",
    "Homunculus": "construct",
    "Gorgon": "construct",
    "Scarecrow": "construct",
    "Helmed Horror": "construct",
    # Dragons
    "Ancient Red Dragon": "dragon",
    "Adult Gold Dragon": "dragon",
    "Young Silver Dragon": "dragon",
    "Wyrmling Black Dragon": "dragon",
    "Shadow Dragon": "dragon",
    "Dragon Turtle": "dragon",
    "Dracolich": "dragon",
    "Faerie Dragon": "dragon",
    "Pseudodragon": "dragon",
    "Wyvern": "dragon",
    # Elementals
    "Fire Elemental": "elemental",
    "Water Elemental": "elemental",
    "Air Elemental": "elemental",
    "Earth Elemental": "elemental",
    "Ice Elemental": "elemental",
    "Magma Elemental": "elemental",
    "Smoke Elemental": "elemental",
    "Steam Elemental": "elemental",
    "Lightning Elemental": "elemental",
    "Dust Elemental": "elemental",
    # Fey
    "Titania": "fey",
    "Oberon": "fey",
    "Pixie": "fey",
    "Satyr": "fey",
    "Dryad": "fey",
    "Nymph": "fey",
    "Green Hag": "fey",
    "Sprite": "fey",
    "Quickling": "fey",
    "Blink Dog": "fey",
    # Giants
    "Hill Giant": "giant",
    "Storm Giant": "giant",
    "Fire Giant": "giant",
    "Frost Giant": "giant",
    "Stone Giant": "giant",
    "Cloud Giant": "giant",
    "Death Giant": "giant",
    "Verbeeg": "giant",
    "Cyclops": "giant",
    "Fomorian": "giant",
    # Humanoids
    "Orc": "humanoid",
    "Goblin": "humanoid",
    "Kobold": "humanoid",
    "Hobgoblin": "humanoid",
    "Bugbear": "humanoid",
    "Troll": "humanoid",
    "Lizardfolk": "humanoid",
    "Kenku": "humanoid",
    "Gnoll": "humanoid",
    "Yin-ta": "humanoid",
    # Monstrosities
    "Kraken": "monstrosity",
    "Gorgon": "monstrosity",
    "Manticore": "monstrosity",
    "Bulette": "monstrosity",
    "Chimera": "monstrosity",
    "Hydra": "monstrosity",
    "Otyugh": "monstrosity",
    "Rust Monster": "monstrosity",
    "Umber Hulk": "monstrosity",
    "Hook Horror": "monstrosity",
    # Oozes
    "Gelatinous Cube": "ooze",
    "Black Pudding": "ooze",
    "Gray Ooze": "ooze",
    "Ochre Jelly": "ooze",
    "Slithering Tracker": "ooze",
    # Undead
    "Zombie": "undead",
    "Skeleton": "undead",
    "Ghoul": "undead",
    "Wight": "undead",
    "Vampire": "undead",
    "Lich": "undead",
    "Ghost": "undead",
    "Specter": "undead",
    "Banshee": "undead",
    "Wraith": "undead",
    # Plants
    "Shambling Mound": "plant",
    "Twig Blight": "plant",
    "Myconid": "plant",
    "Treant": "plant",
    "Vine Blight": "plant",
    # Fiends
    "Imp": "fiend",
    "Barbed Devil": "fiend",
    "Pit Fiend": "fiend",
    "Balor": "fiend",
    "Cambion": "fiend",
    "Succubus": "fiend",
    "Marilith": "fiend",
    "Horned Devil": "fiend",
    "Glabrezu": "fiend",
    "Quasit": "fiend",
}

new_locations = {
    # Town locations
    'towns': [
        {
            "name": "Smallville",
            "size": "small",
            "description": "A quiet, humble village nestled in the rolling hills. Known for its peaceful atmosphere and strong sense of community.",
            "inn": "The Cozy Hearth",
            "general_store": "Peddler's Corner",
            "flags": {
                "visited": False,
                "event_triggered": False
            },
            "npcs": []
        },
        {
            "name": "Midtown",
            "size": "medium",
            "description": "A bustling trade town at the crossroads of several major routes. The aroma of fresh-baked goods and the sound of merchants bartering fills the air.",
            "inn": "The Golden Griffin",
            "general_store": "Market Bazaar",
            "flags": {
                "visited": False,
                "event_triggered": False
            },
            "npcs": []
        },
        {
            "name": "Grand City",
            "size": "large",
            "description": "A sprawling metropolis surrounded by towering walls. The heart of commerce and governance in the region, teeming with intrigue and opportunity.",
            "inn": "The Royal Retreat",
            "general_store": "Emporium of Wonders",
            "flags": {
                "visited": False,
                "event_triggered": False
            },
            "npcs": []
        },
        {
            "name": "Riverside",
            "size": "small",
            "description": "A quaint riverside village where life flows as steadily as the gentle current. Renowned for its fishing festivals and hearty riverfolk.",
            "inn": "The Rusty Anchor",
            "general_store": "River's Edge Trading Post",
            "flags": {
                "visited": False,
                "event_triggered": False
            },
            "npcs": [
                {"name": "Hedric the Fisherman", "role": "Elder Villager", "description": "An old but wise fisherman, known for his tales of river spirits."}
            ]
        },
        {
            "name": "Misty Hollow",
            "size": "medium",
            "description": "Nestled in a dense forest, Misty Hollow is cloaked in perpetual fog. Locals whisper of shadowy figures that linger just out of sight.",
            "inn": "The Whispering Willow",
            "general_store": "Mystic Emporium",
            "flags": {
                "visited": False,
                "event_triggered": False
            },
            "npcs": [
                {"name": "Elenna Farseer", "role": "Seer", "description": "A mysterious woman who claims to interpret the whispers of the mist."}
            ]
        },
        {
            "name": "Sunvale",
            "size": "small",
            "description": "A sunny hamlet surrounded by golden fields. Known for its warm-hearted folk and sunflower festivals.",
            "inn": "The Rising Sun Inn",
            "general_store": "Sunvale Supplies",
            "flags": {
                "visited": False,
                "event_triggered": False
            },
            "npcs": [
                {"name": "Tarin Brightfield", "role": "Blacksmith", "description": "A cheerful smith whose laughter echoes through the village."}
            ]
        },
        {
            "name": "Shadowport",
            "size": "large",
            "description": "A sprawling, dark harbor town with an undercurrent of danger. Smugglers and rogues frequent its shadowy docks.",
            "inn": "The Moonlit Maiden",
            "general_store": "Shadowport Market",
            "flags": {
                "visited": False,
                "event_triggered": False
            },
            "npcs": [
                {"name": "Captain Thane", "role": "Pirate Lord", "description": "The feared but respected leader of the Shadowport docks."}
            ]
        },
        {
            "name": "Eagle's Peak",
            "size": "medium",
            "description": "Perched high in the mountains, this town offers breathtaking views and hosts the annual Skyborn Festival.",
            "inn": "The Soaring Eagle",
            "general_store": "Peak Provisions",
            "flags": {
                "visited": False,
                "event_triggered": False
            },
            "npcs": [
                {"name": "Highkeeper Aeron", "role": "Priest", "description": "Caretaker of the temple dedicated to the sky gods."}
            ]
        },
        {
            "name": "Verdant Grove",
            "size": "small",
            "description": "A serene village surrounded by lush greenery. The people here live in harmony with nature and protect sacred groves.",
            "inn": "The Green Leaf",
            "general_store": "Grove Goods",
            "flags": {
                "visited": False,
                "event_triggered": False
            },
            "npcs": [
                {"name": "Sylra Greenthorn", "role": "Herbalist", "description": "A kind soul who brews potions using ancient herbal recipes."}
            ]
        },
        {
            "name": "Ironforge",
            "size": "large",
            "description": "A massive industrial city powered by roaring furnaces. Its streets are lined with blacksmiths and artificers.",
            "inn": "The Hammered Anvil",
            "general_store": "Forge Finds",
            "flags": {
                "visited": False,
                "event_triggered": False
            },
            "npcs": [
                {"name": "Vorrik Ironhand", "role": "Master Smith", "description": "A gruff but skilled blacksmith, revered for crafting legendary weapons."}
            ]
        }
    ],

    # Cave locations
        'caves': [
        {
            "name": "Shadowfang Cavern",
            "size": "small",
            "description": "A dark and narrow cave where shadows seem to move on their own. Whispers echo faintly in the distance.",
            "flags": {
                "trap_disarmed": False,
                "explored": False
            },
            "npcs": [
                {"name": "Thalra Shadowstep", "role": "Rogue", "description": "A shadowy figure searching for a cursed dagger said to be hidden in the cave."}
            ]
        },
        {
            "name": "Crystal Depths",
            "size": "large",
            "description": "A magnificent cavern filled with luminescent crystals. Their soft glow lights the way, but the air feels heavy with danger.",
            "flags": {
                "trap_disarmed": False,
                "explored": False
            },
            "npcs": [
                {"name": "Gilda Brightstone", "role": "Miner", "description": "An ambitious miner drawn to the crystals' beauty but unaware of the lurking dangers."}
            ]
        },
        {
            "name": "The Abyssal Gate",
            "size": "large",
            "description": "A foreboding portal deep within a cavern that hums with otherworldly energy. Legends say it leads to another plane.",
            "flags": {
                "gate_activated": False,
                "enemy_vanquished": False
            },
            "npcs": [
                {"name": "High Seer Aldric", "role": "Scholar", "description": "A frail scholar hoping to study the portal but unprepared for its guardians."}
            ]
        },
        {
            "name": "Whispering Grotto",
            "size": "medium",
            "description": "A cavern where the wind carries whispers of ancient secrets. The walls seem to shimmer faintly, hiding unseen dangers.",
            "flags": {
                "echo_trap_triggered": False,
                "hidden_chamber_found": False
            },
            "npcs": [
                {"name": "Lyra Windspeaker", "role": "Bard", "description": "A traveling bard seeking inspiration from the grotto's mysterious whispers."}
            ]
        },
        {
            "name": "Mossy Hollows",
            "size": "small",
            "description": "A damp cave overgrown with moss and fungi. The air is thick with the smell of decay and earthy growth.",
            "flags": {
                "trap_disarmed": False,
                "explored": False
            },
            "npcs": [
                {"name": "Fynra Greenroot", "role": "Herbalist", "description": "A reclusive herbalist harvesting rare plants for her potions."}
            ]
        },
        {
            "name": "Echoing Abyss",
            "size": "large",
            "description": "A cavern with an endless echo, making it hard to distinguish reality from illusion. It is said that time itself warps here.",
            "flags": {
                "time_distortion_detected": False,
                "artifact_found": False
            },
            "npcs": [
                {"name": "Korin Timebinder", "role": "Chronomancer", "description": "A rogue mage investigating the abyss' time-warping properties."}
            ]
        },
        {
            "name": "Dragon's Maw",
            "size": "large",
            "description": "A cavern shaped like a massive dragon's head. The bones of ancient creatures lie scattered on the floor.",
            "flags": {
                "dragon_awakened": False,
                "hoard_claimed": False
            },
            "npcs": [
                {"name": "Draknor", "role": "Dragon", "description": "A slumbering dragon who guards a treasure hoard deep within the maw."}
            ]
        },
        {
            "name": "Serpent's Tunnels",
            "size": "medium",
            "description": "A labyrinth of twisting tunnels that resemble a snake’s coils. Venomous creatures lurk in the shadows.",
            "flags": {
                "serpents_defeated": False,
                "treasure_found": False
            },
            "npcs": [
                {"name": "Nerithis", "role": "Serpent Cultist", "description": "A fanatical cultist protecting the sacred serpent altar."}
            ]
        },
        {
            "name": "Forgotten Mine",
            "size": "small",
            "description": "An abandoned mine where the tools of old laborers still rest. A faint smell of brimstone lingers in the air.",
            "flags": {
                "mine_cleared": False,
                "hidden_vein_discovered": False
            },
            "npcs": [
                {"name": "Jorin Hammerfall", "role": "Ex-Miner", "description": "A former miner seeking closure after losing his crew to a cave-in."}
            ]
        },
        {
            "name": "Ancient Catacombs",
            "size": "large",
            "description": "A labyrinth of burial chambers filled with the remains of forgotten kings. The air is thick with the weight of history.",
            "flags": {
                "undead_vanquished": False,
                "relic_retrieved": False
            },
            "npcs": [
                {"name": "Esmira Lightbringer", "role": "Paladin", "description": "A devout paladin on a quest to banish the undead from the catacombs."}
            ]
        },
        {
            "name": "Glittering Caverns",
            "size": "medium",
            "description": "A breathtaking cave with walls that glisten as if encrusted with diamonds. The beauty hides treacherous paths and deadly traps.",
            "flags": {
                "gem_collected": False,
                "trap_disarmed": False
            },
            "npcs": [
                {"name": "Zerik Gemcutter", "role": "Treasure Hunter", "description": "A daring treasure hunter willing to risk everything for glittering riches."}
            ]
        }
    ],

    # Bandit camp locations
    'bandit camps': [
        {
            "name": "Raven's Roost",
            "size": "small",
            "description": "A hidden camp perched high in the cliffs, accessible only by a narrow path. Bandit lookouts keep watch day and night.",
            "flags": {
                "bandits_defeated": False,
                "loot_collected": False
            },
            "npcs": [
                {"name": "Garin Stormeye", "role": "Bandit Leader", "description": "A sharp-eyed rogue who commands the roost with cunning and cruelty."}
            ]
        },
        {
            "name": "Serpent's Hideout",
            "size": "large",
            "description": "A sprawling encampment deep in the woods, fortified with crude barricades and traps. The air is thick with the scent of smoke.",
            "flags": {
                "bandits_defeated": False,
                "loot_collected": False
            },
            "npcs": [
                {"name": "Korra Venomfang", "role": "Bandit Alchemist", "description": "A devious alchemist who creates potent poisons to guard the hideout."}
            ]
        },
        {
            "name": "Blackthorn Encampment",
            "size": "medium",
            "description": "Nestled in a dense thicket of blackthorn trees, this camp is a natural fortress with spiked barricades and thorny defenses.",
            "flags": {
                "bandits_defeated": False,
                "loot_collected": False
            },
            "npcs": [
                {"name": "Tharik Blackthorn", "role": "Bandit Captain", "description": "A ruthless captain who uses the forest's natural defenses to his advantage."}
            ]
        },
        {
            "name": "Viper's Den",
            "size": "small",
            "description": "A hidden underground lair where venomous creatures roam freely. The bandits use the natural dangers to ward off intruders.",
            "flags": {
                "bandits_defeated": False,
                "loot_collected": False
            },
            "npcs": [
                {"name": "Zethis Fang", "role": "Venom Master", "description": "A cunning bandit who uses trained vipers to protect the den."}
            ]
        },
        {
            "name": "Daggerfall Outpost",
            "size": "large",
            "description": "A heavily fortified outpost built on the ruins of an old watchtower. It serves as a strategic base for raiding nearby towns.",
            "flags": {
                "bandits_defeated": False,
                "loot_collected": False
            },
            "npcs": [
                {"name": "Captain Valrik", "role": "Outpost Commander", "description": "A seasoned warrior who trains bandits to become disciplined raiders."}
            ]
        },
        {
            "name": "Crimson Camp",
            "size": "medium",
            "description": "An encampment stained red by the bandits' ruthless deeds. Bloodied banners fly high as a warning to intruders.",
            "flags": {
                "bandits_defeated": False,
                "loot_collected": False
            },
            "npcs": [
                {"name": "Ildra Bloodbane", "role": "Bandit Warlord", "description": "A fearsome leader known for her brutality and skill with a blade."}
            ]
        },
        {
            "name": "Shadow Hideaway",
            "size": "small",
            "description": "A secluded cave that blends into the shadows of the surrounding cliffs. Bandits here excel in stealth and ambush tactics.",
            "flags": {
                "bandits_defeated": False,
                "loot_collected": False
            },
            "npcs": [
                {"name": "Nyra Shadowcloak", "role": "Assassin", "description": "A silent and deadly assassin who strikes from the shadows."}
            ]
        },
        {
            "name": "Ironclaw Base",
            "size": "large",
            "description": "A sprawling camp built with reinforced walls and steel gates. The bandits here are heavily armed and well-organized.",
            "flags": {
                "bandits_defeated": False,
                "loot_collected": False
            },
            "npcs": [
                {"name": "Rorik Ironclaw", "role": "Warlord", "description": "A hulking brute who rules the base with an iron fist and unmatched strength."}
            ]
        },
        {
        "name": "Silent Knoll",
        "size": "medium",
        "description": "A quiet hilltop camp overlooking a major trade route. Its eerie silence is broken only by the sound of bandits sharpening their blades.",
        "flags": {
            "bandits_defeated": False,
            "loot_collected": False
        },
        "npcs": [
            {"name": "Eris Daggerhand", "role": "Scoutmaster", "description": "A master of ambushes who ensures no caravan escapes unscathed."}
        ]
    },
    {
        "name": "Broken Blade Camp",
        "size": "small",
        "description": "A derelict camp where discarded weapons litter the ground. Despite its state, the bandits here are desperate and dangerous.",
        "flags": {
            "bandits_defeated": False,
            "loot_collected": False
        },
        "npcs": [
            {"name": "Rykard Shattersteel", "role": "Veteran Fighter", "description": "A grizzled veteran who has seen too many battles but refuses to back down."}
        ]
    }
],
    # Roadside locations
    'roadside locations': [
        {
            "name": "Crossroads Rest",
            "size": "small",
            "description": "A quiet waystation where weary travelers pause to rest. A weathered signpost points in four directions.",
            "flags": {
                "visited": False,
                "special_event_triggered": False
            },
            "npcs": [
                {"name": "Old Marris", "role": "Caretaker", "description": "A kind old man who maintains the waystation and shares tales of passing adventurers."}
            ]
        },
        {
            "name": "Wagon Wheel Waystation",
            "size": "small",
            "description": "A bustling roadside stop with a creaky windmill and a smithy for repairing wagons and gear.",
            "flags": {
                "visited": False,
                "special_event_triggered": False
            },
            "npcs": [
                {"name": "Lerik Ironspoke", "role": "Blacksmith", "description": "A hardworking blacksmith who specializes in fixing wagon wheels and crafting tools."}
            ]
        },
        {
            "name": "Traveller's Haven",
            "size": "small",
            "description": "A small inn at the edge of a dense forest, offering refuge for travelers before they venture deeper into the wilderness.",
            "flags": {
                "visited": False,
                "special_event_triggered": False
            },
            "npcs": [
                {"name": "Elyra Dawnshade", "role": "Innkeeper", "description": "A gentle innkeeper who serves hearty meals and has a knack for calming nervous travelers."}
            ]
        },
        {
            "name": "Hillside Retreat",
            "size": "small",
            "description": "A cozy roadside lodge perched on a hill, offering breathtaking views of the valley below.",
            "flags": {
                "visited": False,
                "special_event_triggered": False
            },
            "npcs": [
                {"name": "Farrah Hillwatcher", "role": "Host", "description": "A friendly host who loves sharing stories about the valley's history."}
            ]
        },
        {
            "name": "Wayfarer's Rest",
            "size": "small",
            "description": "A rustic stop for travelers, known for its hot stew and roaring fireplace.",
            "flags": {
                "visited": False,
                "special_event_triggered": False
            },
            "npcs": [
                {"name": "Tobin Hearthstone", "role": "Cook", "description": "A jovial cook who takes pride in his signature stew, said to rejuvenate weary adventurers."}
            ]
        },
        {
            "name": "Lone Pine Inn",
            "size": "small",
            "description": "A solitary inn nestled beside a towering pine tree. Travelers swear the tree hums in the wind.",
            "flags": {
                "visited": False,
                "special_event_triggered": False
            },
            "npcs": [
                {"name": "Iris Windsong", "role": "Innkeeper", "description": "A mysterious innkeeper who claims to hear the tree’s whispers and shares cryptic advice."}
            ]
        },
        {
            "name": "Misty Meadows",
            "size": "small",
            "description": "A foggy field where an old tavern offers respite to lost travelers. The meadows hold an eerie calm.",
            "flags": {
                "visited": False,
                "special_event_triggered": False
            },
            "npcs": [
                {"name": "Gareth Fogwalker", "role": "Guide", "description": "A seasoned guide who knows the meadows' hidden paths and dangers."}
            ]
        },
        {
            "name": "Sunset Oasis",
            "size": "small",
            "description": "An inviting inn located in the heart of a golden plain, famous for its stunning sunsets and warm hospitality.",
            "flags": {
                "visited": False,
                "special_event_triggered": False
            },
            "npcs": [
                {"name": "Solara Brightvale", "role": "Innkeeper", "description": "A radiant innkeeper who welcomes all with a kind smile and a warm meal."}
            ]
        },
        {
            "name": "Twin Oaks Tavern",
            "size": "small",
            "description": "A quaint tavern surrounded by two towering oak trees. The atmosphere is lively and welcoming.",
            "flags": {
                "visited": False,
                "special_event_triggered": False
            },
            "npcs": [
                {"name": "Davin Oakroot", "role": "Tavern Owner", "description": "A jolly tavern owner who entertains patrons with tales of the twin oaks’ origins."}
            ]
        },
        {
            "name": "Roaming Rendezvous",
            "size": "small",
            "description": "A mobile caravan-turned-tavern that sets up shop wherever travelers gather.",
            "flags": {
                "visited": False,
                "special_event_triggered": False
            },
            "npcs": [
                {"name": "Mira Nomadheart", "role": "Caravan Leader", "description": "A free-spirited leader who shares stories and songs of her travels."}
            ]
        },
        {
            "name": "Silent Springs",
            "size": "small",
            "description": "A tranquil rest stop near a bubbling spring, known for its soothing waters and serene environment.",
            "flags": {
                "visited": False,
                "special_event_triggered": False
            },
            "npcs": [
                {"name": "Lirien Watersong", "role": "Caretaker", "description": "A calm caretaker who offers refreshing spring water to passing travelers."}
            ]
        },
        {
            "name": "Starlight Rest Stop",
            "size": "small",
            "description": "A serene stop under open skies, perfect for stargazing. It’s said that falling stars grant wishes here.",
            "flags": {
                "visited": False,
                "special_event_triggered": False
            },
            "npcs": [
                {"name": "Astren Skysoul", "role": "Stargazer", "description": "A mystic who guides travelers in reading the stars."}
            ]
        },
        {
            "name": "Hidden Hollow",
            "size": "small",
            "description": "A secluded retreat nestled in a forested hollow. The air is filled with the scent of wildflowers.",
            "flags": {
                "visited": False,
                "special_event_triggered": False
            },
            "npcs": [
                {"name": "Meyra Bloomfield", "role": "Healer", "description": "A gentle healer who uses herbs from the hollow to craft remedies."}
            ]
        },
        {
            "name": "Golden Fields Inn",
            "size": "small",
            "description": "An inn surrounded by golden wheat fields, known for its fresh bread and cheerful atmosphere.",
            "flags": {
                "visited": False,
                "special_event_triggered": False
            },
            "npcs": [
                {"name": "Harlin Goldenharvest", "role": "Baker", "description": "A jovial baker who offers free samples to weary travelers."}
            ]
        },
        {
            "name": "Riverside Retreat",
            "size": "small",
            "description": "A peaceful lodge overlooking a calm river, perfect for fishing and reflection.",
            "flags": {
                "visited": False,
                "special_event_triggered": False
            },
            "npcs": [
                {"name": "Wendall Riversage", "role": "Angler", "description": "A friendly angler who shares tips and stories about the river."}
            ]
        },
        {
            "name": "Forest's Edge",
            "size": "small",
            "description": "A rustic cabin at the edge of a dense forest, offering safety before venturing into the unknown.",
            "flags": {
                "visited": False,
                "special_event_triggered": False
            },
            "npcs": [
                {"name": "Kaelen Woodshade", "role": "Woodsman", "description": "A seasoned woodsman who warns travelers of dangers in the forest."}
            ]
        },
        {
            "name": "Desert Rose Inn",
            "size": "small",
            "description": "An oasis of comfort in the arid desert, known for its refreshing drinks and cool shade.",
            "flags": {
                "visited": False,
                "special_event_triggered": False
            },
            "npcs": [
                {"name": "Selah Sandbloom", "role": "Innkeeper", "description": "A hospitable innkeeper who provides shelter from the desert’s heat."}
            ]
        },
        {
            "name": "Mountain Pass Lodge",
            "size": "small",
            "description": "A sturdy lodge built into the mountainside, offering refuge to travelers braving the treacherous pass.",
            "flags": {
                "visited": False,
                "special_event_triggered": False
            },
            "npcs": [
                {"name": "Dorn Stonepath", "role": "Guide", "description": "A rugged guide who helps travelers navigate the mountain pass safely."}
            ]
        },
        {
            "name": "The Old Mill",
            "size": "small",
            "description": "An abandoned mill converted into a makeshift shelter. Its creaking blades whisper of bygone days.",
            "flags": {
                "visited": False,
                "special_event_triggered": False
            },
            "npcs": [
                {"name": "Edrin Wheelwright", "role": "Historian", "description": "A wandering historian seeking to uncover the mill’s secrets."}
            ]
        },
        {
            "name": "Windy Plains Outpost",
            "size": "small",
            "description": "A small outpost on a windswept plain, serving as a checkpoint for caravans and travelers alike.",
            "flags": {
                "visited": False,
                "special_event_triggered": False
            },
            "npcs": [
                {"name": "Captain Darric Gale", "role": "Outpost Guard", "description": "A diligent guard who ensures the safety of travelers passing through."}
            ]
        }
    ],
    # Story-critical locations
    'story_locations': [
        {
            "name": "Ebonspire Keep",
            "size": "large",
            "description": "The ruined stronghold of the antagonist, shrouded in mystery and brimming with danger. This marks the climax of the journey.",
            "flags": {
                "final_battle_triggered": False,
                "allies_recruited": False
            },
            "npcs": []
        },
        {
            "name": "Twilight Sanctuary",
            "size": "medium",
            "description": "An ancient temple hidden within the mountains. Its walls whisper secrets of the past and hold powerful artifacts.",
            "flags": {
                "artifact_collected": False,
                "ritual_completed": False
            },
            "npcs": []
        },
        {
            "name": "Blightwatch Outpost",
            "size": "medium",
            "description": "A reclaimed military post now serving as a rallying point for allies. Key for Act I progression.",
            "flags": {
                "outpost_reclaimed": False,
                "key_found": False
            },
            "npcs": []
        },
        {
            "name": "Shattered Grove",
            "size": "large",
            "description": "A corrupted forest pulsing with dark magic. Its heart holds the key to cleansing the land.",
            "flags": {
                "grove_cleansed": False,
                "npc_saved": False
            },
            "npcs": []
        },
        {
            "name": "Stormhaven Port",
            "size": "large",
            "description": "A bustling harbor town, central for trade and a pivotal transition to the next act.",
            "flags": {
                "ship_acquired": False,
                "pirates_defeated": False
            },
            "npcs": []
        },
        {
            "name": "Ashen Vale",
            "size": "large",
            "description": "A desolate battlefield filled with ancient relics. The truth behind the war lies buried here.",
            "flags": {
                "visions_seen": False,
                "artifact_discovered": False
            },
            "npcs": []
        },
        {
            "name": "Silent Peaks Monastery",
            "size": "small",
            "description": "A secluded sanctuary where wisdom is passed down. Key to the protagonist’s growth and training.",
            "flags": {
                "training_completed": False,
                "mentor_met": False
            },
            "npcs": []
        }
    ]
}


# Factions dictionary: Players, NPCs, or locations can adapt beliefs, join, or represent factions
# They will also have varying levels of hostility or helpfulness to certain factions who are rivals or allies
factions = {
    'order_of_the_silver_shield': {
        'name': 'Order of the Silver Shield',
        'alignment': 'Lawful Good',
        'description': 'The Order of the Silver Shield is a noble and chivalrous faction dedicated to protecting the innocent, upholding justice, and eradicating evil.',
        'allied_factions': ['circle_of_enchanters', 'guild_of_artisans'],
        'rival_factions': ['cult_of_the_shadow', 'brigands_of_the_crimson_eye'],
        'neutral_factions': [],
    },
    'circle_of_enchanters': {
        'name': 'Circle of Enchanters',
        'alignment': 'Neutral',
        'description': 'The Circle of Enchanters is a secretive faction of spellcasters who seek knowledge and the understanding of magical forces. They maintain balance and neutrality in their pursuits.',
        'allied_factions': ['order_of_the_silver_shield'],
        'rival_factions': ['cult_of_the_shadow', 'cabal_of_the_arcane_eye'],
        'neutral_factions': [],
    },
    'cult_of_the_shadow': {
        'name': 'Cult of the Shadow',
        'alignment': 'Chaotic Evil',
        'description': 'The Cult of the Shadow is a dark and sinister faction that worships forbidden powers and seeks to spread chaos and corruption throughout the land.',
        'allied_factions': ['brigands_of_the_crimson_eye'],
        'rival_factions': ['order_of_the_silver_shield', 'circle_of_enchanters'],
        'neutral_factions': [],
    },
    'guild_of_artisans': {
        'name': 'Guild of Artisans',
        'alignment': 'Lawful Neutral',
        'description': 'The Guild of Artisans is a faction comprising skilled craftsmen and artisans. They strive for excellence in their craft, preserving traditional methods, and promoting trade and prosperity.',
        'allied_factions': ['order_of_the_silver_shield'],
        'rival_factions': ['cabal_of_the_arcane_eye'],
        'neutral_factions': [],
    },
    'brigands_of_the_crimson_eye': {
        'name': 'Brigands of the Crimson Eye',
        'alignment': 'Chaotic Neutral',
        'description': 'The Brigands of the Crimson Eye are a notorious faction of thieves and mercenaries. They operate outside the law and are driven by personal gain and the thrill of adventure.',
        'allied_factions': ['cult_of_the_shadow'],
        'rival_factions': ['order_of_the_silver_shield'],
        'neutral_factions': ['circle_of_enchanters'],
    },
    'cabal_of_the_arcane_eye': {
        'name': 'Cabal of the Arcane Eye',
        'alignment': 'Neutral Evil',
        'description': 'The Cabal of the Arcane Eye is a secretive faction of power-hungry sorcerers and warlocks. They manipulate arcane forces for their own gain and seek to control the world.',
        'allied_factions': ['circle_of_enchanters'],
        'rival_factions': ['guild_of_artisans'],
        'neutral_factions': [],
    },
    'wardens_of_nature': {
        'name': 'Wardens of Nature',
        'alignment': 'Neutral Good',
        'description': 'The Wardens of Nature are guardians of the natural world, protecting forests, rivers, and wildlife from harm and exploitation.',
        'allied_factions': ['order_of_the_silver_shield'],
        'rival_factions': ['iron_fist_clan'],
        'neutral_factions': ['circle_of_enchanters'],
    },
    'iron_fist_clan': {
        'name': 'Iron Fist Clan',
        'alignment': 'Lawful Evil',
        'description': 'The Iron Fist Clan is a militaristic faction seeking to impose their rule through strength and discipline, valuing order above all.',
        'allied_factions': [],
        'rival_factions': ['wardens_of_nature', 'brigands_of_the_crimson_eye'],
        'neutral_factions': ['cabal_of_the_arcane_eye'],
    },
    'seekers_of_the_lost': {
        'name': 'Seekers of the Lost',
        'alignment': 'Chaotic Good',
        'description': 'Adventurers and explorers dedicated to uncovering lost knowledge and ancient artifacts for the benefit of all.',
        'allied_factions': ['guild_of_artisans', 'wardens_of_nature'],
        'rival_factions': ['cult_of_the_shadow'],
        'neutral_factions': ['circle_of_enchanters'],
    },
}

# Reward Items Table:
# This table contains various items that can be used as rewards for players in the game.
# Each item has a unique identifier (1-15) and includes a name, description, and value.
reward_items_table = {
    1: i.Item(
        "Health Potion",
        "A small vial containing a red liquid. When consumed, it restores health.",
        50
    ),
    2: i.Item(
        "Scroll of Insight",
        "A parchment containing mystical runes. Allows the identification of magical items.",
        75
    ),
    3: i.Item(
        "Lockpicks",
        "A set of tools used for picking locks. Essential for any rogue.",
        30
    ),
    4: i.Item(
        "Antidote Elixir",
        "A small vial containing a substance that provides advantage on saving throws against poison for 1 hour.",
        20
    ),
    5: i.Item(
        "Climber's Rope",
        "A 50-foot length of silk rope that can move at your command.",
        100
    ),
    6: i.Item(
        "Night Vision Goggles",
        "These goggles allow you to see in darkness as if it were dim light.",
        150
    ),
    7: i.Item(
        "Bag of Endless Storage",
        "This bag has an interior space considerably larger than its outside dimensions.",
        200
    ),
    8: i.Item(
        "Wand of Arcane Missiles",
        "A wand that can cast Arcane Missiles at varying levels.",
        250
    ),
    9: i.Item(
        "Ring of Feather Landing",
        "This ring negates any damage from falling.",
        120
    ),
    10: i.Item(
        "Elixir of Concealment",
        "An elixir that grants invisibility for 1 hour.",
        100
    ),
    11: i.Item(
        "Boots of Swiftness",
        "Boots that increase the wearer's speed.",
        180
    ),
    12: i.Item(
        "Amulet of Protection",
        "An amulet that grants a bonus to defense.",
        220
    ),
    13: i.Item(
        "Potion of Strength",
        "A potion that temporarily increases strength.",
        90
    ),
    14: i.Item(
        "Lantern of Revealing",
        "A lantern that reveals hidden or invisible creatures and objects.",
        130
    ),
    15: i.Item(
        "Gloves of Dexterity",
        "Gloves that enhance the wearer's dexterity.",
        160
    ),
}

# Magical Items Table:
# This table contains various magical weapons that can be used as rare and powerful rewards for players in the game.
# Each item has a unique identifier (1-15) and includes a name, description, value, damage, damage type, poisoned, and enchant.
magical_items_table = {
    1: i.Melee_Item(
        "Blazing Edge",
        "A sword with a blade wreathed in fire. Deals extra fire damage.",
        1000,
        dice_Roll.roll_d6(),
        "Slashing",
        False,
        "Fire"
    ),
    2: i.Melee_Item(
        "Frostbite Blade",
        "A sword with a blade of ice. Deals extra cold damage.",
        1200,
        dice_Roll.roll_d6(),
        "Slashing",
        False,
        "Cold"
    ),
    3: i.Melee_Item(
        "Drakebane",
        "A sword specifically crafted to slay drakes. Deals extra damage against drakes.",
        1500,
        dice_Roll.roll_d8(),
        "Slashing",
        False,
        "+5 Damage to Drakes"
    ),
    4: i.Melee_Item(
        "Staff of Elements",
        "A staff that grants the wielder various magical abilities.",
        2000,
        dice_Roll.roll_d6(),
        "Bludgeoning",
        False,
        "Random Magical Abilities"
    ),
    5: i.Melee_Item(
        "Venomstrike Dagger",
        "A dagger coated in venom. Deals poison damage and can poison the target.",
        800,
        dice_Roll.roll_d4(),
        "Piercing",
        True,
        "Poisoned"
    ),
    6: i.Melee_Item(
        "Thunderclap Hammer",
        "A mighty hammer with lightning enchantments. Deals extra thunder damage.",
        1800,
        dice_Roll.roll_d8(),
        "Bludgeoning",
        False,
        "Thunder"
    ),
    7: i.Melee_Item(
        "Wishblade",
        "A sword that grants the wielder a limited number of wishes.",
        2500,
        dice_Roll.roll_d8(),
        "Slashing",
        False,
        "Grants 3 wishes"
    ),
    8: i.Melee_Item(
        "Radiant Avenger",
        "A sword imbued with holy magic. Deals extra radiant damage and grants protection against evil.",
        2200,
        dice_Roll.roll_d8(),
        "Slashing",
        False,
        "Radiant"
    ),
    9: i.Melee_Item(
        "Decapitating Blade",
        "A sword with the ability to decapitate foes on a critical hit.",
        3000,
        dice_Roll.roll_d10(),
        "Slashing",
        False,
        None
    ),
    10: i.Melee_Item(
        "Solaris Blade",
        "A sword that emits bright light and deals radiant damage.",
        2000,
        dice_Roll.roll_d8(),
        "Slashing",
        False,
        "Radiant"
    ),
    11: i.Melee_Item(
        "Shadowfang",
        "A dagger that grants stealth abilities and deals extra damage when attacking from shadows.",
        1600,
        dice_Roll.roll_d4(),
        "Piercing",
        False,
        "Shadow"
    ),
    12: i.Melee_Item(
        "Earthshaker Maul",
        "A massive maul that can create tremors upon striking the ground.",
        2100,
        dice_Roll.roll_d12(),
        "Bludgeoning",
        False,
        "Earthquake"
    ),
    13: i.Melee_Item(
        "Lifedrinker Sword",
        "A cursed sword that drains the life of enemies to heal the wielder.",
        2500,
        dice_Roll.roll_d8(),
        "Slashing",
        False,
        "Life Steal"
    ),
    14: i.Melee_Item(
        "Stormcaller Spear",
        "A spear that can summon storms and deal lightning damage.",
        1900,
        dice_Roll.roll_d6(),
        "Piercing",
        False,
        "Lightning"
    ),
    15: i.Melee_Item(
        "Soul Reaver",
        "A blade that can capture the souls of defeated enemies.",
        3000,
        dice_Roll.roll_d10(),
        "Slashing",
        False,
        "Soul Capture"
    ),
}
