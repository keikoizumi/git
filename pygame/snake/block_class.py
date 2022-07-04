#Standard module
import random

#external module
import pygame

#Self-made module
import const

class Block:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load(const.APPLE_IMG_PATH).convert()
        self.block_image = pygame.image.load(const.BLOCK_IMG_PATH).convert()
        self.x = []
        self.y = []
        for i in range(30):
            self.x += [const.SIZE * i]
        for i in range(18):
            self.y += [const.SIZE * i]

    def draw(self):
        for i in range(len(self.x) - 1):
            self.parent_screen.blit(self.block_image, (self.x[i], 0))
            self.parent_screen.blit(self.block_image, (self.x[i], const.DIP_H - const.SIZE))
        for i in range(len(self.y) - 1):
            self.parent_screen.blit(self.block_image, (0, self.y[i]))
            self.parent_screen.blit(self.block_image, (const.DIP_W - const.SIZE, self.y[i]))
