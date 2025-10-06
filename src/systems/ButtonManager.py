from systems.Button import Button

class ButtonManager:
    """
    Manages buttons including their creation, rendering, and interactions.
    
    Attributes:
    -----------
    screen : pygame.Surface
        The surface on which buttons will be rendered.
    buttons : list
        A list of Button objects currently on the screen.
    """
    def __init__(self, screen):
        self.screen = screen
        self.buttons = []

    def create_buttons(self, options):
        """Create buttons for the given options."""
        self.buttons.clear()  # Clear previous buttons
        for i, option in enumerate(options):
            button = Button(
                text=option, 
                position=(50, 400 + i * 60), 
                size=(700, 50), 
                font_name=None,  # Default font
                font_size=24, 
                color=(255, 255, 255), 
                hover_color=(90, 90, 90)
            )
            self.buttons.append(button)

    def draw_buttons(self):
        """Draw all buttons to the screen."""
        for button in self.buttons:
            button.draw(self.screen)

    def handle_event(self, event):
        """Handle button click events and return the index of the clicked button."""
        for index, button in enumerate(self.buttons):
            if button.is_clicked(event):
                return index
        return None
