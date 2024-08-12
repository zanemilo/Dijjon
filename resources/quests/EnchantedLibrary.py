# Dijjon ForgottenTombs
# Developed & designed by: Zane M Deso
# Purpose: Placeholder Quest/Event/Location Idea

import random


class EnchantedLibrary:
    def __init__(self):
        self.books = ["Book of Shadows", "Tome of Time", "Lost Spells", "Ancient Diaries"]
        self.secret_found = False
        self.puzzle_solved = False
        self.master_key = False

    def enter_library(self):
        print("You've entered the ancient library. Dust fills the air, and the sound of silence overwhelms.")
        self.explore()

    def explore(self):
        print("You see several old books on a large wooden table in the center.")
        action = input("Would you like to 'read' a book, 'search' the room, or 'leave'? ")
        if action.lower() == 'read':
            self.read_book()
        elif action.lower() == 'search':
            self.search_room()
        elif action.lower() == 'leave':
            print("You leave the library, maybe to return another day.")
        else:
            print("Not a valid action. Please choose again.")
            self.explore()

    def read_book(self):
        book = random.choice(self.books)
        print(f"You start reading {book}.")
        if "Lost Spells" in book and not self.puzzle_solved:
            self.solve_puzzle()
        elif "Book of Shadows" in book:
            self.find_secret()
        else:
            print("It's fascinating but not particularly helpful right now.")
        self.explore()

    def find_secret(self):
        if not self.secret_found:
            print("As you flip through the Book of Shadows, a loose page falls out revealing a hidden map!")
            self.secret_found = True
        else:
            print("You've already discovered the hidden map.")
        self.explore()

    def solve_puzzle(self):
        print("The Lost Spells contain a ciphered message.")
        puzzle = input("Enter the correct phrase to decipher the message: ")
        if puzzle.lower() == "memento mori":
            print("The spell unlocks a hidden drawer, revealing a master key!")
            self.puzzle_solved = True
            self.master_key = True
        else:
            print("Nothing happens. It seems that wasn't the right phrase.")
        self.explore()

    def search_room(self):
        if self.master_key:
            print("Using the master key, you unlock a hidden door behind a bookshelf.")
        else:
            print("You find some interesting, albeit mundane, artifacts.")
        self.explore()

# Create an instance and start the game
library_game = EnchantedLibrary()
library_game.enter_library()
