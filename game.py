import pygame
from bullet import Bullet
from player import Player
from enemy import Enemy

pygame.init()
pygame.display.set_caption("Space Invaders")

running = True
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
font = pygame.font.Font("assets/Pixeled.ttf", 50)

bullets = []
enemies = []
player = Player()

FONT_SURFACE = font.render("You win!", False, "Black")


def setUpEnemies():
    green_enemy_count = 10
    red_enemy_count = 10
    yellow_enemy_count = 10

    enemy_type = 'green'
    horizontal_gap = 50
    vertical_gap = 30

    current_x = 128
    current_y = 72
    for i in range(green_enemy_count):
        enemies.append(Enemy((current_x, current_y), enemy_type))
        current_x += horizontal_gap

    current_y += vertical_gap
    current_x = 128
    enemy_type = 'red'
    for i in range(red_enemy_count):
        enemies.append(Enemy((current_x, current_y), enemy_type))
        current_x += horizontal_gap

    current_y += vertical_gap
    current_x = 128
    enemy_type = 'yellow'
    for i in range(yellow_enemy_count):
        enemies.append(Enemy((current_x, current_y), enemy_type))
        current_x += horizontal_gap 
    
setUpEnemies()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("grey")

    screen.blit(player.surface, player.rect)

    for enemy in enemies:
        screen.blit(enemy.surface, enemy.rect)

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
