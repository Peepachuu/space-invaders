from bullet import Bullet
import pygame

pygame.init()

VELOCITY = 6
FIRE_RATE = 400
STARTING_POSITION = [640, 360]

class Player:
    def __init__(self):
        self.last_fired = -100
        self.surface = pygame.image.load("../assets/player.png").convert_alpha()
        self.rect = self.surface.get_rect(center = (640, 360))
        self.shoot_sound = pygame.mixer.Sound('../assets/laser.wav')

    def move(self, keys_pressed):
        if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:
            self.rect.left = max(self.rect.left - VELOCITY, 0)
        if keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
            self.rect.right = min(self.rect.right + VELOCITY, 1280)

    def can_shoot(self, current_time, mouse_pressed, keys_pressed):
        return (mouse_pressed[0] or keys_pressed[pygame.K_SPACE]) and current_time - self.last_fired > FIRE_RATE

    def shoot(self, current_time):
        self.last_fired = current_time
        bullet_position = (self.rect.centerx, self.rect.top)
        self.shoot_sound.play()
        return Bullet(bullet_position, -1, True)
