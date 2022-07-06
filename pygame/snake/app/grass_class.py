#external module
import pygame

#Self-made module
import app.const as const

class Grass:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load(const.APPLE_IMG_PATH).convert()
        self.grass_image = pygame.image.load(const.GRASS_IMG_PATH).convert()
        self.grasss = []
        for i in range(30):
            self.grasss.append([const.SIZE * i, 0])
        #for i in range(18):
        #    self.grasss.append([0, const.SIZE * i])
        #self.x = []
        #self.y = []
        #for i in range(30):
        #    self.x += [const.SIZE * i]
        #for i in range(18):
        #    self.y += [const.SIZE * i]

    def draw(self):
        for i in self.grasss:
            self.x = i[0]
            self.y = i[1]
            #self.parent_screen.blit(self.grass_image, (self.x, self.y))
            self.parent_screen.blit(self.grass_image, (self.x, const.DIP_H - const.SIZE))
            #self.parent_screen.blit(self.grass_image, (const.DIP_W - const.SIZE, self.y))
        #for i in range(len(self.x) - 1):
        #    self.parent_screen.blit(self.grass_image, (self.x[i], 0))
        #    self.parent_screen.blit(self.grass_image, (self.x[i], const.DIP_H - const.SIZE))
        #for i in range(len(self.y) - 1):
        #    self.parent_screen.blit(self.grass_image, (0, self.y[i]))
        #    self.parent_screen.blit(self.grass_image, (const.DIP_W - const.SIZE, self.y[i]))
