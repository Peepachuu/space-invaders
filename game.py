import pygame
from bullet import Bullet
from player import Player

pygame.init()
pygame.display.set_caption("Space Invaders")

running = True
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
background_surface = pygame.image.load("assets/tv.png").convert_alpha()

bullets = []
player = Player()


BULLET_SURFACE = pygame.image.load("assets/green.png").convert_alpha()
PLAYER_SURFACE = pygame.image.load("assets/player.png").convert_alpha()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("grey")
    screen.blit(PLAYER_SURFACE, player.position)

    for bullet in bullets:
        bullet.move()
        screen.blit(BULLET_SURFACE, bullet.position)
    pygame.display.flip()

    keys = pygame.key.get_pressed()
    mouse_presses = pygame.mouse.get_pressed()
    current_time = pygame.time.get_ticks()
    
    player.move(keys)
    if player.can_shoot(current_time, mouse_presses, keys):
        bullets.append(player.shoot(current_time))

    clock.tick(60)

pygame.quit()