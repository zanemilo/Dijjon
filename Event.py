# Dijjon Event class
# Developed & designed by: Zane M Deso
# Purpose: Abstract parent class to quest and encounter classes.


class Event:
    """Event Class acts as abstract parent class to quest and encounter classes. Handles base level functionality such as name, desc, completion status, fail status."""
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.is_active = False
        self.is_completed = False
        self.is_failed = False

    def start(self):
        self.is_active = True
        print(f"Event '{self.name}' has started: {self.description}")

    def end(self):
        self.is_active = False
        if not self.is_failed:
            self.is_completed = True
        print(f"Event '{self.name}' has ended. {'Completed successfully.' if self.is_completed else 'Failed.'}")

    def progress(self, decision=None):
        # This method will be overridden by subclasses to implement specific logic based on decisions
        raise NotImplementedError("Subclasses should implement this method to handle event progression based on player decisions.")

    def display_event_details(self):
        print(f"Event Name: {self.name}")
        print(f"Description: {self.description}")
        print(f"Status: {'Active' if self.is_active else 'Inactive'}")
        print(f"Completed: {'Yes' if self.is_completed else 'No'}")
        print(f"Failed: {'Yes' if self.is_failed else 'No'}")

    def update_status(self, completed=False, failed=False):
        self.is_completed = completed
        self.is_failed = failed
        if completed or failed:
            self.end()


