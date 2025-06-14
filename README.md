# Dijjon Alpha

This is the official documentation for Dijjon Alpha, a text-based game set
in the Fantasy RPG world of Dijjon.

## Author: Zane Milo Deso

### Last Updated: 6/14/2025

## Table of Contents
- [Introduction](#introduction)
- [Why I’m Making This Game](#why-im-making-this-game)
- [Key Features](#key-features)
- [Roadmap](#roadmap)
- [Major Change Log](#major-change-log)

## Introduction

Dijjon Alpha is a text-based fantasy RPG that combines RNG mechanics with dynamic storytelling. No two playthroughs are alike, offering unique encounters and outcomes with each session. The game incorporates Agile development practices, structured around focused mini-sprints for iterative progress.

# Why I’m Making This Game

Dijjon is more than just a game to me; it’s a deeply personal project that combines my love for storytelling, my fascination with systems, and my desire to create something meaningful. Growing up, video games were my escape, a source of wonder and connection to stories that stayed with me long after the credits rolled. They offered moments of joy, introspection, and even a sense of purpose during times when life felt overwhelming.

This game is my way of channeling that inspiration into something new. It’s a chance to create a world where players can lose themselves in a story that resonates emotionally and challenges them to think about choices, consequences, and the complexity of relationships. I want Dijjon to be a space where creativity meets mechanics, where every interaction feels alive, and every decision matters.

At its core, this project is about expression—about finding a way to share my love for games and storytelling while building something I can be proud of. It’s a personal journey, one fueled by a passion for crafting experiences that might inspire others the way games once inspired me.

## Key Features

### Custom Engine Architecture
- **Modular Design:** The codebase is organized into dedicated modules (e.g., `Quest`, `QuestManager`, `DialogueManager`, `InteractionManager`) to separate concerns and enhance maintainability.
- **Agile & Iterative Development:** The project employs mini-sprints to continuously integrate new features, refactor code, and refine gameplay mechanics.
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
    
### Dynamic Quest & Narrative Mechanics
- **Branching Quest System:** The quest engine is planned to dynamically handle quest instances and branching storylines through a modular dispatcher system. Quests are defined as collections of narrative tasks, each with multiple possible outcomes based on player choices.
- **Robust Internal Logic:**  
  - **Task Execution:** Quests are broken down into steps that execute scripted actions based on user input.
  - **Skill Checks & Randomization:** Integrated logic for dice rolls and dynamic skill checks ensures that outcomes reflect both player decisions and RNG mechanics.
  - **Dialogue Management:** A dedicated dialogue system presents narrative text with clear formatting and timed output for a more immersive terminal experience.

### Planned Enhancements
- **Visual & GUI Upgrades:** While current development focuses on internal logic and text-based mechanics, future iterations will transition into rich visual experiences:
  - **Interactive GUI:** Plans to integrate a full Pygame-based GUI that will replace terminal interactions with dynamic windows, interactive menus, and visual storytelling.
  - **Audio-Visual Integration:** Future enhancements include background imagery, ambient sound effects, and music loops to further immerse the player in the world of Dijjon. Potentially, voice acted introduction and key dialogues.
- **Extended Gameplay Systems:** Additional features such as an enhanced combat system, AI-driven NPC behavior, and a more complex quest generation system are already planned.

## Technical Highlights

- **Custom Quest Engine:**  
  The `Quest` class, along with its manager modules, implements a dispatcher pattern to execute narrative tasks dynamically. This allows for highly flexible story progression that can adapt to player choices.
  
- **Interaction Management:**  
  The `InteractionManager` orchestrates skill checks and opposing roll logic, ensuring that all in-game challenges are resolved with clear, reproducible outcomes based on both player stats and random factors.
  
## Roadmap

### Core Game Mechanics

    Combat System: Refine combat mechanics and integrate AI strategies
    for NPCs.
    Quest System: Expand the quest system to include more complex and
    branching quests.
    Race: Create dedicated race.py file that will handle race
          functions and features.
    Exploration: Implement a more detailed exploration system with
    environmental interactions and dynamic events. This will allow
    players to interact with the world in meaningful ways, such as
    discovering hidden areas, solving puzzles, and encountering
    random events that can affect their journey. They will be able
    to explore the world of Dijjon in a more immersive way, with
    detailed environments and interactive elements, such as merchants,
    NPCs, and more.

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
    Mob & Event Generation: Dynamically create challenges for players.

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
    Testing and Debugging: Use unit tests to ensure code quality
    via assertions, mock objects, and test cases.

### Documentation and Help System

    Game Documentation: Create comprehensive documentation for
    players.
    Developer Documentation: Maintain clear developer documentation.

## Major Change Log

<ul>
    <li>Refactored import statements to avoid circular imports:
    All imports now delegated to main
    <li>Implemented a new `Quest` class to handle quest
    management and dynamic task execution. (6/14/2025)
    Minor narrative flow required to be fully functional.
    <li>Refactored codebase to align with better practices
    for directory design flow. (11/2/2024)
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

### Codebase Structure

Code base -- Certain folders to be implemented in the future if not active yet.

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

