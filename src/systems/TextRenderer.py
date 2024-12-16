import pygame

class TextRenderer:
    """
    Renders text to the screen with a typing effect and supports text wrapping.
    
    Attributes:
    ----------
    screen : pygame.Surface
        The surface on which the text will be rendered.
    text : str
        The complete text to render.
    font : pygame.font.Font
        The font used to render the text.
    color : tuple
        The color of the text in RGB format.
    position : tuple
        The (x, y) position where the text starts.
    typing_speed : int
        The speed of the typing effect in milliseconds between characters.
    rect_width : int
        The width of the rectangular area for text wrapping.
    """
    def __init__(self, screen, font_name, font_size, color, position, typing_speed, rect_width):
        self.screen = screen
        self.font = pygame.font.Font(font_name, font_size)
        self.color = color
        self.position = position
        self.typing_speed = typing_speed  # Time in milliseconds between characters
        self.rect_width = rect_width
        self.lines = []  # List of lines to render
        self.displayed_text = ''
        self.text_index = 0
        self.last_update_time = pygame.time.get_ticks()
        self.finished = False
        self.set_text("")

    def set_text(self, text):
        """Set a new text to render."""
        self.text = text
        self.lines = []  # Clear previous lines
        self.displayed_text = ''
        self.text_index = 0
        self.last_update_time = pygame.time.get_ticks()
        self.finished = False
        self.prepare_lines()

    def prepare_lines(self):
        """Split the text into lines that fit within the rect_width."""
        words = self.text.split()
        line = ''
        for word in words:
            # Check if adding the word exceeds the width
            if self.font.size(line + word)[0] <= self.rect_width:
                line += word + ' '
            else:
                self.lines.append(line.strip())
                line = word + ' '
        if line:
            self.lines.append(line.strip())

    def update(self):
        """Updates the displayed text with a typing effect."""
        if not self.finished:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_update_time > self.typing_speed:
                if self.text_index < len(self.text):
                    self.displayed_text += self.text[self.text_index]
                    self.text_index += 1
                    self.last_update_time = current_time
                else:
                    self.finished = True

    def draw(self):
        """Draws the current state of the text to the screen, wrapping within the rectangle area."""
        # Split the displayed text into lines
        words = self.displayed_text.split()
        rendered_lines = []
        line = ''
        for word in words:
            if self.font.size(line + word)[0] <= self.rect_width:
                line += word + ' '
            else:
                rendered_lines.append(line.strip())
                line = word + ' '
        if line:
            rendered_lines.append(line.strip())

        # Draw each line at the specified position
        y_offset = 0
        for line in rendered_lines:
            text_surface = self.font.render(line, True, self.color)
            text_rect = text_surface.get_rect(topleft=(self.position[0], self.position[1] + y_offset))
            self.screen.blit(text_surface, text_rect)
            y_offset += self.font.get_linesize()
