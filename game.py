import pygame

pygame.init()

running = True
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("green")
    pygame.display.flip()

    clock.tick(60)

pygame.quit()