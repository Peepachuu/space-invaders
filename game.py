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
    green_enemy_count = 20
    red_enemy_count = 30
    yellow_enemy_count = 10

    y_cord = 72

    horizontal_gap = 50
    vertical_gap = 40

    def place_enemies(count, enemy_type):
        x_cord = 128
        nonlocal y_cord
        for i in range(1, count + 1):
            enemies.append(Enemy((x_cord, y_cord), enemy_type))
            x_cord += horizontal_gap
            if i % 10 == 0:
                y_cord += vertical_gap
                x_cord = 128

    place_enemies(10, 'yellow')
    place_enemies(20, 'green')
    place_enemies(30, 'red')

setUpEnemies()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

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