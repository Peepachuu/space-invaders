VELOCITY = 8
BULLET_SURFACE = pygame.image.load("assets/green.png").convert_alpha()
class Bullet:
    def __init__(self, position):
        self.position = position

    def move(self):
        self.position[1] += VELOCITY