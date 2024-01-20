from bullet import Bullet
import pygame

pygame.init()

VELOCITY = 6
FIRE_RATE = 400
STARTING_POSITION = [640, 360]

class Player:
    def __init__(self):
        self.position = STARTING_POSITION
        self.last_fired = -100

    def move(self, keys_pressed):
        if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:
            self.position[0] -= VELOCITY
        if keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
            self.position[0] += VELOCITY

    def can_shoot(self, current_time, mouse_pressed, keys_pressed):
        return mouse_pressed[0] or keys_pressed[pygame.K_SPACE] and current_time - self.last_fired > FIRE_RATE

    def shoot(self, current_time):
        self.last_fired = current_time
        bullet_position = [self.position[0], self.position[1]]
        return Bullet(bullet_position)

    def out_of_bounds(self, cord_to_place):
        if self.position[0] < -100 or self.position[0] > 1380:
            self.position[0] = cord_to_place