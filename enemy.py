import pygame
import random

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

class Enemy1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load("enemy1.png")
        self.image = pygame.transform.scale(self.original_image, (90, 65))
        self.image = pygame.transform.rotate(self.image, 270)
        self.rect = self.image.get_rect(center=(random.randint(40, SCREEN_WIDTH // 2 - 40), 0))

    def update(self):
        self.rect.y += 5
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.centerx = random.randint(40, SCREEN_WIDTH // 2 - 40)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Enemy2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load("enemy2.png")
        self.image = pygame.transform.scale(self.original_image, (90, 65))
        self.image = pygame.transform.rotate(self.image, 270)
        self.rect = self.image.get_rect(center=(random.randint(SCREEN_WIDTH // 2 + 40, SCREEN_WIDTH - 40), 0))

    def update(self):
        self.rect.y += 5
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.centerx = random.randint(SCREEN_WIDTH // 2 + 40, SCREEN_WIDTH - 40)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
