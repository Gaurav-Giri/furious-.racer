import pygame
import random
from textWithBorder import draw_text_with_border

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

class Coin(pygame.sprite.Sprite):
    def __init__(self, font, text_col, border_col, border_thickness):
        super().__init__()
        self.font = font
        self.text_col = text_col
        self.border_col = border_col
        self.border_thickness = border_thickness
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(random.randint(40, SCREEN_WIDTH - 40), random.randint(40, SCREEN_HEIGHT // 2)))
        self.draw_coin()

    def draw_coin(self):
        self.image.fill((0, 0, 0, 0))
        draw_text_with_border(self.image, "$", self.font, self.text_col, self.border_col, 5, 5, self.border_thickness)

    def update(self):
        self.rect.y += 3  # Move the coin down the screen
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.bottom = 0
            self.rect.centerx = random.randint(40, SCREEN_WIDTH - 40)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
