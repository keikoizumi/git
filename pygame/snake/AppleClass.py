import pygame
import random
import const as CONST

class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load(CONST.APPLE_IMG_PATH).convert()
        self.x = 40
        self.y = 340

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
