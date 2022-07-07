import app.const as const

#external module
import pygame

class Life:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.life_image = pygame.image.load(const.LIFE_IMG_PATH).convert()
        self.life = [
                    const.SIZE * 10
                    ,const.SIZE * 10 + const.SIZE
                    ,const.SIZE * 10 + const.SIZE * 2
                    ]
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
            print(self.life)
        self.draw()

    def death_check(self):
        if len(self.life) == 0:
            return True
        return False

    def draw(self):
        for i in self.life:
                self.x = i
                self.parent_screen.blit(self.life_image, (self.x, 0))