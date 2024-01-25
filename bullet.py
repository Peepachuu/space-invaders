import pygame

pygame.init()
VELOCITY = 8

class Bullet:

    surface = None
    def __init__(self, position):
        self.rect = Bullet.surface.get_rect(center = position)

    def move(self):
        self.rect.bottom -= VELOCITY

    def out_of_bounds(self):
        return self.rect.bottom < 0

    @staticmethod
    def set_surface():
        Bullet.surface = pygame.image.load("assets/green.png").convert_alpha()