#external module
import pygame

#Self-made module
import const

class Poop:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load(const.SNAKE_POOP_IMG_PATH).convert()
        self.poop_x = -100
        self.poop_y = -100

    def make_poop(self, snake_x, snake_y):
        for i in range(len(snake_x) -1 , 0, -1):
            if snake_x[i] != -1:
                self.poop_x = snake_x[i]
                self.poop_y = snake_y[i]
                break
        self.draw()

    #描画
    def draw(self):
        self.parent_screen.blit(self.image, (self.poop_x, self.poop_y))