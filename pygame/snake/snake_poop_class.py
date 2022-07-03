#external module
import pygame

#Self-made module
import const

class Poop:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load(const.SNAKE_POOP_IMG_PATH).convert()
        self.x = -100
        self.y = -100

    def make_poop(self, apple_x, apple_y, snake_x, snake_y):
        print(f'snake_x {snake_x}')
        print(f'snake_y {snake_y}')

        self.apple_x = apple_x
        self.apple_y = apple_y
        try:
            self.x = snake_x[-3]
            self.y = snake_y[-3]
        except IndexError as e:
            self.x = snake_x[-1]
            self.y = snake_y[-1]

    #描画
    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))