#external module
import pygame

#Self-made module
import const

class Cicada:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image_cicada = pygame.image.load(const.CICADA_IMG_PATH).convert()
        self.cicada = [[20, 300]]

    def draw(self):
        for i in self.cicada:
            self.x = i[0]
            self.y = i[1]
            self.parent_screen.blit(self.image_cicada, (self.x, self.y))
