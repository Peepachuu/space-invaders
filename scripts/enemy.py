import pygame
from bullet import Bullet

pygame.init()


class Enemy:

    vertical_velocity = 10
    horizontal_velocity = 2
    enemy_explosion = pygame.mixer.Sound('../assets/explosion.wav')
    shoot_sound = pygame.mixer.Sound('../assets/laser.wav')
    def __init__(self, coords, enemy_type):
        self.surface = pygame.image.load(f"../assets/{enemy_type}.png").convert_alpha()
        self.rect = self.surface.get_rect(center = coords)

    def shoot(self):
        bullet_position = (self.rect.centerx, self.rect.bottom)
        self.shoot_sound.play()
        return Bullet(bullet_position, 1, False)
