import pygame

pygame.init()
VELOCITY = 10
width = 4
height = 12

class Bullet:

    def __init__(self, position, direction, from_player):
        where_to_place = (position[0] - width//2, position[1])
        self.rect = pygame.Rect(where_to_place, (width, height))
        self.direction = direction
        self.from_player = from_player

    def move(self):
        self.rect.bottom += (VELOCITY * self.direction)

    def out_of_bounds(self):
        return (self.rect.bottom < 0 or self.rect.top > 720)
