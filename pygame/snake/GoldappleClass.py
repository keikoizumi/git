import pygame
import random
import const as CONST

class Goldapple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.cnt = 1
        self.x = -50
        self.y = -50
        self.image = pygame.image.load(CONST.GOLD_APPLE_IMG_PATH).convert()

    def mkapple(self):
        self.x = random.randint(1,24)*CONST.SIZE
        self.y = random.randint(1,14)*CONST.SIZE

    #りんごの描画
    def draw(self):
        #配列の数分描画
        self.parent_screen.blit(self.image, (self.x, self.y))