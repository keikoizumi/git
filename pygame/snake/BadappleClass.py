import pygame
import random
import const as CONST

class Badapple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load(CONST.BAD_APPLE_PATH).convert()
        self.x = 840
        self.y = 540

    #りんごの描画
    def draw(self):
        #配列の数分描画
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    #りんごの移動
    def move(self):
        self.x = random.randint(1,24)*CONST.SIZE
        self.y = random.randint(1,14)*CONST.SIZE
        self.draw()
