# Dijjon Trade Class
# Developed & designed by: Zane M Deso
# Purpose: Used to handle any trade or bartering transaction.


from typing import Optional, Dict

class Trade:
    """
    Trade Class for handling item purchase and trading transactions.

    Attributes:
        transaction_id (int): Unique identifier for each trade transaction.
    """

    def __init__(self, transaction_id: int) -> None:
        """
        Initialize a new Trade instance.

        Args:
            transaction_id: The starting transaction ID.
        """
        self.transaction_id = transaction_id

    def tick_transaction_id(self) -> int:
        """
        Increment and return the next transaction ID.

        Returns:
            The updated transaction ID.
        """
        self.transaction_id += 1
        return self.transaction_id

    def has_gold(self, player, cost: int) -> bool:
        """
        Check if the player has enough gold for a purchase.

        Args:
            player: The player object with a `gold` attribute.
            cost: The cost in gold.

        Returns:
            True if player.gold >= cost, False otherwise.
        """
        return getattr(player, 'gold', 0) >= cost

    def select_item(self, player, item_list: Dict[str, object]) -> Optional[str]:
        """
        Display available items and prompt the player to select one.

        Args:
            player: The player object making the purchase.
            item_list: A dict mapping item keys to item objects with `.name` and `.val`.

        Returns:
            The selected item key, or None if the player cancels.
        """
        print(f"Your GP: {player.gold}")
        for idx, (key, item) in enumerate(item_list.items(), start=1):
            print(f"{idx}. {item.name} - {item.val} gp")

        while True:
            choice = input("Enter number to buy, or 'q' to cancel: ")
            if choice.lower() == 'q':
                return None
            if choice.isdigit():
                index = int(choice)
                if 1 <= index <= len(item_list):
                    return list(item_list.keys())[index - 1]
            print("Invalid input; please enter a valid number or 'q' to quit.")

    def execute_trade(self, player, item) -> bool:
        """
        Process the purchase: deduct gold and add item to inventory.

        Args:
            player: The player object with `gold` and `inventory` attributes.
            item: The item object with `.name` and `.val`.

        Returns:
            True if the purchase succeeded, False otherwise.
        """
        if not self.has_gold(player, item.val):
            print(f"Not enough gold to purchase {item.name}.")
            return False

        player.gold -= item.val
        # Add item to inventory (increment count)
        inventory = getattr(player, 'inventory', {})
        inventory[item.name] = inventory.get(item.name, 0) + 1
        player.inventory = inventory

        print(f"Purchased {item.name} for {item.val} gp.")
        return True

    def order(self, player, item_list: Dict[str, object]) -> None:
        """
        Main loop to handle trading: selection and execution.

        Args:
            player: The player object participating in the trade.
            item_list: A dict of available items to purchase.
        """
        key = self.select_item(player, item_list)
        if key is None:
            print("Trade cancelled.")
            return

        item = item_list[key]
        success = self.execute_trade(player, item)
        if not success:
            # Offer retry
            retry = input("Would you like to try again? (y/n): ")
            if retry.lower().startswith('y'):
                self.order(player, item_list)
            else:
                print("No purchase made.")
