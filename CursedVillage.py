# Dijjon ForgottenTombs
# Developed & designed by: Zane M Deso
# Purpose: Placeholder Quest/Event/Location Idea


class CursedVillage:
    def __init__(self):
        self.cure_found = False
        self.spirits_helped = 0
        self.villagers_saved = 0

    def explore_area(self):
        print("You enter the village, eerily silent with statuesque figures scattered around.")
        while not self.cure_found or self.spirits_helped < 3:
            choice = input("Would you like to 'talk' to a spirit, 'search' for ingredients, or 'leave'? ")
            if choice == 'talk':
                self.talk_to_spirit()
            elif choice == 'search':
                self.search_ingredients()
            elif choice == 'leave':
                break
            else:
                print("Invalid choice. Try again.")

    def talk_to_spirit(self):
        print("A faint voice reaches out to you, begging for help.")
        self.spirits_helped += 1
        if self.spirits_helped == 3:
            print("The spirits have shown you the location of the hidden grimoire.")
            self.search_grimoire()

    def search_ingredients(self):
        print("You found some herbal components that might be part of the cure.")
        if self.spirits_helped >= 3:
            self.cure_found = True
            print("You have everything you need to brew the cure!")

    def search_grimoire(self):
        print("You uncover an ancient book that outlines the reversal spell.")

village = CursedVillage()
village.explore_area()
