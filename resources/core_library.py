# Dijjon Core Library File
# Developed & designed by: Zane M Deso
# Purpose: Used to store all in-game content. Implementation of a helper class to access each list/dict accordingly is required.
# Perhaps using Master to navigate the tables would be best.

import scripts.game_mechanics.Item as i
import scripts.game_mechanics.dice_Roll as dice_Roll


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
}

# List of available races (Original names replaced with unique alternatives)
races = [
    "Drakari",        # Replaces "Dragonborn"
    "Stonekin",       # Replaces "Dwarf"
    "Sylphari",       # Replaces "Elf"
    "Frostling",      # Replaces "Gnome"
    "Halfian",        # Replaces "Half-Elf"
    "Minfolk",        # Replaces "Halfling"
    "Orcane",         # Replaces "Half-Orc"
    "Humara",         # Replaces "Human"
    "Shadeborn",      # Replaces "Tiefling"
]

# List of available classes (Original names replaced with unique alternatives)
classes = [
    "Berserker",      # Replaces "Barbarian"
    "Minstrel",       # Replaces "Bard"
    "Diviner",        # Replaces "Cleric"
    "Naturebinder",   # Replaces "Druid"
    "Warrior",        # Replaces "Fighter"
    "Ascetic",        # Replaces "Monk"
    "Knight",         # Replaces "Paladin"
    "Pathfinder",     # Replaces "Ranger"
    "Shadow",         # Replaces "Rogue"
    "Mage",           # Replaces "Sorcerer"
    "Enchanter",      # Replaces "Warlock"
    "Spellbinder",    # Replaces "Wizard"
]

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
]

# Commoner jobs
jobs = [
    'Farmer', 'Blacksmith', 'Carpenter', 'Baker', 'Tailor', 'Fisherman',
    'Miner', 'Woodcutter', 'Merchant', 'Innkeeper', 'Barber', 'Miller',
    'Potter', 'Brewer', 'Butcher', 'Mason', 'Scribe', 'Tanner',
    'Herbalist', 'Messenger', 'Stablehand', 'Servant', 'Street Vendor',
    'Town Crier', 'Cartographer', 'Guard', 'Town Guard', 'Jeweler',
    'Weaver', 'Bard', 'Sailor',
]

# Monster types
monster_type_list = [
    "aberration", "beast", "celestial", "construct", "dragon",
    "elemental", "fey", "giant", "humanoid", "monstrosity",
]

# Monsters with types as values (Original names replaced with unique alternatives)
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
    "Yuan-ti": "humanoid",
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
    'circle_of_enchanters': {  # Renamed from 'circle_of_mages'
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
    }
}

# Reward Items Table:
# This table contains various items that can be used as rewards for players in the game.
# Each item has a unique identifier (1-10) and includes a name, description, and value.
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
}

# Magical Items Table:
# This table contains various magical weapons that can be used as rare and powerful rewards for players in the game.
# Each item has a unique identifier (1-10) and includes a name, description, value, damage, damage type, poisoned, and enchant.
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
}
