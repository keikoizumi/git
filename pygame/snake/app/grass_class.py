import random

#external module
import pygame

#Self-made module
import app.const as const

class Grass:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load(const.APPLE_IMG_PATH).convert()
        self.grass_image = pygame.image.load(const.GRASS_IMG_PATH).convert()
        self.two_x1 = random.randint(const.SIZE * 5, const.PLAY_DIP_W - const.SIZE * 2)
        self.two_y1 = random.randint(const.SIZE * 5, const.DIP_H / 2 - const.SIZE * 2)
        self.two_x2 = random.randint(const.SIZE * 5, const.PLAY_DIP_W - const.SIZE * 2)
        self.two_y2 = random.randint(const.DIP_H / 2, const.DIP_H - const.SIZE * 2)
        self.two_grass = [
                            [self.two_x1, self.two_y1]
                            ,[self.two_x1 + const.SIZE, self.two_y1]
                            ,[self.two_x2, self.two_y2]
                            ,[self.two_x2 + const.SIZE, self.two_y2]
                            ,[self.two_x2 + const.SIZE * 2, self.two_y2]
        ]
        self.grasss = []
        cnt = const.DIP_W / const.SIZE
        for i in range(int(cnt)):
            self.grasss.append([const.SIZE * i, 0])

    def draw(self):
        for i in self.two_grass:
            self.two_x = i[0]
            self.two_y = i[1]
            self.parent_screen.blit(self.grass_image, (self.two_x, self.two_y))

        for i in self.grasss:
            self.x = i[0]
            self.y = i[1]
            self.parent_screen.blit(self.grass_image, (self.x, const.DIP_H - const.SIZE))


