import pygame
import sys

sys.path.append("..")  # Adds the parent directory to the Python module search path

from systems.ui.Button import Button


# ------------------------------------------------------------------------------
# TextRenderer Class
# ------------------------------------------------------------------------------

class TextRenderer:
    """
    Typewriter + word-wrapped text renderer for Pygame.

    Usage:
        tr = TextRenderer(
            screen=screen,
            text="",
            font_name=None,         # use default pygame font by default
            font_size=24,
            color=(255,255,255),
            position=(50, 100),
            typing_speed=50,        # ms per character
            line_spacing=6,
            max_width=None,         # if None, uses screen.get_width() - position[0] - right_margin
            right_margin=50,
            align="left"            # "left", "center", "right"
        )
        tr.reset("Your long paragraph ...")
        ...
        tr.update()
        tr.draw()
    """

    def __init__(
        self,
        screen,
        text="",
        font_name=None,
        font_size=24,
        color=(255, 255, 255),
        position=(50, 100),
        typing_speed=50,
        line_spacing=6,
        max_width=550,
        max_length=557,
        right_margin=50,
        align="left",
    ):
        self.screen = screen
        self.text = text or ""
        self.font = pygame.font.Font(font_name, font_size)
        self.color = color
        self.x, self.y = position
        self.typing_speed = max(1, int(typing_speed))
        self.line_spacing = line_spacing
        self.right_margin = right_margin
        self.align = align
        self.max_length = max_length
        scr_w = self.screen.get_width()
        self.max_width = max_width if max_width is not None else max(10, scr_w - self.x - self.right_margin)

        # typewriter state
        self.display_char_count = 0
        self.last_update_time = 0
        self.finished = False

        # cache of wrapped lines for the CURRENT visible substring
        self._wrapped_lines = []

        # initialize with current text
        self._recompute_wrapping()

    # -----------------------------
    # Public API (used by main.py)
    # -----------------------------
    def reset(self, new_text: str):
        """Reset to a new text and restart the typewriter effect."""
        self.text = new_text or ""
        if self.max_length is not None:
            self.text = self.text[: self.max_length]
        self.display_char_count = 0
        self.last_update_time = 0
        self.finished = False
        self._recompute_wrapping()

    def update(self):
        """Advance the typewriter effect based on elapsed time."""
        if self.finished:
            return
        now = pygame.time.get_ticks()
        if self.last_update_time == 0:
            self.last_update_time = now
            return

        elapsed = now - self.last_update_time
        # how many characters to reveal since last tick
        chars_to_add = elapsed // self.typing_speed
        if chars_to_add > 0:
            self.display_char_count = min(len(self.text), self.display_char_count + chars_to_add)
            self.last_update_time = now
            self.finished = (self.display_char_count >= len(self.text))
            # recompute wrapping for the visible substring
            self._recompute_wrapping()

    def draw(self):
        """Render the currently visible, word-wrapped text."""
        line_y = self.y
        for surf, rect in self._line_surfaces(self._wrapped_lines):
            rect.topleft = (self._aligned_x(rect.width), line_y)
            self.screen.blit(surf, rect)
            line_y += rect.height + self.line_spacing

    # -----------------------------
    # Internals
    # -----------------------------
    def _visible_text(self) -> str:
        # Respect explicit newlines; typewriter reveals through them
        visible = self.text[: self.display_char_count]
        if self.max_length is not None:
            visible = visible[: self.max_length]
        return visible

    def _recompute_wrapping(self):
        vt = self._visible_text()
        self._wrapped_lines = self._wrap_text(vt, self.max_width)

    def _wrap_text(self, text: str, max_width: int):
        """
        Wrap text by words to fit within max_width (in pixels).
        Preserves explicit '\n' as hard breaks.
        """
        lines = []
        font = self.font

        for paragraph in text.split("\n"):
            if not paragraph:
                # Preserve blank line
                lines.append("")
                continue

            words = paragraph.split(" ")
            cur_line = ""
            for w in words:
                candidate = w if not cur_line else (cur_line + " " + w)
                if font.size(candidate)[0] <= max_width:
                    cur_line = candidate
                else:
                    # If a single long token itself exceeds width, hard-break within the token
                    if not cur_line:
                        cur_line = self._hard_break_long_token(w, max_width)
                        # _hard_break_long_token returns a list of segments except possibly last short piece
                        *full_segs, tail = cur_line
                        lines.extend(full_segs)
                        cur_line = tail
                    else:
                        lines.append(cur_line)
                        # start a new line with current word; if it still doesn't fit, hard-break it
                        if font.size(w)[0] <= max_width:
                            cur_line = w
                        else:
                            segs = self._hard_break_long_token(w, max_width)
                            *full_segs, tail = segs
                            lines.extend(full_segs)
                            cur_line = tail

            if cur_line:
                lines.append(cur_line)

        return lines

    def _hard_break_long_token(self, token: str, max_width: int):
        """
        Break a single overlong token (e.g., a long URL or unspaced hyphen string)
        into chunks that fit the width. Returns list of pieces; caller will place all
        but the last as fixed lines, and keep the last as the current line.
        """
        pieces = []
        start = 0
        while start < len(token):
            lo, hi = start + 1, len(token)
            best = start + 1
            # binary search the longest slice that fits
            while lo <= hi:
                mid = (lo + hi) // 2
                if self.font.size(token[start:mid])[0] <= max_width:
                    best = mid
                    lo = mid + 1
                else:
                    hi = mid - 1
            pieces.append(token[start:best])
            start = best
        return pieces

    def _line_surfaces(self, lines):
        for line in lines:
            surf = self.font.render(line, True, self.color)
            yield surf, surf.get_rect()

    def _aligned_x(self, line_width: int) -> int:
        if self.align == "left":
            return self.x
        elif self.align == "center":
            return self.x + (self.max_width - line_width) // 2
        elif self.align == "right":
            return self.x + (self.max_width - line_width)
        else:
            return self.x


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

# # ------------------------------------------------------------------------------
# # EXAMPLE Main Game Code
# # ------------------------------------------------------------------------------

# # Constants for the game window dimensions
# LENGTH = 800
# WIDTH = 600

# # Initialize Pygame
# pygame.init()
# # Set up the display window
# screen = pygame.display.set_mode((LENGTH, WIDTH))
# pygame.display.set_caption('RPG Text Renderer')  # Window title

# # Define color constants using RGB tuples
# WHITE = (255, 255, 255)
# GRAY = (150, 150, 150)
# DARK_GRAY = (50, 50, 50)
# BLACK = (0, 0, 0)

# # Font settings
# font_name = None  # Use default font provided by Pygame
# font_size = 24  # Font size for button text

# # Define the player's name
# player_name = "Player"

# # Define the list of options presented to the player
# options = [
#     'Swing your fist as hard as you can in the direction of the tugging. [Attack Roll]', 
#     'Take a closer look', 
#     'Lay completely still.', 
#     'Scream as loud as you can!'
# ]

# # Create Button objects for each option
# buttons = display_options(options, font_name, 24, (100, 50, 50), (90, 39, 40))

# # Create an instance of TextRenderer for the introductory text
# intro_text = f"{player_name} . . ."
# text_renderer = TextRenderer(
#     screen=screen,
#     text=intro_text,
#     font_name=font_name,
#     font_size=36,  # Larger font size for the intro text
#     color=(200, 200, 200),  # Light gray color for the text
#     position=(LENGTH * 0.1125, WIDTH * 0.175),  # Position calculated as a percentage of window size
#     typing_speed=100  # 100 milliseconds between each character
# )

# # ------------------------------------------------------------------------------
# # Main Game Loop
# # ------------------------------------------------------------------------------

# # Flag to control the main game loop
# running = True
# # Variable to store the player's selected option
# selected_option = None

# while running:
#     # Event handling loop
#     for event in pygame.event.get():
#         # If the player closes the window, exit the game loop
#         if event.type == pygame.QUIT:
#             running = False

#         # Check for button clicks only after the text has been fully rendered
#         if text_renderer.finished:
#             for i, button in enumerate(buttons):
#                 if button.is_clicked(event):
#                     # Store the selected option based on which button was clicked
#                     selected_option = options[i]
#                     print(f"Selected Option: {selected_option}")
#                     # Placeholder for further actions based on the selected option
#                     if i == 0:
#                         print("Attack: AWT Implementation")
#                         # Add your attack logic here
#                     elif i == 1:
#                         print("Closer Look: AWT Implementation")
#                         # Add logic for taking a closer look
#                     elif i == 2:
#                         print("Stay Still: AWT Implementation")
#                         # Add logic for staying still
#                     elif i == 3:
#                         print("Scream: AWT Implementation")
#                         # Add logic for screaming

#     # Fill the entire screen with black to clear previous frames
#     screen.fill(BLACK)

#     # Update the TextRenderer to handle the typewriter effect
#     text_renderer.update()
#     # Draw the currently displayed portion of the text
#     text_renderer.draw()

#     # After the text has been fully rendered, draw the option buttons
#     if text_renderer.finished:
#         for button in buttons:
#             button.draw(screen)

#     # Update the full display surface to the screen
#     pygame.display.flip()


# pygame.quit()

  