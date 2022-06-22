import pygame
import time
from pygame.locals import *
import AppleClass
import BadappleClass
import SnakeClass
import const as CONST

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(CONST.CAPTION)

        pygame.mixer.init()
        self.play_background_music()

        self.surface = pygame.display.set_mode((CONST.DIP_W, CONST.DIP_H))
        self.snake = SnakeClass.Snake(self.surface)
        self.apple = AppleClass.Apple(self.surface)
        self.badapple = BadappleClass.Badapple(self.surface)

    def play_background_music(self):
        pygame.mixer.music.load(CONST.B_MUSIC_PATH)
        pygame.mixer.music.play(-1, 0)

    def play_sound(self, sound_name):
        if sound_name == "crash":
            sound = pygame.mixer.Sound(CONST.CRASH_SOUND_PATH)
        elif sound_name == 'ding':
            sound = pygame.mixer.Sound(CONST.DING_SOUND_PATH)

        pygame.mixer.Sound.play(sound)

    def reset(self):
        self.snake = SnakeClass.Snake(self.surface)
        self.apple = AppleClass.Apple(self.surface)
        self.badapple = BadappleClass.Badapple(self.surface)

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + CONST.SIZE:
            if y1 >= y2 and y1 < y2 + CONST.SIZE:
                return True
        return False

    def render_background(self):
        bg = pygame.image.load(CONST.B_IMG_PATH)
        self.surface.blit(bg, (0,0))

    def play(self):
        self.render_background()

        self.snake.walk()
        self.apple.draw()
        self.badapple.draw()
        self.display_score()
        pygame.display.flip()

        # snake eating apple scenario
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.play_sound("ding")
            self.snake.increase_length()
            self.apple.move()
            self.badapple.move()

        # snake eating bad apple scenario
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.badapple.x, self.badapple.y):
            self.play_sound('crash')
            raise "Snake had a bad apple"

        # snake colliding with itself
        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.play_sound('crash')
                raise "Collision Occurred"

        # 枠を出たらUターン
        if (self.snake.x[0] >= CONST.DIP_W or self.snake.x[0] < 0
            or self.snake.y[0] >= CONST.DIP_H or self.snake.y[0] < 0):

            if self.snake.direction == 'left':
                self.snake.move_right()
            elif self.snake.direction == 'right':
                self.snake.move_left()
            elif self.snake.direction == 'up':
                self.snake.move_down()
            elif self.snake.direction == 'down':
                self.snake.move_up()

    def display_score(self):
        font = pygame.font.SysFont(CONST.G_OVER_FONT,CONST.G_OVER_FONT_SIZE)
        score = font.render(f"Score: {self.snake.length}",True,(200,200,200))
        self.surface.blit(score,(850,10))

    def show_game_over(self):
        self.render_background()
        font = pygame.font.SysFont(CONST.G_OVER_FONT, CONST.G_OVER_FONT_SIZE)
        line1 = font.render(CONST.G_OVER + str(self.snake.length), True, (255, 255, 255))
        self.surface.blit(line1, (CONST.DIP_W/4, CONST.DIP_H/2 - 20,))
        line2 = font.render(CONST.G_OVER_OP , True, (255, 255, 255))
        self.surface.blit(line2, (CONST.DIP_W/4, CONST.DIP_H/2 + 10))
        pygame.mixer.music.pause()
        pygame.display.flip()

    def run(self):
        running = True
        pause = False

        while running:

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        pause = False

                    if not pause:
                        if event.key == K_LEFT:
                            self.snake.move_left()

                        if event.key == K_RIGHT:
                            self.snake.move_right()

                        if event.key == K_UP:
                            self.snake.move_up()

                        if event.key == K_DOWN:
                            self.snake.move_down()

                elif event.type == QUIT:
                    running = False
            try:

                if not pause:
                    self.play()

            except Exception as e:
                self.show_game_over()
                self.reset()
                pause = True

            time.sleep(CONST.SPEED)