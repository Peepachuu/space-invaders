import pygame
import bullet

pygame.init()

running = True
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption("Space Invaders")
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_surface = pygame.image.load("assets/player.png").convert_alpha()
background_surface = pygame.image.load("assets/tv.png").convert_alpha()
laser_surface = pygame.image.load("assets/green.png").convert_alpha()
bullets = []
last_fired = pygame.time.get_ticks() - 1000
time_between_bullets = 500
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("grey")
    screen.blit(player_surface, player_pos)


    for bul in bullets:
        screen.blit(laser_surface, bul.position)
        bul.position = pygame.Vector2(bul.position[0], bul.position[1])
    pygame.display.flip()


    if player_pos[0] < -100 or player_pos[0] > 1380:
        player_pos[0] = screen.get_width() / 2


    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_pos = pygame.Vector2(player_pos[0] - 6, player_pos[1])
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_pos = pygame.Vector2(player_pos[0] + 6, player_pos[1])

    mouse_presses = pygame.mouse.get_pressed()
    current_time = pygame.time.get_ticks()
    if mouse_presses[0] or keys[pygame.K_SPACE] and current_time - last_fired > time_between_bullets:
        newBullet = bullet.Bullet(player_pos)
        bullets.append(newBullet)
        last_fired = current_time

    clock.tick(60)

pygame.quit()