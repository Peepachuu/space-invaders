from bullet import Bullet
import pygame

pygame.init()

VELOCITY = 6
FIRE_RATE = 400
PLAYER_SURFACE = pygame.image.load("assets/player.png").convert_alpha()
STARTING_POSITION = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

class Player:
    def __init__(self, last_fired=pygame.time.get_ticks() - 1000):
        self.sprite = PLAYER_SURFACE
        self.position = STARTING_POSITION

    def move(self, keys_pressed):
        if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:
            self.position[0] -= VELOCITY
        if keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
            self.position[0] += VELOCITY

    def shoot(self, current_time, mouse_pressed, keys_pressed):
        if mouse_pressed[0] or keys[pygame.K_SPACE] and current_time - self.last_fired > FIRE_RATE:
            self.last_fired = current_time
            return Bullet(self.position)