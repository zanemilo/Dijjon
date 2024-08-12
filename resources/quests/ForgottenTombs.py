# Dijjon ForgottenTombs
# Developed & designed by: Zane M Deso
# Purpose: Placeholder Quest/Event/Location Idea


class ForgottenTombs:
    def __init__(self):
        self.riddles_solved = 0
        self.traps_disarmed = 0
        self.treasure_found = False

    def enter_tombs(self):
        print("As you descend into the darkness, the air grows cold and heavy.")
        self.navigate_tombs()

    def navigate_tombs(self):
        while not self.treasure_found:
            action = input("Do you want to 'solve' a riddle, 'disarm' a trap, or 'search' for treasure? ")
            if action == 'solve':
                self.solve_riddle()
            elif action == 'disarm':
                self.disarm_trap()
            elif action == 'search':
                self.search_treasure()
            else:
                print("Not a valid action. Please choose again.")

    def solve_riddle(self):
        self.riddles_solved += 1
        print(f"You decipher the ancient script and solve the riddle. Total riddles solved: {self.riddles_solved}")

    def disarm_trap(self):
        self.traps_disarmed += 1
        print(f"You carefully disarm a dangerous trap. Total traps disarmed: {self.traps_disarmed}")

    def search_treasure(self):
        if self.riddles_solved >= 3 and self.traps_disarmed >= 2:
            print("You find the legendary treasure hidden deep within the tombs!")
            self.treasure_found = True
        else:
            print("You need to solve more riddles and disarm more traps to uncover the treasure.")

tombs = ForgottenTombs()
tombs.enter_tombs()
