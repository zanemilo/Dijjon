import pygame

class Button:
    """
    A simple Button class for Pygame.
    
    Attributes:
    ----------
    text : str
        The text displayed on the button.
    position : tuple
        The (x, y) coordinates of the button's top-left corner.
    size : tuple
        The width and height of the button.
    font_name : str
        The font used for the button text.
    font_size : int
        The size of the font.
    color : tuple
        The color of the button text in RGB format.
    hover_color : tuple
        The color of the button text when the mouse hovers over it.
    rect : pygame.Rect
        The rectangle representing the button's position and size.
    font : pygame.font.Font
        The font object used to render the text.
    """
    def __init__(self, text, position, size, font_name=None, font_size=30, color=(255, 255, 255), hover_color=(200, 200, 200)):
        self.text = text
        self.position = position
        self.size = size
        self.color = color
        self.hover_color = hover_color
        self.rect = pygame.Rect(position, size)  # Create the button rectangle
        self.font = pygame.font.Font(font_name, font_size)  # Load the font

    def draw(self, screen):
        """
        Draws the button on the screen.
        
        Parameters:
        ----------
        screen : pygame.Surface
            The surface to draw the button on.
        """
        # Check if mouse is over the button
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            current_color = self.hover_color  # Change color on hover
        else:
            current_color = self.color  # Normal color

        # Render the button text
        text_surface = self.font.render(self.text, True, current_color)
        text_rect = text_surface.get_rect(center=self.rect.center)  # Center the text
        screen.blit(text_surface, text_rect)  # Draw the text on the screen

    def is_clicked(self, event):
        """
        Checks if the button is clicked.
        
        Parameters:
        ----------
        event : pygame.event
            The Pygame event to check.
        
        Returns:
        -------
        bool
            True if the button is clicked, False otherwise.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False
