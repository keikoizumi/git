#external module
import pygame

#Self-made module
import app.const as const

class Cicada:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image_cicada = pygame.image.load(const.CICADA_IMG_PATH).convert()
        self.x = -100
        self.y = -100
        self.is_cicada = False

    def draw(self):
        self.parent_screen.blit(self.image_cicada, (self.x, self.y))

    def make_cicada(self):
        self.x = 20
        self.y = 300
        self.draw()
        self.is_cicada = True
