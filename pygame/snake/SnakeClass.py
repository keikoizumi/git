from tkinter import W
import pygame
import CONST

class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load(CONST.SNAKE_YELLOW_IMG_PATH).convert()
        self.face = pygame.image.load(CONST.SNAKE_YELLOW_FACE_IMG_PATH).convert()
        self.direction = 'down'
        self.b_direction = 'down'

        self.length = 1
        self.x = [CONST.SIZE]
        self.y = [CONST.SIZE]

        self.draw()

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):
        # update body
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direction == 'left':
            self.x[0] -= CONST.SIZE
        if self.direction == 'right':
            self.x[0] += CONST.SIZE
        if self.direction == 'up':
            self.y[0] -= CONST.SIZE
        if self.direction == 'down':
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
        elif self.length >= 30:
            self.image = pygame.image.load(CONST.SNAKE_GREEN_IMG_PATH)
            self.face = pygame.image.load(CONST.SNAKE_GREEN_FACE_IMG_PATH)
