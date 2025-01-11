# Dijjon Core Library File
# Developed & designed by: Zane M Deso
# Purpose: Used to store all in-game content. Implementation of a helper class to access each list/dict accordingly is required.
# Perhaps using Master to navigate the tables would be best.

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

# Nested dict containing master list of locations
# Towns, caves, bandit camps, and roadside locations
locations = { 
    # Town locations
    'towns': [
        {
            "name": "Smallville",
            "size": "small",
            "inn": "The Cozy Hearth",
            "general_store": "Peddler's Corner",
        },
        {
            "name": "Midtown",
            "size": "medium",
            "inn": "The Golden Griffin",
            "general_store": "Market Bazaar",
        },
        {
            "name": "Grand City",
            "size": "large",
            "inn": "The Royal Retreat",
            "general_store": "Emporium of Wonders",
        },
        {
            "name": "Riverside",
            "size": "small",
            "inn": "The Rusty Anchor",
            "general_store": "River's Edge Trading Post",
        },
        {
            "name": "Misty Hollow",
            "size": "medium",
            "inn": "The Whispering Willow",
            "general_store": "Mystic Emporium",
        },
        {
            "name": "Sunvale",
            "size": "small",
            "inn": "The Rising Sun Inn",
            "general_store": "Sunvale Supplies",
        },
        {
            "name": "Shadowport",
            "size": "large",
            "inn": "The Moonlit Maiden",
            "general_store": "Shadowport Market",
        },
        {
            "name": "Eagle's Peak",
            "size": "medium",
            "inn": "The Soaring Eagle",
            "general_store": "Peak Provisions",
        },
        {
            "name": "Verdant Grove",
            "size": "small",
            "inn": "The Green Leaf",
            "general_store": "Grove Goods",
        },
        {
            "name": "Ironforge",
            "size": "large",
            "inn": "The Hammered Anvil",
            "general_store": "Forge Finds",
        },
    ],
    # Cave locations
    'caves': [
        {
            "name": "Shadowfang Cavern",
            "size": "small",
        },
        {
            "name": "Crystal Depths",
            "size": "large",
        },
        {
            "name": "Whispering Grotto",
            "size": "medium",
        },
        {
            "name": "Mossy Hollows",
            "size": "small",
        },
        {
            "name": "Echoing Abyss",
            "size": "large",
        },
        {
            "name": "Dragon's Maw",
            "size": "large",
        },
        {
            "name": "Serpent's Tunnels",
            "size": "medium",
        },
        {
            "name": "Forgotten Mine",
            "size": "small",
        },
        {
            "name": "Ancient Catacombs",
            "size": "large",
        },
        {
            "name": "Glittering Caverns",
            "size": "medium",
        },
    ],
    # Bandit camp locations
    'bandit camps': [
        {
            "name": "Raven's Roost",
            "size": "small",
        },
        {
            "name": "Serpent's Hideout",
            "size": "large",
        },
        {
            "name": "Blackthorn Encampment",
            "size": "medium",
        },
        {
            "name": "Viper's Den",
            "size": "small",
        },
        {
            "name": "Daggerfall Outpost",
            "size": "large",
        },
        {
            "name": "Crimson Camp",
            "size": "medium",
        },
        {
            "name": "Shadow Hideaway",
            "size": "small",
        },
        {
            "name": "Ironclaw Base",
            "size": "large",
        },
        {
            "name": "Silent Knoll",
            "size": "medium",
        },
        {
            "name": "Broken Blade Camp",
            "size": "small",
        },
    ],
    # Roadside locations
    'roadside locations': [
        {
            "name": "Crossroads Rest",
            "size": "small",
        },
        {
            "name": "Wagon Wheel Waystation",
            "size": "small",
        },
        {
            "name": "Traveller's Haven",
            "size": "small",
        },
        {
            "name": "Hillside Retreat",
            "size": "small",
        },
        {
            "name": "Wayfarer's Rest",
            "size": "small",
        },
        {
            "name": "Lone Pine Inn",
            "size": "small",
        },
        {
            "name": "Misty Meadows",
            "size": "small",
        },
        {
            "name": "Sunset Oasis",
            "size": "small",
        },
        {
            "name": "Twin Oaks Tavern",
            "size": "small",
        },
        {
            "name": "Roaming Rendezvous",
            "size": "small",
        },
        {
            "name": "Silent Springs",
            "size": "small",
        },
        {
            "name": "Starlight Rest Stop",
            "size": "small",
        },
        {
            "name": "Hidden Hollow",
            "size": "small",
        },
        {
            "name": "Golden Fields Inn",
            "size": "small",
        },
        {
            "name": "Riverside Retreat",
            "size": "small",
        },
        {
            "name": "Forest's Edge",
            "size": "small",
        },
        {
            "name": "Desert Rose Inn",
            "size": "small",
        },
        {
            "name": "Mountain Pass Lodge",
            "size": "small",
        },
        {
            "name": "The Old Mill",
            "size": "small",
        },
        {
            "name": "Windy Plains Outpost",
            "size": "small",
        },
    ],
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
