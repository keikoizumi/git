from operator import eq
from random import Random
import random
import pygame
import time
from pygame.locals import *
import AppleClass
import BadappleClass
import GoldappleClass
import SnakeClass
import ScoreClass
import const as CONST

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(CONST.CAPTION)

        pygame.mixer.init()
        self.play_background_music()
        #インスタンスの初期化
        self.surface = pygame.display.set_mode((CONST.DIP_W, CONST.DIP_H))
        self.snake = SnakeClass.Snake(self.surface)
        self.apple = AppleClass.Apple(self.surface)
        self.badapple = BadappleClass.Badapple(self.surface)
        self.goldapple = GoldappleClass.Goldapple(self.surface)
        self.score = ScoreClass.Score()

    def play_background_music(self):
        v = random.randint(1,3)
        if v == 1:
            pygame.mixer.music.load(CONST.B_MUSIC_PATH)
        elif v == 2:
            pygame.mixer.music.load(CONST.B_RAIN_PATH)
        else:
            pygame.mixer.music.load(CONST.B_SUMMER_PATH)
        pygame.mixer.music.play(-1, 0)

    def play_sound(self, sound_name):
        if sound_name == "crash":
            sound = pygame.mixer.Sound(CONST.CRASH_SOUND_PATH)
        elif sound_name == 'ding':
            sound = pygame.mixer.Sound(CONST.DING_SOUND_PATH)
        elif sound_name == 'gold':
            sound = pygame.mixer.Sound(CONST.GET_GOLD_SOUND_PATH)

        pygame.mixer.Sound.play(sound)

    #インスタンスのリセット
    def reset(self):
        self.snake = SnakeClass.Snake(self.surface)
        self.apple = AppleClass.Apple(self.surface)
        self.badapple = BadappleClass.Badapple(self.surface)
        self.goldapple = GoldappleClass.Goldapple(self.surface)
        self.score = ScoreClass.Score()

    #衝突判定
    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + CONST.SIZE:
            if y1 >= y2 and y1 < y2 + CONST.SIZE:
                #蛇が切り返したときに死なない
                if self.snake.direction != self.snake.b_direction:
                    return True
        return False

    def had_badapple(self, x1, y1):
        for i in self.badapple.badapples:
            x2 = i[0]
            y2 = i[1]
            if x1 >= x2 and x1 < x2 + CONST.SIZE:
                if y1 >= y2 and y1 < y2 + CONST.SIZE:
                    return True
        return False

    def goldapple(self):
        cnt = 1
        if cnt == 1:
            self.goldapple.mkapple()
        cnt += 1

    #背景
    def render_background(self):
        bg = pygame.image.load(CONST.B_IMG_PATH)
        self.surface.blit(bg, (0,0))

    def play(self):
        self.render_background()
        self.snake.walk()
        self.apple.draw()
        self.badapple.draw()

        #make golden apple
        if self.snake.length%10 == 0 and self.goldapple.cnt == 1:
            self.goldapple.mkapple()
            self.goldapple.cnt+=1
        self.goldapple.draw()

        # snake eating apple scenario
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.play_sound('ding')
            self.snake.increase_length()
            #すでにりんごがある場所に配置しない
            self.badapple.mkapple(self.apple.x, self.apple.y)
            self.apple.move(self.badapple.badapples)

        # snake eating gold apple
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.goldapple.x, self.goldapple.y):
            self.play_sound('gold')
            self.badapple = BadappleClass.Badapple(self.surface)
            self.goldapple = GoldappleClass.Goldapple(self.surface)
            self.goldapple.cnt = 1

        # snake eating bad apple scenario
        if self.had_badapple(self.snake.x[0], self.snake.y[0]):
            self.play_sound('crash')
            raise "Snake had a bad apple"

        # snake colliding with itself
        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.play_sound('crash')
                raise "Collision Occurred"

        # 枠を出たらUターン
        if (self.snake.x[0] + CONST.SIZE > CONST.DIP_W or self.snake.x[0] < 0
            or self.snake.y[0] + CONST.SIZE > CONST.DIP_H or self.snake.y[0] < 0):

            if self.snake.direction == 'left':
                self.snake.move_right()
            elif self.snake.direction == 'right':
                self.snake.move_left()
            elif self.snake.direction == 'up':
                self.snake.move_down()
            elif self.snake.direction == 'down':
                self.snake.move_up()

        #スコアの表示
        self.display_score()
        pygame.display.flip()

    #スコアの画面表示
    def display_score(self):
        font = pygame.font.SysFont(CONST.G_OVER_FONT,CONST.G_OVER_FONT_SIZE)
        best_score = font.render(f"Best Score: {self.score.b_score}",True,(200,200,200))
        score = font.render(f"Score: {self.snake.length}",True,(200,200,200))
        self.surface.blit(best_score,(650,10))
        self.surface.blit(score,(850,10))

    #Game Over画面
    def show_game_over(self):
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

        #結果スコア
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
                            self.snake.b_direction ='right'

                        if event.key == K_RIGHT:
                            self.snake.move_right()
                            self.snake.b_direction ='left'

                        if event.key == K_UP:
                            self.snake.move_up()
                            self.snake.b_direction ='down'

                        if event.key == K_DOWN:
                            self.snake.move_down()
                            self.snake.b_direction ='up'

                elif event.type == QUIT:
                    running = False
            try:

                if not pause:
                    self.play()

            except Exception as e:
                self.show_game_over()
                self.reset()
                self.play_background_music()
                pause = True

            time.sleep(CONST.SPEED)