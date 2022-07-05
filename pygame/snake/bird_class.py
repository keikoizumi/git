#Standard module
import random

#external module
import pygame

#Self-made module
import const

class Bird:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load(const.BIRD_IMG_PATH).convert()
        self.x = -100
        self.y = -100
        self.is_bird = False

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))

    def make_bird(self):
        #鳥の新しい座標
        self.is_bird = True
        self.x = abs(random.randint(30, 400))
        self.y = abs(random.randint(50, 200))
