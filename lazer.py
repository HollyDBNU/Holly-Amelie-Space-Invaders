
import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, speed, screen_height):
        super().__init__()
        self.image = pygame.Surface((2, 12))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=pos)
        self.speed = speed
        self.screen_height = screen_height

    def update(self):
        self.rect.y += abs(self.speed)
        if self.rect.top > self.screen_height:
            self.kill()
