import pygame

pygame.init()

class Enemy:
    def __init__(self, coords, enemy_type):
        self.surface = pygame.image.load(f"assets/{enemy_type}.png").convert_alpha()
        self.rect = self.surface.get_rect(center = coords)
    