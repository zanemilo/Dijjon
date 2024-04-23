# Dijjon tree
# Developed & designed by: Zane M Deso
# Purpose: This will be the class for the linked lists that will allow for use in state management classes, previous events, current events, maybe even milestone progressions in the future.


class Node:
    """A Node in a singly linked list, contains data and a link to the next node."""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """A singly linked list."""
    def __init__(self):
        self.head = None
    
    def append(self, data):
        """Appends a new node with the given data to the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def remove(self, data):
        """Removes the first node containing the given data."""
        current = self.head
        previous = None
        while current:
            if current.data == data:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return True  # Return True if the node was removed
            previous = current
            current = current.next
        return False  # Return False if the node was not found
    
    def find(self, data):
        """Searches for a node containing the given data. Returns the node if found, None otherwise."""
        current = self.head
        while current:
            if current.data == data:
                return current.data
            current = current.next
        return None
    
    def display(self):
        """Displays the contents of the list."""
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        return elements

# # Example usage:
# inventory = LinkedList()
# inventory.append("blade")
# inventory.append("bread")
# inventory.append("bits")
# print("inventory contents:", inventory.display())
# inventory.remove("bits")
# print("inventory after removing bits:", inventory.display())
# node = inventory.find("bread")
# print("Node found:", node.data if node else "No node found")


# # Example usage assuming each menu is an object or structured data:
# last_menu = LinkedList()
# menu_state1 = {'menu': 'Main', 'selection': 'Start Game'}
# menu_state2 = {'menu': 'Options', 'selection': 'Audio Settings'}
# menu_state3 = {'menu': 'Quit', 'selection': 'Quit'}

# last_menu.append(menu_state1)
# last_menu.append(menu_state2)

# # Display each menu state:
# for state in last_menu.display():
#     print(state)

# print("Bloop"if last_menu.find(menu_state2) is None else "Shoop" )