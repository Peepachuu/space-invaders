import pygame

VELOCITY = 8

class Bullet:
    def __init__(self, position):
        self.position = position

    def move(self):
        self.position[1] -= VELOCITY

    def out_of_bounds(self):
        return self.position[1] < -20