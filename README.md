# Dijjon Alpha

This is the official documentation for Dijjon Alpha, a text-based game set
in the Fantasy RPG world of Dijjon.

## Author: Zane M Deso

### Last Updated: 12/16/2024

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

Current Sprint Goal

    Complete a simple and self honorary Year in review for the development of
    the game so far.

    Primary concern is to fix import statements
    and refactor to avoid circular imports.
    As a rule of thumb,
    Leave imports to main to delegate or a middle man class.

    UPDATE: Refactor complete see change log.
    AWT updated import statements and consolidation of 
    class concerns to avoid ciruclar import.

    In Quest Class, integrate skill checks, combat, and the player
    Flesh out EnchantedForest HardCoded Quest.
    Make functional puzzle aspect.

    Integrate text renderer (GUI via pygame) with Quest system
    allowing player to make options and read outcomes in a 
    game window instead of in terminal.

    Add VERY basic visual/sound elements (Background imgs, ambience, SFX, simple music)
    

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

    Key Decision Points: Define moral, strategic, and
    information-based decisions.
    Consequences and Repercussions: Implement immediate, delayed,
    and subtle changes.

### Random Elements

    Random Encounters: Introduce variability in challenges and
    opportunities.
    Luck-Based Elements: Incorporate dice rolls for certain outcomes.

### Character Development and Relationships

    Emotional Ties: Affect NPC relationships based on player decisions.
    Reputation: Influence NPC interactions based on player's reputation.

### Time-Sensitive Quests

    Seasonal and Time-Based Events: Include quests available during
    specific in-game times.
    Missable Quests: Opportunities that disappear if not acted upon.

### Tracking Past Choices

    State Tracking: Log decisions and their outcomes.
    Dialogue Changes: Alter NPC dialogues based on player history.

### Multiple Endings

    Cumulative Decisions: Plan multiple endings based on player choices.

### Feedback and Adaptation

    Environmental Changes: Reflect player actions in the game world.
    NPC Adaptations: Change NPC strategies based on player reputation.
