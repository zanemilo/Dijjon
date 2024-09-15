import pygame

class Button:
    def __init__(self, text, pos, size, font, font_size, color, hover_color):
        self.text = text
        self.rect = pygame.Rect(pos, size)
        self.font = pygame.font.Font(font, font_size)
        self.color = color
        self.hover_color = hover_color

    def draw(self, screen):
        # Check if mouse is over the button
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, self.hover_color, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)

        # Render text on the button
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False
