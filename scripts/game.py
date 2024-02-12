import pygame
from bullet import Bullet
from player import Player
from enemy import Enemy

pygame.init()
pygame.display.set_caption("Space Invaders")

running = True
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
font = pygame.font.Font("../assets/Pixeled.ttf", 50)
background_music = pygame.mixer.Sound('../assets/music.wav')
background_music.set_volume(0.5)
background_music.play(loops = -1)

bullets = []
enemies = []
player = Player()

FONT_SURFACE = font.render("You win!", False, "Black")


def setUpEnemies():
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


def check_bullet_collisions(bullet_index):
    for i in range(len(enemies)):
        if pygame.Rect.colliderect(bullets[bullet_index].rect, enemies[i].rect):
            return i
    return None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    screen.blit(player.surface, player.rect)

    for enemy in enemies:
        screen.blit(enemy.surface, enemy.rect)

    bullets_to_remove = []
    enemies_to_remove = []
    for i in range(len(bullets)):
        enemy_index = check_bullet_collisions(i)
        if enemy_index != None:
            bullets_to_remove.append(i)
            enemies_to_remove.append(enemy_index)
            Enemy.enemy_explosion.play()

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

    current_enemies = []
    for i in range(len(enemies)):
        if i not in enemies_to_remove:
            current_enemies.append(enemies[i])
    enemies = current_enemies

    clock.tick(60)

pygame.quit()