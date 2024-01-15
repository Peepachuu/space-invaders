import pygame

pygame.init()

running = True
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption("Space Invaders")
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("gray")

    pygame.draw.circle(screen, "red", player_pos, 100)
    pygame.display.flip()


    if player_pos[0] < -100 or player_pos[0] > 1380:
        player_pos[0] = screen.get_width() / 2


    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_pos = pygame.Vector2(player_pos[0] - 6, player_pos[1])
    if keys[pygame.K_d]:
        player_pos = pygame.Vector2(player_pos[0] + 6, player_pos[1])

    clock.tick(60)

pygame.quit()