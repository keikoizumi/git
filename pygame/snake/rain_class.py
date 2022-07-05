import random

#external module
import pygame

#Self-made module
import const

class Rain:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image_jpg = pygame.image.load(const.RAIN_IMG_PATH).convert()
        self.image_png = pygame.image.load(const.RAIN_IMG_PATH).convert()
        self.rains = [[0,0]]
        for i in range(25):
            self.x = i * random.randint(const.SIZE,const.SIZE * 2)
            self.y = 0
            for j in range(10):
                self.y += const.SIZE + random.randint(const.SIZE / 2,const.SIZE)
                self.rains.append([self.x, self.y])

    def draw(self):
        self.move_rain()
        for i in self.rains:
                self.x = i[0]
                self.y = i[1]
                if random.randint(1,5) % 2 == 0:
                    self.parent_screen.blit(self.image_png, (self.x, self.y))
                elif random.randint(1,5) % 2 == 1:
                    self.parent_screen.blit(self.image_jpg, (self.x, self.y))
                else:
                    pass

    def move_rain(self):
        for i in self.rains:
            if i[1] > const.DIP_H:
                i[1] = 0
            else:
                i[1] += const.SIZE

