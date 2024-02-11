import pygame

pygame.init()
VELOCITY = 8
width = 6
height = 6

class Bullet:

    def __init__(self, position):
        where_to_place = (position[0] - width//2, position[1])
        self.rect = pygame.Rect(where_to_place, (width, height))

    def move(self):
        self.rect.bottom -= VELOCITY

    def out_of_bounds(self):
        return self.rect.bottom < 0
