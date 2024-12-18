# Dijjon Alpha

This is the official documentation for Dijjon Alpha, a text-based game set
in the Fantasy RPG world of Dijjon.

## Author: Zane M Deso

### Last Updated: 12/18/2024

## Table of Contents

    Introduction
    Current Sprint Goal
    Backlog
    Bugs to Fix
    Roadmap
    Major Change Log
    Story Arch Plans

## Introduction

Dijjon Alpha is a text-based fantasy RPG that combines RNG mechanics with dynamic storytelling. No two playthroughs are alike, offering unique encounters and outcomes with each session. The game incorporates Agile development practices, structured around focused mini-sprints for iterative progress.

# Why I’m Making This Game

Dijjon is more than just a game to me; it’s a deeply personal project that combines my love for storytelling, my fascination with systems, and my desire to create something meaningful. Growing up, video games were my escape, a source of wonder and connection to stories that stayed with me long after the credits rolled. They offered moments of joy, introspection, and even a sense of purpose during times when life felt overwhelming.

This game is my way of channeling that inspiration into something new. It’s a chance to create a world where players can lose themselves in a story that resonates emotionally and challenges them to think about choices, consequences, and the complexity of relationships. I want Dijjon to be a space where creativity meets mechanics, where every interaction feels alive, and every decision matters.

At its core, this project is about expression—about finding a way to share my love for games and storytelling while building something I can be proud of. It’s a personal journey, one fueled by a passion for crafting experiences that might inspire others the way games once inspired me.

Current Sprint Goal

    Primary Goals:

        Complete a reflective "Year in Review" of the game’s development progress.
        Refactor import statements to avoid circular imports:
        All imports now delegated to main.py or middle-man modules to ensure clarity and consistency.
        Refactor complete; see Change Log.

    Key Development Tasks:

        Integrate skill checks, combat systems, and player mechanics into the Quest class.
        Fully implement the Enchanted Forest hardcoded quest, adding functional puzzle elements.
        Connect the text renderer (pygame GUI) with the quest system to shift gameplay from terminal to an interactive game window.
        Introduce basic audio-visual elements for immersion:
            Background images.
            Ambient sound effects.
            Simple music loops.
    

## Previous Sprint Goal

    Create a start menu with some playable functionality.
    Plug in some of the hard-coded quests into the main game.
    Work on story points if time permits.

    Implement continue function. (Idea here is to have beginning -> middle ->
    end of the quest, although some quests do not warrant having to finish
    objectives. This one the palyer could just mosey on by)

## Backlog

### High Priority

    [H] Make functional intro quest line
    [H] Inject encounters into hardcoded quests to add dynamic feel to
        'traveling', 'exploring', or 'continuing'
    [H] Refactor Player class to be a child of an Entity class; set NPCs
        and Mobs as children of the Entity class.
    [H] Finish Implementation of Combat Class.
    [H] Finish Implementation of First Bandit Quest Prototype.
    [H] Refactor code into dedicated files for better readability and
        maintainability. (Look into master.py, a lot of the functions
        can be organized into char_class.py or race.py.)
    [H] Text render (Renders fonts to screen)
    [H] Game loop with input handling (Allow dynamic inputs)
    [H] State tracking (Changes what is available per state)

### Medium Priority

    [M] Integrate Quest Journal with Quests.
    [M] Improve UI functionality for the quest journal.
    [M] Enhance menu functions for better user experience.
    [M] Build compositional relationships within the Player class.
    [M] Implement character classes and abilities with a
        CharacterClassFactory.

### Low Priority

    [L] Incorporate Party Level + Size to Solo Monster Hash Lookup Table
        for balanced solo monster encounters.
    [L] Track map expansion using nodes.
    [L] Add functionality for quest generation.
    [L] Create mad-lib type phrases for commoner jobs.
    [L] Improve Player Inventory UI.
    [L] Add optional check types based on location or event type.
    [L] Enhance roll_stats function in dice_Roll file.
    [L] Add accessors and mutators to each class.
    [L] Implement enchants to Melee_Items class.

## Bugs to Fix

    [M] Fix the give_item function to properly update or remove items in
        the player's inventory.

## Roadmap

### Core Game Mechanics

    Combat System: Refine combat mechanics and integrate AI strategies
    for NPCs.
    Quest System: Expand the quest system to include more complex and
    branching quests.
    Race: Create dedicated race.py file that will handle race
          functions and features.

### Character Development

    Character Classes: Enhance character class system with unique
    abilities and progression paths. Creating unique classes!
    Entities and NPCs: Develop detailed attributes and behaviors
    for entities. Using AI->queue commands!

### Item and Inventory Management

    Items: Add item durability and special effects.
    Trading System: Implement a trading system for interactions
    with NPC vendors and players.

### World Building

    Environment: Define more environments and locations for
    exploration.
    Mob Generation: Dynamically create challenges for players.

### User Interface and Experience

    GUI: Use a simple pyGame gui to display text, images and
         stats much more gracefully.
    Settings and Customization: Update the settings module for
    more customization options.
    Configuration: Implement a config file for key mapping, input-
                    type, screen resolution, etc.
    Feedback System: Implement a system to collect player feedback.

### Technical Improvements

    Code Refactoring: Regularly review and refactor the codebase.
    Testing and Debugging: Increase focus on testing all modules.

### Documentation and Help System

    Game Documentation: Create comprehensive documentation for
    players.
    Developer Documentation: Maintain clear developer documentation.

## Major Change Log

<ul>
    <li>Refactored codebase to align with better practices
    for directory design flow. See refactor below. (11/2/2024)
    main is functional after merging with Master.
    <li>Created base level unit tests, plans to expand and
    automate (9/15/2024)
    <li>Implemented Quest Class to dynamically handle creating and 
    playing quests. (9/1/2024)
    <li>Major refactor on codebase: No need to clutter one folder with
    all of the scripts so everything is now in dedicated folders.
    (8/12/2024)
    <li>Integrated DijjonAlphaDevelopment folder with Git: Enhanced
    tracking of progress.
    <li>Refactoring player and NPC creation: Expanded classes and races,
    refactored to core library (1/6/2024).
    <li>Race and class selection enumeration: Improved user input
    handling (Done).
    <li>Changed attribute name convention for "int" in Player class:
    <li>Resolved conflicts with int() function (Done).
    <li>Integrated repository with GitHub: Improved version control
    and collaboration.
</ul>

### Refactor (11/2/2024)

Code base made to align more so with the following codebase directory struct

    Dijjon/
    ├── assets/
    │   ├── audio/                # For storing any sound/music files
    │   ├── fonts/                # For font resources
    │   ├── images/               # Restructured image assets here
    │   │   ├── characters/
    │   │   ├── enemies/
    │   │   ├── environment/
    │   │   └── ui/
    │   └── levels/
    │       └── tilesets/
    ├── docs/
    ├── src/
    │   ├── core/
    │   │   ├── config.py         # New, consolidated config file
    │   │   ├── constants.py      # Constants and universal settings
    │   │   ├── main.py           # Renamed main game loop
    │   │   └── settings.py
    │   ├── entities/
    │   │   ├── player.py         # From `scripts/entity/Player.py`
    │   │   ├── enemy.py          # From `scripts/entity/Mob.py`
    │   │   ├── npc.py
    │   │   └── effects/          # Special effects like lycan, vampire
    │   ├── systems/
    │   │   ├── ai/
    │   │   ├── audio/
    │   │   ├── events/
    │   │   ├── graphics/
    │   │   ├── input/
    │   │   ├── physics/
    │   │   ├── rendering.py
    │   │   └── ui.py
    │   └── world/
    │       ├── dungeon/
    │       └── environment.py
    ├── tests/
    ├── tools/
    └── README.md

## Testing

We have implemented unit tests to ensure the game's functionality and reliability. This section provides instructions on how to run the tests.
Running Tests

To run the tests, follow these steps:
<ul>
<li>Navigate to the Project Root Directory
<li>Open your terminal or command prompt and navigate to the root directory of the project:
<li>bash
</ul>

```cd path/to/DijjonAlphaDevelopment```

Replace path/to/DijjonAlphaDevelopment with the actual path to your project directory.

Run Tests Using Unittest

Use the following command to discover and run all tests:

<i>using bash</i>

```python -m unittest discover -s scripts/tests -p 'test_*.py'```

Explanation of the command:

    python -m unittest: Runs Python's built-in unittest module as a script.
    discover: Tells unittest to discover tests automatically.
    -s scripts/tests: Specifies the start directory for test discovery.
    -p 'test_*.py': Sets the pattern to match test files (e.g., test_main.py).

Interact with Tests (If Prompted)

Some tests may require user interaction, such as inputting actions during combat simulations. When running such tests, you might see prompts like:

    Hero, choose an action (attack, defend, etc.):

    Enter the requested input to proceed with the tests.

Notes

    Ensure Dependencies Are Installed:
        Make sure you have all necessary dependencies installed, and that your Python environment is correctly set up.
        If you are using a virtual environment, activate it before running the tests.

    Python Version:
        The project is developed using Python 3. Ensure that you are using a compatible Python interpreter.

Future Improvements

We aim to enhance our testing suite by automating user interactions to make the tests fully automated. This will improve efficiency and allow integration with continuous integration pipelines.

## Story Arch Plans

### Branching Choices

    Key Decision Points:
        Decisions during pivotal scenes such as The Incident at Hollowreach Citadel (Act One) directly influence trust dynamics, alliances, and reputation.
        Player choices in moments of chaos (e.g., saving lives, pursuing evidence, or aligning loyalties) determine early allegiances with Zyrian or Drajhan factions.
        Choices during interactions with major NPCs (e.g., Prince Veylen Drevaris, Myrra, Kelgar) affect their trust and potential outcomes in later acts.
    Consequences and Repercussions:
        Immediate: Choices in Act One will impact early trust dynamics and NPC behavior.
        Long-Term: State allegiances and rivalries evolve, potentially altering the game's ending and global narrative.

### Random Elements

    Dynamic Encounters:

    Replace Enchanted Forest static elements with more modular, scene-based encounters from the Hollowreach Citadel Incident, refugee exodus, and The Sunken Hold quest.
    Implement random NPC behaviors during chaos scenes. For instance:
        Refugees may betray the player for resources.
        Soldiers may desert or remain loyal based on player choices.

    Luck-Based Outcomes:

        Introduce RNG-based skill checks during pivotal scenes, e.g., defusing a dangerous situation or evading pursuit by Black Vanguard forces.
        Ensure randomness impacts scene flow without negating player agency.

### Character Development and Relationships

    Dynamic NPC Relationships:

    Replace generic relationships from Enchanted Forest with detailed arcs based on decisions tied to main characters like Myrra, Kelgar, and Ashki.
    Introduce shifting alliances with major NPC factions:
        Black Vanguard Extremists (Drajh).
        Azure Order Radicals (Zyra).
    Develop a dynamic relationship with Prince Veylen Drevaris, reflecting player alignment, diplomacy, or enmity.

    Player Reputation:

        Expand on state-wide perception mechanics:
            Zyra and Drajh citizens, soldiers, and leadership will react differently based on actions taken during and after The First Fragment.

### Time-Sensitive Quests

    Act One ("The First Fragment") has limited time to investigate the Hollowreach explosion.
    Act Two introduces time-sensitive survival scenarios, such as securing resources for refugees before supplies run out.
    Act Three involves critical deadlines tied to the relic’s activation at the Citadel of Eternity.

### Tracking Past Choices

    State Tracking:

    Log all key choices during story events, such as:
        The player’s response to chaos at Hollowreach Citadel.
        Actions taken during the refugee exodus and confrontations with the Archdemon.
    Use logs to dynamically alter future NPC behavior and dialogue.

    Dialogue Changes:

        Refine dialogues for major NPCs to reflect decisions tied to their trust and reputation mechanics.
        Example: General Vyrne's reaction to the player saving her life versus pursuing clues in Act One.

### Multiple Endings

    Reconciliation Ending 
    Domination Ending
    Destruction Ending 
    Unstable Peace Ending

### Feedback and Adaptation

    Environmental Changes:

    Tie world-building elements directly to key events:
        Example: Demon-corrupted zones expand as time progresses in Act Two unless the player takes proactive measures.

    Faction Adaptation:

        Major factions dynamically respond to player choices:
            The Black Vanguard may grow stronger if the player neglects counteracting their propaganda.
            The Azure Order might turn on the player if perceived as a threat to Zyrian sovereignty.
