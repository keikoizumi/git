#external module
import pygame

#Self-made module
import app.const as const

class Grass:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load(const.APPLE_IMG_PATH).convert()
        self.grass_image = pygame.image.load(const.GRASS_IMG_PATH).convert()
        self.grasss = []
        cnt = const.DIP_W / const.SIZE
        for i in range(int(cnt)):
            self.grasss.append([const.SIZE * i, 0])

    def draw(self):
        for i in self.grasss:
            self.x = i[0]
            self.y = i[1]
            self.parent_screen.blit(self.grass_image, (self.x, const.DIP_H - const.SIZE))
