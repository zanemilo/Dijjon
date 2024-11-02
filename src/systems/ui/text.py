import pygame
from Button import Button

# ------------------------------------------------------------------------------
# TextRenderer Class
# ------------------------------------------------------------------------------

class TextRenderer:
    """
    A class to handle rendering text with a typewriter effect in Pygame.

    Attributes:
        screen (pygame.Surface): The Pygame surface where text will be rendered.
        text (str): The complete text to display with the typewriter effect.
        font (pygame.font.Font): The font used for rendering the text.
        color (tuple): RGB color of the text.
        position (tuple): (x, y) position on the screen where text starts.
        typing_speed (int): Time in milliseconds between each character display.
        displayed_text (str): The portion of text currently displayed.
        text_index (int): Index of the next character to display.
        last_update_time (int): Timestamp of the last character update.
        finished (bool): Flag indicating if the entire text has been displayed.
    """

    def __init__(self, screen, text, font_name, font_size, color, position, typing_speed):
        """
        Initializes the TextRenderer with the given parameters.

        Args:
            screen (pygame.Surface): The surface to render text on.
            text (str): The full text to display.
            font_name (str or None): The name/path of the font file. None for default font.
            font_size (int): Size of the font.
            color (tuple): RGB color tuple for the text.
            position (tuple): (x, y) position for the text on the screen.
            typing_speed (int): Delay in milliseconds between each character.
        """
        self.screen = screen
        self.text = text
        self.font = pygame.font.Font(font_name, font_size)
        self.color = color
        self.position = position
        self.typing_speed = typing_speed  # Time in milliseconds between characters
        self.displayed_text = ''  # Text currently displayed on the screen
        self.text_index = 0  # Index of the next character to display
        self.last_update_time = pygame.time.get_ticks()  # Time when the last character was added
        self.finished = False  # Indicates whether the entire text has been displayed

    def update(self):
        """
        Updates the displayed_text by adding one character at a time based on typing_speed.
        Should be called every frame in the game loop.
        """
        if not self.finished:
            current_time = pygame.time.get_ticks()
            # Check if enough time has passed to add the next character
            if current_time - self.last_update_time > self.typing_speed:
                if self.text_index < len(self.text):
                    # Append the next character to displayed_text
                    self.displayed_text += self.text[self.text_index]
                    self.text_index += 1
                    self.last_update_time = current_time  # Reset the timer
                else:
                    # All characters have been displayed
                    self.finished = True

    def draw(self):
        """
        Renders the currently displayed text onto the screen.
        Should be called every frame in the game loop after update().
        """
        # Render the text surface with the current displayed_text
        text_surface = self.font.render(self.displayed_text, True, self.color)
        # Get the rectangle area for positioning
        text_rect = text_surface.get_rect(topleft=self.position)
        # Blit the text surface onto the screen at the specified position
        self.screen.blit(text_surface, text_rect)

    def reset(self, new_text=None):
        """
        Resets the TextRenderer to display new text.

        Args:
            new_text (str, optional): New text to display. If None, retains the current text.
        """
        if new_text:
            self.text = new_text
        self.displayed_text = ''
        self.text_index = 0
        self.last_update_time = pygame.time.get_ticks()
        self.finished = False

# ------------------------------------------------------------------------------
# display_options Function
# ------------------------------------------------------------------------------

def display_options(options, font_name, font_size, color, hover_color):
    """
    Creates a list of Button objects for the given options.

    Args:
        options (list of str): List of option texts to create buttons for.
        font_name (str or None): The name/path of the font file. None for default font.
        font_size (int): Size of the font for the button text.
        color (tuple): RGB color tuple for the button's normal state.
        hover_color (tuple): RGB color tuple for the button when hovered.

    Returns:
        list of Button: A list containing Button objects for each option.
    """
    buttons = []
    for i, option in enumerate(options):
        # Position buttons vertically spaced by 60 pixels
        button_position = (50, 200 + i * 60)
        button_size = (700, 50)  # Width and height of each button
        # Create a Button object with specified parameters
        button = Button(option, button_position, button_size, font_name, font_size, color, hover_color)
        buttons.append(button)
    return buttons

# ------------------------------------------------------------------------------
# Main Game Code
# ------------------------------------------------------------------------------

# Constants for the game window dimensions
LENGTH = 800
WIDTH = 600

# Initialize Pygame
pygame.init()
# Set up the display window
screen = pygame.display.set_mode((LENGTH, WIDTH))
pygame.display.set_caption('RPG Text Renderer')  # Window title

# Define color constants using RGB tuples
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
DARK_GRAY = (50, 50, 50)
BLACK = (0, 0, 0)

# Font settings
font_name = None  # Use default font provided by Pygame
font_size = 24  # Font size for button text

# Define the player's name
player_name = "Player"

# Define the list of options presented to the player
options = [
    'Swing your fist as hard as you can in the direction of the tugging. [Attack Roll]', 
    'Take a closer look', 
    'Lay completely still.', 
    'Scream as loud as you can!'
]

# Create Button objects for each option
buttons = display_options(options, font_name, 24, (100, 50, 50), (90, 39, 40))

# Create an instance of TextRenderer for the introductory text
intro_text = f"{player_name} . . ."
text_renderer = TextRenderer(
    screen=screen,
    text=intro_text,
    font_name=font_name,
    font_size=36,  # Larger font size for the intro text
    color=(200, 200, 200),  # Light gray color for the text
    position=(LENGTH * 0.1125, WIDTH * 0.175),  # Position calculated as a percentage of window size
    typing_speed=100  # 100 milliseconds between each character
)

# ------------------------------------------------------------------------------
# Main Game Loop
# ------------------------------------------------------------------------------

# Flag to control the main game loop
running = True
# Variable to store the player's selected option
selected_option = None

while running:
    # Event handling loop
    for event in pygame.event.get():
        # If the player closes the window, exit the game loop
        if event.type == pygame.QUIT:
            running = False

        # Check for button clicks only after the text has been fully rendered
        if text_renderer.finished:
            for i, button in enumerate(buttons):
                if button.is_clicked(event):
                    # Store the selected option based on which button was clicked
                    selected_option = options[i]
                    print(f"Selected Option: {selected_option}")
                    # Placeholder for further actions based on the selected option
                    if i == 0:
                        print("Attack: AWT Implementation")
                        # Add your attack logic here
                    elif i == 1:
                        print("Closer Look: AWT Implementation")
                        # Add logic for taking a closer look
                    elif i == 2:
                        print("Stay Still: AWT Implementation")
                        # Add logic for staying still
                    elif i == 3:
                        print("Scream: AWT Implementation")
                        # Add logic for screaming

    # Fill the entire screen with black to clear previous frames
    screen.fill(BLACK)

    # Update the TextRenderer to handle the typewriter effect
    text_renderer.update()
    # Draw the currently displayed portion of the text
    text_renderer.draw()

    # After the text has been fully rendered, draw the option buttons
    if text_renderer.finished:
        for button in buttons:
            button.draw(screen)

    # Update the full display surface to the screen
    pygame.display.flip()


pygame.quit()
