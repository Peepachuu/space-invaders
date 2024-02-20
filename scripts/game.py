import pygame
from bullet import Bullet
from player import Player
from enemy import Enemy
from random import randrange

pygame.init()
pygame.display.set_caption("Space Invaders")

running = True
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
font = pygame.font.Font("../assets/Pixeled.ttf", 20)
background_music = pygame.mixer.Sound('../assets/music.wav')
background_music.set_volume(0.5)
background_music.play(loops = -1)

bullets = []
enemies = []
enemies_moving_right = True
enemy_last_shot = -1000
player = Player()


def setUpEnemies():
    y_cord = 72

    horizontal_gap = 50
    vertical_gap = 40

    def place_enemies(count, enemy_type, enemy_points):
        x_cord = 128
        nonlocal y_cord
        for i in range(1, count + 1):
            enemies.append(Enemy((x_cord, y_cord), enemy_type, enemy_points))
            x_cord += horizontal_gap
            if i % 10 == 0:
                y_cord += vertical_gap
                x_cord = 128

    place_enemies(10, 'yellow', 300)
    place_enemies(20, 'green', 200)
    place_enemies(30, 'red', 100)

setUpEnemies()

def check_bullet_collisions(bullet_index):
    for i in range(len(enemies)):
        if bullets[bullet_index].from_player and pygame.Rect.colliderect(bullets[bullet_index].rect, enemies[i].rect):
            return i
    return None

def check_player_collisions(bullet_index):
    return (not bullets[bullet_index].from_player and pygame.Rect.colliderect(bullets[bullet_index].rect, player.rect))

def move_enemies():
    horizontal_velocity = Enemy.horizontal_velocity * (1 if enemies_moving_right else -1)
    should_move_right = enemies_moving_right
    for enemy in enemies:
        if enemy.rect.right + horizontal_velocity >= screen.get_width():
            should_move_right = False
        elif enemy.rect.left + horizontal_velocity <= 0:
            should_move_right = True
        enemy.rect.x += horizontal_velocity
    if enemies_moving_right != should_move_right:
        for enemy in enemies:
            enemy.rect.bottom += Enemy.vertical_velocity
    return should_move_right

def display_score():
    score_surface = font.render(f"score: {player.score}", False, "White")
    score_rect = score_surface.get_rect()
    score_rect.left = 15
    score_rect.top = -5
    screen.blit(score_surface, score_rect)

def display_player_lives():
    y_cord = 15
    x_cord = 485
    player_surface = player.get_surface()
    for i in range(player.get_lives()):
        screen.blit(player_surface, (x_cord, y_cord))
        x_cord -= 80

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    keys = pygame.key.get_pressed()
    mouse_presses = pygame.mouse.get_pressed()
    current_time = pygame.time.get_ticks()

    screen.blit(player.surface, player.rect)
    display_score()
    display_player_lives()

    if not enemies:
        running = False

    for enemy in enemies:
        screen.blit(enemy.surface, enemy.rect)

    bullets_to_remove = []
    enemies_to_remove = []
    for i in range(len(bullets)):
        enemy_index = check_bullet_collisions(i)
        player_collision = check_player_collisions(i)

        if player_collision:
            running = player.got_hit()
            bullets_to_remove.append(i)

        if enemy_index != None:
            bullets_to_remove.append(i)
            player.update_score(enemies[enemy_index].points)
            enemies_to_remove.append(enemy_index)
            Enemy.enemy_explosion.play()

        if bullets[i].out_of_bounds():
            bullets_to_remove.append(i)
        bullets[i].move()
        pygame.draw.rect(screen, "white", bullets[i].rect)
    pygame.display.flip()

    
    enemies_moving_right = move_enemies()
    player.move(keys)
    if player.can_shoot(current_time, mouse_presses, keys):
        bullets.append(player.shoot(current_time))

    if current_time - enemy_last_shot > 1000:
        rand_index = randrange(len(enemies))
        bullets.append(enemies[rand_index].shoot())
        enemy_last_shot = current_time

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