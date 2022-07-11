import app.const as const

#external module
import pygame

class Life:
    def __init__(self, parent_screen, y):
        self.parent_screen = parent_screen
        self.life_image = pygame.image.load(const.LIFE_IMG_PATH).convert()
        self.life = [
                    const.DIP_W - const.SIZE * 4
                    ,const.DIP_W - const.SIZE * 3
                    , const.DIP_W - const.SIZE * 2
        ]
        self.y = y
        self.draw()

    def add(self):
        if len(self.life) < const.MAX_LIFE:
            ll = self.life[-1]
            ll += const.SIZE
            #if len(self.life) == 1:
            #    self.life[1] = 440
            #elif len(self.life) == 2:
            #    self.life[2] = 480
            self.life = ll
        self.draw()

    def remove(self):
        if len(self.life) > 0:
            del self.life[-1]
        self.draw()

    def death_check(self):
        if len(self.life) == 0:
            return True
        return False

    def draw(self):
        for i in self.life:
                self.x = i
                self.parent_screen.blit(self.life_image, (self.x, self.y))