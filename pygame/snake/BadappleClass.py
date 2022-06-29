import pygame
import random
import const as CONST

class Badapple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load(CONST.BAD_APPLE_IMG_PATH).convert()
        #二次元配列にバッドアップルを格納する
        self.badapples = [[-50,-50]]

    def mkapple(self, bx, by):
        #新しいりんごの座標
        self.x = random.randint(1,24)*CONST.SIZE
        self.y = random.randint(1,14)*CONST.SIZE
        self.bx = bx
        self.by = by
        if self.x == self.bx and self.y == self.by:
            self.mkapple(self, self.bx, self.by)
        else:
            self.badapples.append([self.x,self.y])

    #りんごの描画
    def draw(self):
        #配列の数分描画
        for i in self.badapples:
            self.x = i[0]
            self.y = i[1]
            self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    #りんごの移動
    def move(self):
        self.x = random.randint(1,24)*CONST.SIZE
        self.y = random.randint(1,14)*CONST.SIZE
        self.draw()
