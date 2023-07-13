

# random names
name_list = ["Aarav",
    "Ada",
    "Aelius",
    "Aiko",
    "Aisling",
    "Akari",
    "Amara",
    "Ananda",
    "Anders",
    "Anika",
    "Aruna",
    "Aya",
    "Bastian",
    "Camila",
    "Cassia",
    "Ciaran",
    "Dalia",
    "Darian",
    "Eamon",
    "Eira",
    "Eirik",
    "Eliana",
    "Enara",
    "Esme",
    "Finnian",
    "Freya",
    "Giselle",
    "Hakan",
    "Hiroshi",
    "Idris",
    "Iliana",
    "Inara",
    "Isolde",
    "Jasmin",
    "Kai",
    "Kaia",
    "Kamila",
    "Kiran",
    "Lakshmi",
    "Leif",
    "Lilja",
    "Lucien",
    "Maeve",
    "Malik",
    "Maya",
    "Milan",
    "Mira",
    "Nadia",
    "Nikola",
    "Nina",
    "Orion",
    "Paloma",
    "Ravi",
    "Rhea",
    "Rohan",
    "Rosalind",
    "Sana",
    "Sasha",
    "Soren",
    "Suri",
    "Tara",
    "Tavian",
    "Thalia",
    "Uma",
    "Veda",
    "Vikram",
    "Xander",
    "Yara",
    "Yusuf",
    "Zara",
    "Zia",
    "Alessio",
    "Amaya",
    "Ananya",
    "Anouk",
    "Ari",
    "Asher",
    "Astrid",
    "Avi",
    "Azalea",
    "Bijan",
    "Bodhi",
    "Cassian",
    "Chiara",
    "Daliah",
    "Darius",
    "Elara",
    "Elina",
    "Emil",
    "Emira",
    "Eva",
    "Felix",
    "Flora",
    "Gia",
    "Gwyn",
    "Hiro",
    "Iris",
    "Isra",
    "Jaya",
    "Juno",
    "Kaden",
    "Kaya",
    "Keira",
    "Khalil",
    "Lana",
    "Lev",
    "Lilith",
    "Linnea",
    "Lucia",
    "Lyra",
    "Marin",
    "Milo",
    "Nadia",
    "Niamh",
    "Nyla",
    "Orin",
    "Pasha",
    "Rafael",
    "Raya",
    "Ren",
    "Rhian",
    "Sage",
    "Selene",
    "Seren",
    "Sylvan",
    "Talia",
    "Tavi",
    "Vera",
    "Wren",
    "Zayn",]

# commoner jobs
jobs = [
    'Farmer',
    'Blacksmith',
    'Carpenter',
    'Baker',
    'Tailor',
    'Fisherman',
    'Miner',
    'Woodcutter',
    'Merchant',
    'Innkeeper',
    'Barber',
    'Miller',
    'Potter',
    'Brewer',
    'Butcher',
    'Mason',
    'Scribe',
    'Tanner',
    'Herbalist',
    'Messenger',
    'Stablehand',
    'Servant',
    'Street Vendor',
    'Town Crier',
    'Cartographer',
    'Guard',
    'Town Guard',
    'Jeweler',
    'Weaver',
    'Bard',
    'Sailor',
]

# monster types
monster_type_list = [
    "aberration",
    "beast",
    "celestial",
    "construct",
    "dragon",
    "elemental",
    "fey",
    "giant",
    "humanoid",
    "monstrosity",
]

# monsters with types as values
monster_dict = {
    # Aberrations
    "Cthulhu": "aberration",
    "Illithid": "aberration",
    "Beholder": "aberration",
    "Nothic": "aberration",
    "Gibbering Mouther": "aberration",
    "Aboleth": "aberration",
    "Mind Flayer": "aberration",
    "Slaad": "aberration",
    "Deep Scion": "aberration",
    "Flumph": "aberration",
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
    "Solar": "celestial",
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

# nested dict containing master list of locations
# towns, caves, bandit camps, and roadside locations
locations = { 
    # town locations
    'towns' : [
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
    # cave locations
    'caves' : [
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
    # bandit camp locations
    'bandit camps' : [
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
    # roadside locations
    'roadside locations' : [
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

# factions dictionary this way a player, npc or location can adapt beliefs, join or represent the factions
# they will also have varying levels of hostility, or helpfulness to certain factions whom are rivals or allies
factions = {
    'order_of_the_silver_shield': {
        'name': 'Order of the Silver Shield',
        'alignment': 'Lawful Good',
        'description': 'The Order of the Silver Shield is a noble and chivalrous faction dedicated to protecting the innocent, upholding justice, and eradicating evil.',
        'allied_factions': ['circle_of_mages', 'guild_of_artisans'],
        'rival_factions': ['cult_of_the_shadow', 'brigands_of_the_crimson_eye'],
        'neutral_factions': [],
    },
    'circle_of_mages': {
        'name': 'Circle of Mages',
        'alignment': 'Neutral',
        'description': 'The Circle of Mages is a secretive faction of spellcasters who seek knowledge and the understanding of magical forces. They maintain balance and neutrality in their pursuits.',
        'allied_factions': ['order_of_the_silver_shield'],
        'rival_factions': ['cult_of_the_shadow', 'cabal_of_the_arcane_eye'],
        'neutral_factions': [],
    },
    'cult_of_the_shadow': {
        'name': 'Cult of the Shadow',
        'alignment': 'Chaotic Evil',
        'description': 'The Cult of the Shadow is a dark and sinister faction that worships forbidden powers and seeks to spread chaos and corruption throughout the land.',
        'allied_factions': ['brigands_of_the_crimson_eye'],
        'rival_factions': ['order_of_the_silver_shield', 'circle_of_mages'],
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
        'neutral_factions': ['circle_of_mages'],
    },
    'cabal_of_the_arcane_eye': {
        'name': 'Cabal of the Arcane Eye',
        'alignment': 'Neutral Evil',
        'description': 'The Cabal of the Arcane Eye is a secretive faction of power-hungry sorcerers and warlocks. They manipulate arcane forces for their own gain and seek to control the world.',
        'allied_factions': ['circle_of_mages'],
        'rival_factions': ['guild_of_artisans'],
        'neutral_factions': [],
    }
}

