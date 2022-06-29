import pygame
import CONST

class  GameOver:
    def show(self, parent_screen):
        self.score.write(self.snake.length)
        self.render_background()

        font = pygame.font.SysFont(CONST.G_OVER_FONT, CONST.G_OVER_FONT_SIZE)

        #NEW RECORD達成時
        if int(self.score.b_score) < int(self.score.n_score):
            line0 = font.render(CONST.G_BEST , True, (255, 255, 255))
            self.surface.blit(line0, (CONST.DIP_W/4, CONST.DIP_H/3 - 20,))
            self.score.write(self.score.n_score)
        else:
            self.score.write(self.score.b_score)