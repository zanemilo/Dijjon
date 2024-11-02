# Dijjon Trade Class
# Developed & designed by: Zane M Deso
# Purpose: Used to handle any trade or bartering transaction.

import systems.core_library as cl 
import scripts.game_mechanics.Item as it 


class Trade:
    """
    Trade Class for handling shopping for items and trading items within the game.

    Attributes:
        transaction_id (int): Unique identifier for each trade transaction.
    """

    def __init__(self, transaction_id):
        """
        Initializes a new Trade instance with a given transaction ID.

        Args:
            transaction_id (int): The initial transaction ID.
        """
        self.transaction_id = transaction_id

    def tick_transaction_id(self):
        """
        Increments the transaction ID by one to ensure uniqueness.

        Returns:
            int: The updated transaction ID.
        """
        self.transaction_id += 1
        return self.transaction_id

    def has_gold_check(self, player, item_cost=0):
        """
        Checks if the player has sufficient gold to pay for an item, service, or interaction.

        Args:
            player (Player): The player object containing gold attribute.
            item_cost (int, optional): The cost of the item or service. Defaults to 0.

        Returns:
            bool: True if player has enough gold, False otherwise.
        """
        if player.gold >= item_cost:
            return True
        else:
            return False
        
    def order(self, player, item_list):
        """
        Handles the ordering process where a player can purchase items from a given item list.

        Args:
            player (Player): The player object making the purchase.
            item_list (dict): A dictionary of available items to purchase, with item names as keys and item objects as values.
        """
        global last_var  # Declaring 'last_var' as a global variable (ensure it's defined elsewhere)

        # Display the player's current gold
        print(f"Buy:\n\nYour GP: {player.gold}")

        # Enumerate through the available items and display them to the player
        for i, (name, item) in enumerate(item_list.items()):
            print(f"{i+1}. {item.name} - {item.val} gp")

        # Prompt the player to make a purchase choice
        choice = input("What would you like to purchase?\n")
        
        # Loop to validate the player's choice
        while not choice.isdigit() or int(choice) not in range(1, len(item_list)+1):
            # Prompt the player for a valid choice or to leave
            invalid_choice = input(f"Invalid choice. Please select a valid option. \nWould you like to leave?\nInput the number of your choice\n\n1. Yes\n2. No")
    
            if int(invalid_choice()) == 1:
                # If player chooses to leave, perform the necessary action (variable 'last_var' usage unclear)
                last_var
    
            elif int(invalid_choice()) == 2:
                # If player chooses not to leave, restart the ordering process
                self.order(item_list)
    
            else:
                # Handle any other invalid input by notifying the player and restarting the order
                print(f"\nInvalid input. Returning to last screen and returning input as error to logs.\n")
                self.order(item_list)
    
            # Restart the ordering process
            self.order(item_list)
    
        # Retrieve the chosen item based on player's input
        chosen_item = list(item_list.values())[int(choice)-1]
    
        # Check if the player has enough gold to purchase the chosen item
        if self.has_gold_check(player, chosen_item.val) == True:
            # Deduct the item's cost from the player's gold
            player.gold -= chosen_item.val
    
            # Notify the player of the successful purchase
            print(f"You have purchased {chosen_item.name} for {chosen_item.val} gold.")
    
            # Create a temporary dictionary to hold the purchased item
            temp_dict1 = {chosen_item.name : chosen_item.val}
    
            # Update the player's inventory with the purchased item
            player.inventory.update(temp_dict1)  # This may overwrite existing items with the same name
    
            # Uncomment and fix the following line if necessary
            # playerOne.inventory.update(name=f'{chosen_item.name}')  # FIX ME: not working as intended, might need to simplify or refactor this code
    
            # Remove the purchased item from the temporary dictionary
            temp_dict1.pop(chosen_item.name)  # Deletes temp_dict1 key and value
    
            # Debug print statements (commented out)
            # print(temp_dict1, "\n")
    
            # Display the updated player inventory
            print(player.inventory, "\n")
    
        else:
            # Inform the player that they do not have enough gold
            print(f"You do not have enough gp to purchase {chosen_item.name}")
            
            # Restart the ordering process
            self.order(item_list)
