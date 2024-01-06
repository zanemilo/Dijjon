import core_library as cl


class Trade:
    """Trade Class for shopping for items, trading items"""

    def __init__(self, name):
        self.name = name

    def has_gold_check(self, player, item_cost):
        """function called to check if the player has sufficient gold to pay for an item/service/interaction"""
        item_cost = 0
        if player.gold >= item_cost:
            item_cost = 0
            return True
        else:
            item_cost = 0
            return False
        
    # starts order(think salesperson) function using an item list as an arguement
    def order(self, player, item_list):
        global last_var

        print(f"Buy:\n\nYour GP: {player.gold}")

        for i, (name, item) in enumerate(item_list.items()):
            print(f"{i+1}. {item.name} - {item.val} gp")

        choice = input("What would you like to purchase?\n")
        
        # while loop checks if input is digit or integer that is in the range of enumerated item_list options
        while not choice.isdigit() or int(choice) not in range(1, len(item_list)+1):

            invalid_choice = input(f"Invalid choice. Please select a valid option. \nWould you like to leave?\nInput the number of your choice\n\n1. Yes\n2. No")

            if int(invalid_choice()) == 1:
                last_var()

            elif int(invalid_choice()) == 2:
                self.order(item_list)

            else:
                print(f"\nInvalid input. Returning to last screen and returning input as error to logs.\n")
                self.order(item_list)

            self.order(item_list)

        chosen_item = list(item_list.values())[int(choice)-1]

        if self.has_gold_check(player, chosen_item.val) == True:

            player.gold -= chosen_item.val

            print(f"You have purchased {chosen_item.name} for {chosen_item.val} gold.")

            temp_dict1 = {chosen_item.name : chosen_item.val}

            player.inventory.update(temp_dict1) # this would overwrite the value

            #playerOne.inventory.update(name=f'{chosen_item.name}')# FIX ME: not working as intended, might need to simplify or refactor this code

            temp_dict1.pop(chosen_item.name) # deletes temp_dict1 key and value

            #print(temp_dict1, "\n")

            print(player.inventory, "\n")

        else:
            print(f"You do not have enough gp to purchase {chosen_item.name}")
            
            self.order(item_list)