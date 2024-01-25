import pygame
from bullet import Bullet
from player import Player

pygame.init()
pygame.display.set_caption("Space Invaders")

running = True
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
font = pygame.font.Font("assets/Pixeled.ttf", 50)

bullets = []
player = Player()

FONT_SURFACE = font.render("You win!", False, "Black")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("grey")

    screen.blit(player.surface, player.rect)

    bullets_to_remove = []
    for i in range(len(bullets)):
        if bullets[i].out_of_bounds():
            bullets_to_remove.append(i)
        bullets[i].move()
        pygame.draw.rect(screen, "red", bullets[i].rect)
    pygame.display.flip()

    keys = pygame.key.get_pressed()
    mouse_presses = pygame.mouse.get_pressed()
    current_time = pygame.time.get_ticks()
    
    player.move(keys)
    if player.can_shoot(current_time, mouse_presses, keys):
        bullets.append(player.shoot(current_time))

    current_bullets = []
    for i in range(len(bullets)):
        if i not in bullets_to_remove:
            current_bullets.append(bullets[i])
    bullets = current_bullets

    clock.tick(60)

pygame.quit()