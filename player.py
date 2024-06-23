import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png")
        self.image = pygame.transform.scale(self.image, (90, 65))
        self.final_image = pygame.transform.rotate(self.image, 360)
        self.rect = self.final_image.get_rect()
        self.rect.center = (160, 520)
        self.angle = 0
        self.lives = 3
        self.is_shaking = False
        self.shake_duration = 60  # Duration for shake effect in frames
        self.shake_counter = 0

    def update(self):
        if self.is_shaking:
            self.shake_counter += 1
            if self.shake_counter >= self.shake_duration:
                self.is_shaking = False
                self.shake_counter = 0
            self.rect.x += 5 * (-1) ** self.shake_counter  # Shake effect
            return

        keys = pygame.key.get_pressed()
        self.usable_image = pygame.transform.rotate(self.final_image, 90 + self.angle)
        self.angle = 0

        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
            self.angle = 15
        if keys[pygame.K_RIGHT] and self.rect.right < 400:
            self.rect.x += 5
            self.angle = -15

        self.usable_image = pygame.transform.rotate(self.final_image, 90 + self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def draw(self, surface):
        surface.blit(self.usable_image, self.rect)

    def reset_position(self):
        self.rect.center = (160, 520)
        self.is_shaking = True
        self.shake_counter = 0

    def get_lives(self):
        return self.lives