from tkinter import W
from numpy import append
import pygame
import CONST

class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load(CONST.SNAKE_YELLOW_IMG_PATH).convert()
        self.face = pygame.image.load(CONST.SNAKE_YELLOW_FACE_IMG_PATH).convert()
        self.face = pygame.transform.rotate(self.face,180)
        #self.direction = 'down'
        self.directions = ['down','down']

        self.length = 1
        self.x = [CONST.SIZE]
        self.y = [CONST.SIZE]

        self.draw()

    def move_left(self):
        #お顔の向きを整える
        if self.directions[-1] == 'up':
            self.face = pygame.transform.rotate(self.face,90)
        elif self.directions[-1] == 'down':
            self.face = pygame.transform.rotate(self.face,-90)
        elif self.directions[-1] == 'right':
            self.face = pygame.transform.rotate(self.face,180)
        else:
            self.face = pygame.transform.rotate(self.face,0)

        self.directions.pop(0)
        self.directions.append('left')

    def move_right(self):
        if self.directions[-1] == 'up':
            self.face = pygame.transform.rotate(self.face,-90)
        elif self.directions[-1] == 'down':
            self.face = pygame.transform.rotate(self.face,90)
        elif self.directions[-1] == 'left':
            self.face = pygame.transform.rotate(self.face,180)
        else:
            self.face = pygame.transform.rotate(self.face,0)

        self.directions.pop(0)
        self.directions.append('right')

    def move_up(self):
        if self.directions[-1] == 'down':
            self.face = pygame.transform.rotate(self.face,180)
        elif self.directions[-1] == 'left':
            self.face = pygame.transform.rotate(self.face,-90)
        elif self.directions[-1] == 'right':
            self.face = pygame.transform.rotate(self.face,90)
        else:
            self.face = pygame.transform.rotate(self.face,0)

        self.directions.pop(0)
        self.directions.append('up')

    def move_down(self):
        if self.directions[-1] == 'up':
            self.face = pygame.transform.rotate(self.face,180)
        elif self.directions[-1] == 'left':
            self.face = pygame.transform.rotate(self.face,90)
        elif self.directions[-1] == 'right':
            self.face = pygame.transform.rotate(self.face,-90)
        else:
            self.face = pygame.transform.rotate(self.face,0)

        self.directions.pop(0)
        self.directions.append('down')

    def walk(self):
        # update body
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.directions[-1] == 'left':
            self.x[0] -= CONST.SIZE
        if self.directions[-1] == 'right':
            self.x[0] += CONST.SIZE
        if self.directions[-1] == 'up':
            self.y[0] -= CONST.SIZE
        if self.directions[-1] == 'down':
            self.y[0] += CONST.SIZE

        self.draw()

    def draw(self):
        for i in range(self.length - 1):
            #スキンカラー変更対応
            self.chc()
            self.parent_screen.blit(self.face, (self.x[0], self.y[0]))
            self.parent_screen.blit(self.image, (self.x[i + 1], self.y[i + 1]))
        pygame.display.flip()

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    #スキンカラーの変更
    def chc(self):
        if self.length >= 20:
            self.image = pygame.image.load(CONST.SNAKE_RED_IMG_PATH)
            self.face = pygame.image.load(CONST.SNAKE_RED_FACE_IMG_PATH)
            self.face = pygame.transform.rotate(self.face,180)
        elif self.length >= 30:
            self.image = pygame.image.load(CONST.SNAKE_GREEN_IMG_PATH)
            self.face = pygame.image.load(CONST.SNAKE_GREEN_FACE_IMG_PATH)
            self.face = pygame.transform.rotate(self.face,180)
