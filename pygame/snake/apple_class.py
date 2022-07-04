#Standard module
import random

#external module
import pygame

#Self-made module
import const

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
    def move(self, bad_apples):
        #りんごの新しい座標
        self.x = abs(random.randint(1, const.DIP_W) - const.SIZE)
        self.y = abs(random.randint(1, const.DIP_H) - const.SIZE)
        for i in bad_apples:
            self.bx = i[0]
            self.by = i[1]
            #座標が重なっていないか確認
            if ((self.x < self.bx or self.bx + const.SIZE < self.x)
                and (self.y < self.by or self.by + const.SIZE < self.y)):
                pass
            else:
                #座標の再作成
                self.move(bad_apples)
        self.draw()

    #蛇が画面のソトに侵攻した場合
    def out_of_range_move_up(self):
        self.y += const.SIZE
    def out_of_range_move_down(self):
        self.y -= const.SIZE
    def out_of_range_move_right(self):
        self.x -= const.SIZE
    def out_of_range_move_left(self):
        self.x += const.SIZE