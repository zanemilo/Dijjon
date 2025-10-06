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
        self.ui_buttons = []

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

    def create_UI_buttons(self, options, pos=(100, 600)):
        """Create UI buttons for the given options."""
        self.ui_buttons.clear()  # Clear previous buttons
        for i, option in enumerate(options):
            button = Button(
                text=option, 
                position=pos, 
                size=(700, 50), 
                font_name=None,  # Default font
                font_size=24, 
                color=(150, 255, 100), 
                hover_color=(80, 90, 70)
            )
            self.ui_buttons.append(button)

    def draw_buttons(self):
        """Draw all buttons to the screen."""
        for button in self.buttons:
            button.draw(self.screen)
        for ui_button in self.ui_buttons:
            ui_button.draw(self.screen)

    def handle_event(self, event):
        """Handle button click events and return the index of the clicked button."""
        for index, button in enumerate(self.buttons):
            if button.is_clicked(event):
                return index
        
        return None
    
    def handle_UI_event(self, event):
        """Handle UI button click events and return the index of the clicked button."""
        for ui_index, ui_button in enumerate(self.ui_buttons):
            if ui_button.is_clicked(event):
                return ui_index
        return None
    
