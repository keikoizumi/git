#Standard module
import random

#external module
import pygame

#Self-made module
import const

class BadApple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load(const.BAD_APPLE_IMG_PATH).convert()
        #二次元配列にバッドアップルを格納する
        self.bad_apples = [[-50,-50]]
        self.cnt = 0

    def mkapple(self, bx, by):
        #腐ったりんごの数
        self.cnt += 1
        #新しいりんごの座標
        self.x = random.randint(1, 24) * const.SIZE
        self.y = random.randint(1, 14) * const.SIZE
        self.bx = bx
        self.by = by
        if self.x == self.bx and self.y == self.by:
            self.mkapple(self, self.bx, self.by)
        else:
            self.bad_apples.append([self.x, self.y])

    #りんごの描画
    def draw(self):
        #配列の数分描画
        for i in self.bad_apples:
            self.x = i[0]
            self.y = i[1]
            self.parent_screen.blit(self.image, (self.x, self.y))
        print(self.bad_apples)

    #りんごの移動
    def move(self):
        self.x = random.randint(1, 24) * const.SIZE
        self.y = random.randint(1, 14) * const.SIZE
        self.draw()

    #りんごの削除
    def del_apples(self, cnt_apple):
        self.cnt -= cnt_apple
        for i in range(cnt_apple):
            del self.bad_apples[-1]
