#Standard module
import random

#external module
import pygame

#Self-made module
import app.const as const

class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load(const.APPLE_IMG_PATH).convert()
        self.x = const.DIP_W / 2
        self.y = const.DIP_H / 4 + const.SIZE

    #りんごの描画
    def draw(self):
        #配列の数分描画
        self.parent_screen.blit(self.image, (self.x, self.y))

    #りんごの移動
    def move(self, bad_apples, blocks):
        self.bad_apples = bad_apples
        self.blocks = blocks
        #りんごの新しい座標
        self.make_new_apple()
        #青りんごと座標が重なっていないか確認
        for i in self.bad_apples:
            self.bx = i[0]
            self.by = i[1]
            while self.check_for_bad_apples():
                self.make_new_apple()
        #ブロックの軸と重なっていないか確認
        for i in self.blocks:
            self.block_x = i[0]
            self.block_y = i[1]
            while self.check_for_blocks():
                self.make_new_apple()
        self.draw()

    def make_new_apple(self):
        self.x = abs(random.randint(1, const.DIP_W) - const.SIZE)
        self.y = abs(random.randint(1, const.DIP_H) - const.SIZE)
    #新しい軸が青りんごと重なっていないことを確認
    #重なりがあればTrue
    def check_for_bad_apples(self):
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