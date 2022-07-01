#from ctypes.wintypes import SIZE
#from tkinter import W
from numpy import append, outer
import datetime
import random
import pygame
import CONST

class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        #スキンカラーの設定
        v = random.randint(1,3)
        #v = 3
        if v == 1:
            self.skincolor = 'red'
            self.image = pygame.image.load(CONST.SNAKE_RED_IMG_PATH).convert()
            self.face = pygame.image.load(CONST.SNAKE_RED_FACE_IMG_PATH).convert()
        elif v == 2:
            self.skincolor = 'green'
            self.image = pygame.image.load(CONST.SNAKE_GREEN_IMG_PATH).convert()
            self.face = pygame.image.load(CONST.SNAKE_GREEN_FACE_IMG_PATH).convert()
        else:
            self.skincolor = 'yellow'
            self.image = pygame.image.load(CONST.SNAKE_YELLOW_IMG_PATH).convert()
            self.face = pygame.image.load(CONST.SNAKE_YELLOW_FACE_IMG_PATH).convert()
            #self.tail = pygame.image.load(CONST.SNAKE_YELLOW_TAIL_IMG_PATH).convert()

        self.face = pygame.transform.rotate(self.face,180)
        #最初のお顔を保存
        self.iniface = self.face

        #最初の体を保存
        self.inibody = self.image
        #self.tail = pygame.transform.rotate(self.tail,180

        #初期方向
        self.directions = ['down','down']
        self.get_gold_apple = False
        #初期長
        self.length = 1
        #初期位置
        self.x = [CONST.SIZE]
        self.y = [CONST.SIZE]
        #self.x.append(-1)
        #self.y.append(-1)
        #self.x.append(-2)
        #self.y.append(-2)

        #時間
        self.d = datetime.datetime.now() + datetime.timedelta(days=-7)

        #speed はノーマル
        self.scnt = 0

        #舌を出さない
        self.out = False

        #速く動く
        self.fastmove = False

        self.paniccnt = 0

        self.draw()

    def move_left(self):
        #お顔の向きを整える
        if self.directions[1] == 'up':
            self.face = pygame.transform.rotate(self.face,90)
            #self.tail = pygame.transform.rotate(self.tail,90)
        elif self.directions[1] == 'down':
            self.face = pygame.transform.rotate(self.face,-90)
            #self.tail = pygame.transform.rotate(self.tail,-90)
        elif self.directions[1] == 'right':
            self.face = pygame.transform.rotate(self.face,180)
            #self.tail = pygame.transform.rotate(self.tail,180)
        else:
            self.face = pygame.transform.rotate(self.face,0)
            #self.tail = pygame.transform.rotate(self.tail,0)

        self.directions.pop(0)
        self.directions.append('left')

    def move_right(self):
        if self.directions[1] == 'up':
            self.face = pygame.transform.rotate(self.face,-90)
            #self.tail = pygame.transform.rotate(self.tail,-90)
        elif self.directions[1] == 'down':
            self.face = pygame.transform.rotate(self.face,90)
            #self.tail = pygame.transform.rotate(self.tail,90)
        elif self.directions[1] == 'left':
            self.face = pygame.transform.rotate(self.face,180)
            #self.tail = pygame.transform.rotate(self.tail,180)
        else:
            self.face = pygame.transform.rotate(self.face,0)
            #self.tail = pygame.transform.rotate(self.tail,0)#
        self.directions.pop(0)
        self.directions.append('right')

    def move_up(self):
        if self.directions[1] == 'down':
            self.face = pygame.transform.rotate(self.face,180)
            #self.tail = pygame.transform.rotate(self.tail,180)
        elif self.directions[1] == 'left':
            self.face = pygame.transform.rotate(self.face,-90)
            #self.tail = pygame.transform.rotate(self.tail,-90)
        elif self.directions[1] == 'right':
            self.face = pygame.transform.rotate(self.face,90)
            #self.tail = pygame.transform.rotate(self.tail,90)
        else:
            self.face = pygame.transform.rotate(self.face,0)
            #self.tail = pygame.transform.rotate(self.tail,0)
        self.directions.pop(0)
        self.directions.append('up')

    def move_down(self):
        if self.directions[1] == 'up':
            self.face = pygame.transform.rotate(self.face,180)
            #self.tail = pygame.transform.rotate(self.tail,180)
        elif self.directions[1] == 'left':
            self.face = pygame.transform.rotate(self.face,90)
            #self.tail = pygame.transform.rotate(self.tail,90)
        elif self.directions[1] == 'right':
            self.face = pygame.transform.rotate(self.face,-90)
            #self.tail = pygame.transform.rotate(self.tail,-90)
        else:
            self.face = pygame.transform.rotate(self.face,0)
            #self.tail = pygame.transform.rotate(self.tail,0)
        self.directions.pop(0)
        self.directions.append('down')

    def walk(self):
        # update body
        for i in range(self.length-1,0,-1):
        #for i in range(len(self.x)-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
            #しっぽの配列 しっぽはあきらめる！
            #if self.length > 1:
            #    self.x[-1] = self.x[-2]
            #    self.y[-1] = self.y[-2]
        #print(f'x: {self.x}')
        #print(f'y: {self.y}')
        #しっぽのポジション
        #if self.directions[1] == 'left':
        #    self.x[-1] -= CONST.SIZE
        #if self.directions[1] == 'right':
        #    self.x[-1] += CONST.SIZE
        #if self.directions[1] == 'up':
        #    self.y[-1] -= CONST.SIZE
        #if self.directions[1] == 'down':
        #    self.y[-1] += CONST.SIZE

        #if self.directions[0] == 'up' and self.directions[1] == 'left':
        #    self.y[-1] =+ CONST.SIZE
        #    self.y[self.length].append(self.y[-1])
        #elif self.directions[0] == 'up'  and self.directions[1] == 'right':
        #    self.x[self.length].append()
        #    self.y[self.length].append(self.y[-1])
        #elif self.directions[0] == 'up'  and self.directions[1] == 'down':
        #    self.x[self.length].append()
        #    self.y[self.length].append(self.y[-1])
#
        #if self.directions[0] == 'down' and self.directions[1] == 'left':
        #    self.x[self.length].append()
        #    self.y[self.length].append(self.y[-1])
        #elif self.directions[0] == 'down'  and self.directions[1] == 'right':
        #    self.x[self.length].append()
        #    self.y[self.length].append(self.y[-1])
        #elif self.directions[0] == 'down'  and self.directions[1] == 'up':
        #    self.x[self.length].append()
        #    self.y[self.length].append(self.y[-1])
#
        #if self.directions[0] == 'left' and self.directions[1] == 'right':
        #    self.x[self.length].append()
        #    self.y[self.length].append(self.y[-1])
        #elif self.directions[0] == 'left'  and self.directions[1] == 'up':
        #    self.x[self.length].append()
        #    self.y[self.length].append(self.y[-1])
        #elif self.directions[0] == 'left'  and self.directions[1] == 'down':
        #    self.x[self.length].append()
        #    self.y[self.length].append(self.y[-1])
#
        #if self.directions[0] == 'right' and self.directions[1] == 'left':
        #    self.x[self.length].append()
        #    self.y[self.length].append(self.y[-1])
        #elif self.directions[0] == 'right'  and self.directions[1] == 'up':
        #    self.x[self.length].append()
        #    self.y[self.length].append(self.y[-1])
        #elif self.directions[0] == 'right'  and self.directions[1] == 'down':
        #    self.x[self.length].append()
        #    self.y[self.length].append(self.y[-1])

        #体のポジション
        if self.directions[1] == 'left':
            self.x[0] -= CONST.SIZE
        if self.directions[1] == 'right':
            self.x[0] += CONST.SIZE
        if self.directions[1] == 'up':
            self.y[0] -= CONST.SIZE
        if self.directions[1] == 'down':
            self.y[0] += CONST.SIZE

        self.draw()

    def draw(self):
        for i in range(self.length - 1):

        #for i in range(len(self.x)-1):
            #スキンカラー変更対応
            #self.chc()
            self.parent_screen.blit(self.face, (self.x[0], self.y[0]))
            self.parent_screen.blit(self.image, (self.x[i + 1], self.y[i + 1]))
            #self.parent_screen.blit(self.tail, (self.x[-1], self.y[-1]))

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
                self.image = pygame.image.load(CONST.SNAKE_RED_IMG_PATH).convert()
                self.draw()
                pygame.display.flip()
                self.image = pygame.image.load(CONST.SNAKE_GREEN_IMG_PATH).convert()
                self.draw()
                pygame.display.flip()
                self.image = pygame.image.load(CONST.SNAKE_YELLOW_IMG_PATH).convert()
                self.draw()
                pygame.display.flip()
                cnt += 1
            self.get_gold_apple = False
            self.image = self.inibody
            pygame.display.flip()

    def had_badapple(self):

        #スキンエフェクト
        cnt = 0
        while cnt < 100:
            #bad face 表示
            if self.skincolor == 'red':
                self.face = pygame.image.load(CONST.SNAKE_RED_HAD_BAD_APPLE_FACE_IMG_PATH).convert()
            elif self.skincolor == 'green':
                self.face = pygame.image.load(CONST.SNAKE_GREEN_HAD_BAD_APPLE_FACE_IMG_PATH).convert()
            else:
                self.face = pygame.image.load(CONST.SNAKE_YELLOW_HAD_BAD_APPLE_FACE_IMG_PATH).convert()

            if self.directions[1] == 'up':
                self.face = pygame.transform.rotate(self.face,0)
            elif self.directions[1] == 'down':
                self.face = pygame.transform.rotate(self.face,180)
            elif self.directions[1] == 'right':
                self.face = pygame.transform.rotate(self.face,-90)
            else:
                self.face = pygame.transform.rotate(self.face,90)

            #スキンエフェクト 青色
            self.image = pygame.image.load(CONST.SNAKE_BLUE_IMG_PATH).convert()
            self.draw()
            pygame.display.flip()
            self.image = self.inibody
            self.draw()
            pygame.display.flip()
            cnt += 1
        self.get_gold_apple = False
        #体は青色にする
        self.image = pygame.image.load(CONST.SNAKE_BLUE_IMG_PATH).convert()
        self.face = self.iniface
        pygame.display.flip()

    def tongue(self):
        #舌を出すフェクト
        if self.out:
            if self.skincolor == 'red':
                self.face = pygame.image.load(CONST.SNAKE_RED_EATING_FACE_IMG_PATH).convert()
            elif self.skincolor == 'green':
                self.face = pygame.image.load(CONST.SNAKE_GREEN_EATING_FACE_IMG_PATH).convert()
            else:
                self.face = pygame.image.load(CONST.SNAKE_YELLOW_EATING_FACE_IMG_PATH).convert()

            if self.directions[1] == 'up':
                self.face = pygame.transform.rotate(self.face,0)
            elif self.directions[1] == 'down':
                self.face = pygame.transform.rotate(self.face,180)
            elif self.directions[1] == 'right':
                self.face = pygame.transform.rotate(self.face,-90)
            else:
                self.face = pygame.transform.rotate(self.face,90)
            #pygame.display.flip()
        else:
            self.face = self.iniface
            if self.directions[1] == 'up':
                self.face = pygame.transform.rotate(self.face,180)
            elif self.directions[1] == 'down':
                self.face = pygame.transform.rotate(self.face,0)
            elif self.directions[1] == 'right':
                self.face = pygame.transform.rotate(self.face,90)
            else:
                self.face = pygame.transform.rotate(self.face,-90)
            #pygame.display.flip()

    def speedup(self):
        #秒間speed up
        if self.scnt == 1:
            self.d = datetime.datetime.now() + datetime.timedelta(seconds=10)
