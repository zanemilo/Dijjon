# Dijjon ForgottenTombs
# Developed & designed by: Zane M Deso
# Purpose: Placeholder Quest/Event/Location Idea


class EnchantedForest:
    def __init__(self):
        self.tasks_completed = 0
        self.path_found = False

    def walk_forest(self):
        print("You step into the vibrant, living forest, where the trees seem to whisper.")
        while not self.path_found:
            choice = input("Choose to 'help' a creature, 'solve' a forest puzzle, or 'continue' walking? ")
            if choice == 'help':
                self.help_creature()
            elif choice == 'solve':
                self.solve_puzzle()
            elif choice == 'continue':
                self.find_path()
            else:
                print("Invalid choice. Try again.")

    def help_creature(self):
        print("You help a stranded mythical beast, earning its gratitude.")
        self.tasks_completed += 1

    def solve_puzzle(self):
        print("You adjust the stones in a creek, altering the flow and revealing a new path.")
        self.tasks_completed += 1

    def find_path(self):
        if self.tasks_completed >= 3:
            print("The heart of the forest opens before you, revealing the ancient being.")
            self.path_found = True
        else:
            print("You need to engage more with the forest to find your way.")

forest = EnchantedForest()
forest.walk_forest()
