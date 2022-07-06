#Standard module
import random

#external module
import pygame

#Self-made module
import app.const as const

class BadApple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load(const.BAD_APPLE_IMG_PATH).convert()
        #二次元配列にバッドアップルを格納する
        self.bad_apples = [[-50,-50]]
        self.cnt = 0

    def make_bad_apple(self, bx, by, blocks):
        #腐ったりんごの数
        self.cnt += 1
        #新しいりんごの座標
        self.make_new_apple()
        self.bx = bx
        self.by = by
        self.blocks = blocks
        #座標が重なっていないか確認
        while self.check_for_apples():
            self.make_new_apple()
        #ブロックの軸と重なっていないか確認
        for i in self.blocks:
            self.block_x = i[0]
            self.block_y = i[1]
            while self.check_for_blocks():
                self.make_new_apple()
        self.bad_apples.append([self.x, self.y])

    def make_new_apple(self):
        self.x = random.randint(const.SIZE, const.DIP_W - const.SIZE)
        self.y = random.randint(const.SIZE, const.DIP_H - const.SIZE)
    #新しい軸が青りんごと重なっていないことを確認
    #重なりがあればTrue
    def check_for_apples(self):
        if ((self.x < self.bx or self.bx + const.SIZE < self.x)
            and (self.y < self.by or self.by + const.SIZE < self.y)):
            return False
        else:
            return True
    #新しい軸がブロックの軸と重なっていないことを確認
    #重なりがあればTrue
    def check_for_blocks(self):
        if ((self.block_x + const.SIZE < self.x or self.x < const.DIP_W - const.SIZE * 2)
            and (self.block_y + const.SIZE < self.y or self.y < const.DIP_H - const.SIZE * 2)):
            return False
        else:
            return True

    #りんごの描画
    def draw(self):
        #配列の数分描画
        for i in self.bad_apples:
            self.x = i[0]
            self.y = i[1]
            self.parent_screen.blit(self.image, (self.x, self.y))

    #りんごの移動
    def move(self):
        self.x = random.randint(1, 24) * const.SIZE
        self.y = random.randint(1, 14) * const.SIZE
        self.draw()

    #りんごの削除
    def del_apples(self, cnt_apple):
        self.cnt -= cnt_apple
        for i in range(cnt_apple):
            try:
                del self.bad_apples[-1]
            except IndexError as e:
                pass