#Standard module
import datetime
import random

#external moduleskin_color
import pygame
from numpy import append, outer

#Self-made module
import const

class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        #スキンカラーの設定
        v = random.randint(1, 3)
        if v == 1:
            self.skin_color = 'red'
            self.image = pygame.image.load(const.SNAKE_RED_IMG_PATH).convert()
            self.face = pygame.image.load(const.SNAKE_RED_FACE_IMG_PATH).convert()
        elif v == 2:
            self.skin_color = 'green'
            self.image = pygame.image.load(const.SNAKE_GREEN_IMG_PATH).convert()
            self.face = pygame.image.load(const.SNAKE_GREEN_FACE_IMG_PATH).convert()
        else:
            self.skin_color = 'yellow'
            self.image = pygame.image.load(const.SNAKE_YELLOW_IMG_PATH).convert()
            self.face = pygame.image.load(const.SNAKE_YELLOW_FACE_IMG_PATH).convert()
        self.face = pygame.transform.rotate(self.face, 180)
        #最初のお顔を保存
        self.init_face = self.face
        #最初の体を保存
        self.init_body = self.image
        #初期方向
        self.directions = ['down', 'down']
        self.get_gold_apple = False
        #初期長
        self.length = 1
        #初期位置
        self.x = [const.SIZE]
        self.y = [const.SIZE]
        #時間
        self.d = datetime.datetime.now() + datetime.timedelta(days=-7)
        #speed はノーマル
        self.s_cnt = 0
        #舌を出さない
        self.out = False
        #速く動く
        self.fast_move = False
        self.panic_cnt = 0
        self.draw()

    def move_left(self):
        #お顔の向きを整える
        if self.directions[1] == 'up':
            self.face = pygame.transform.rotate(self.face, 90)
        elif self.directions[1] == 'down':
            self.face = pygame.transform.rotate(self.face, -90)
        elif self.directions[1] == 'right':
            self.face = pygame.transform.rotate(self.face, 180)
        else:
            self.face = pygame.transform.rotate(self.face, 0)
        self.directions.pop(0)
        self.directions.append('left')

    def move_right(self):
        if self.directions[1] == 'up':
            self.face = pygame.transform.rotate(self.face, -90)
        elif self.directions[1] == 'down':
            self.face = pygame.transform.rotate(self.face, 90)
        elif self.directions[1] == 'left':
            self.face = pygame.transform.rotate(self.face, 180)
        else:
            self.face = pygame.transform.rotate(self.face, 0)
        self.directions.pop(0)
        self.directions.append('right')

    def move_up(self):
        if self.directions[1] == 'down':
            self.face = pygame.transform.rotate(self.face, 180)
        elif self.directions[1] == 'left':
            self.face = pygame.transform.rotate(self.face, -90)
        elif self.directions[1] == 'right':
            self.face = pygame.transform.rotate(self.face, 90)
        else:
            self.face = pygame.transform.rotate(self.face, 0)
        self.directions.pop(0)
        self.directions.append('up')

    def move_down(self):
        if self.directions[1] == 'up':
            self.face = pygame.transform.rotate(self.face, 180)
        elif self.directions[1] == 'left':
            self.face = pygame.transform.rotate(self.face, 90)
        elif self.directions[1] == 'right':
            self.face = pygame.transform.rotate(self.face, -90)
        else:
            self.face = pygame.transform.rotate(self.face, 0)
        self.directions.pop(0)
        self.directions.append('down')

    def walk(self):
        # update body
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
            #しっぽの配列 しっぽはあきらめる！
        #体のポジション
        if self.directions[1] == 'left':
            self.x[0] -= const.SIZE
        if self.directions[1] == 'right':
            self.x[0] += const.SIZE
        if self.directions[1] == 'up':
            self.y[0] -= const.SIZE
        if self.directions[1] == 'down':
            self.y[0] += const.SIZE
        self.draw()

    def draw(self):
        for i in range(self.length - 1):
            self.parent_screen.blit(self.face, (self.x[0], self.y[0]))
            self.parent_screen.blit(self.image, (self.x[i + 1], self.y[i + 1]))

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def decrease_length(self):
        if self.length != 1:
            if self.length > 1 and self.length <= 5:
                self.length -= 1
                del self.x[-1]
                del self.y[-1]
            elif self.length > 5 and self.length <= 10:
                self.length -= 3
                del self.x[-3]
                del self.y[-3]
            elif self.length > 10 and self.length <= 15:
                self.length -= 5
                del self.x[-5]
                del self.y[-5]
            elif self.length > 15 and self.length <= 30:
                self.length -= 5
                del self.x[-5]
                del self.y[-5]
            elif self.length > 30:
                self.length -= 10
                del self.x[-10]
                del self.y[-10]

    #goldを食べたときのスキンエフェクト
    def chcg(self):
        if self.get_gold_apple:
            cnt = 0
            while cnt < 100:
                self.image = pygame.image.load(const.SNAKE_RED_IMG_PATH).convert()
                self.draw()
                pygame.display.flip()
                self.image = pygame.image.load(const.SNAKE_GREEN_IMG_PATH).convert()
                self.draw()
                pygame.display.flip()
                self.image = pygame.image.load(const.SNAKE_YELLOW_IMG_PATH).convert()
                self.draw()
                pygame.display.flip()
                cnt += 1
            self.get_gold_apple = False
            self.image = self.init_body
            pygame.display.flip()

    def had_bad_apple(self):
        #スキンエフェクト
        cnt = 0
        while cnt < 100:
            #bad face 表示
            if self.skin_color == 'red':
                self.face = pygame.image.load(const.SNAKE_RED_HAD_BAD_APPLE_FACE_IMG_PATH).convert()
            elif self.skin_color == 'green':
                self.face = pygame.image.load(const.SNAKE_GREEN_HAD_BAD_APPLE_FACE_IMG_PATH).convert()
            else:
                self.face = pygame.image.load(const.SNAKE_YELLOW_HAD_BAD_APPLE_FACE_IMG_PATH).convert()
            if self.directions[1] == 'up':
                self.face = pygame.transform.rotate(self.face, 0)
            elif self.directions[1] == 'down':
                self.face = pygame.transform.rotate(self.face, 180)
            elif self.directions[1] == 'right':
                self.face = pygame.transform.rotate(self.face, -90)
            else:
                self.face = pygame.transform.rotate(self.face, 90)

            #スキンエフェクト 青色
            self.image = pygame.image.load(const.SNAKE_BLUE_IMG_PATH).convert()
            self.draw()
            pygame.display.flip()
            self.image = self.init_body
            self.draw()
            pygame.display.flip()
            cnt += 1
        self.get_gold_apple = False
        #体は青色にする
        self.image = pygame.image.load(const.SNAKE_BLUE_IMG_PATH).convert()
        self.face = self.init_face
        pygame.display.flip()

    def tongue(self):
        #舌を出すフェクト
        if self.out:
            if self.skin_color == 'red':
                self.face = pygame.image.load(const.SNAKE_RED_EATING_FACE_IMG_PATH).convert()
            elif self.skin_color == 'green':
                self.face = pygame.image.load(const.SNAKE_GREEN_EATING_FACE_IMG_PATH).convert()
            else:
                self.face = pygame.image.load(const.SNAKE_YELLOW_EATING_FACE_IMG_PATH).convert()

            if self.directions[1] == 'up':
                self.face = pygame.transform.rotate(self.face, 0)
            elif self.directions[1] == 'down':
                self.face = pygame.transform.rotate(self.face, 180)
            elif self.directions[1] == 'right':
                self.face = pygame.transform.rotate(self.face, -90)
            else:
                self.face = pygame.transform.rotate(self.face, 90)
        else:
            self.face = self.init_face
            if self.directions[1] == 'up':
                self.face = pygame.transform.rotate(self.face, 180)
            elif self.directions[1] == 'down':
                self.face = pygame.transform.rotate(self.face, 0)
            elif self.directions[1] == 'right':
                self.face = pygame.transform.rotate(self.face, 90)
            else:
                self.face = pygame.transform.rotate(self.face, -90)

    def speedup(self):
        #秒間speed up
        if self.s_cnt == 1:
            self.d = datetime.datetime.now() + datetime.timedelta(seconds=10)
