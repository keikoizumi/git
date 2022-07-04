#Standard module
import random

#external module
import pygame

#Self-made module
import const

class GoldApple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.cnt = 1
        self.x = -50
        self.y = -50
        self.image = pygame.image.load(const.GOLD_APPLE_IMG_PATH).convert()

    def make_gold_apple(self):
        self.x = random.randint(1, 24) * const.SIZE
        self.y = random.randint(1, 14) * const.SIZE

    #りんごの描画
    def draw(self):
        #配列の数分描画
        self.parent_screen.blit(self.image, (self.x, self.y))

    #蛇が画面のソトに侵攻した場合
    def out_of_range_move_up(self):
        self.y += const.SIZE
    def out_of_range_move_down(self):
        self.y -= const.SIZE
    def out_of_range_move_right(self):
        self.x -= const.SIZE
    def out_of_range_move_left(self):
        self.x += const.SIZE