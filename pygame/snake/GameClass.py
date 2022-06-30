import random
import pygame
import time
from pygame.locals import *
import AppleClass
import BadappleClass
import GoldappleClass
import SnakeClass
import ScoreClass
import CONST

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
        if CONST.SOUND:
            m = random.randint(1,3)
            if m == 1:
                pygame.mixer.music.load(CONST.B_MUSIC_PATH)
            elif m == 2:
                pygame.mixer.music.load(CONST.B_RAIN_PATH)
            else:
                pygame.mixer.music.load(CONST.B_SUMMER_PATH)
            pygame.mixer.music.play(-1, 0)

    def play_sound(self, sound_name):
        if CONST.SOUND:
            if sound_name == "crash":
                sound = pygame.mixer.Sound(CONST.CRASH_SOUND_PATH)
            elif sound_name == 'ding':
                sound = pygame.mixer.Sound(CONST.DING_SOUND_PATH)
            elif sound_name == 'gold':
                sound = pygame.mixer.Sound(CONST.GET_GOLD_SOUND_PATH)
            elif sound_name == 'bad':
                sound = pygame.mixer.Sound(CONST.GET_BAD_SOUND_PATH)

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
        if x1 + CONST.SIZE/2 >= x2 and x1 < x2 + CONST.SIZE:
            if y1 + CONST.SIZE/2 >= y2 and y1 < y2 + CONST.SIZE:
                #蛇が切り返したときに死なない
                if (((self.snake.directions[0] == 'up' and self.snake.directions[1] == 'down')
                    or (self.snake.directions[0] == 'down' and self.snake.directions[1] == 'up'))
                    or (self.snake.directions[0] == 'left' and self.snake.directions[1] == 'right')
                    or (self.snake.directions[0] == 'right' and self.snake.directions[1] == 'left')):
                    return False
                else:
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

    #背景
    def render_background(self):
        bg = pygame.image.load(CONST.B_IMG_PATH)
        self.surface.blit(bg, (0,0))

    def play(self):

        self.render_background()
        self.snake.walk()
        self.apple.draw()
        self.badapple.draw()

        #golden appleを作る
        if self.snake.length%10 == 0 and self.goldapple.cnt == 1:
            self.goldapple.mkapple()
            self.goldapple.cnt+=1
            self.play_background_music()
        self.goldapple.draw()

        # 蛇がりんごを食べた！
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.play_sound('ding')
            self.snake.increase_length()
            #すでにりんごがある場所に配置しない
            self.badapple.mkapple(self.apple.x, self.apple.y)
            self.apple.move(self.badapple.badapples)

        # 蛇がgold appleを食べた！
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.goldapple.x, self.goldapple.y):
            self.play_sound('gold')
            self.badapple = BadappleClass.Badapple(self.surface)
            self.goldapple = GoldappleClass.Goldapple(self.surface)
            self.goldapple.cnt = 1
            self.snake.get_gold_apple = True
            self.snake.chcg()

        # 蛇がbad appleを食べた！
        if self.had_badapple(self.snake.x[0], self.snake.y[0]):
            self.play_sound('bad')
            self.snake.had_badapple()
            if self.snake.length == 1:
                raise "Snake had too many bad apples and R.I.P"

        # 蛇が自分自身にぶつかった！
        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.play_sound('crash')
                raise "Collision Occurred"

        # 枠を出たらUターン
        if (self.snake.x[0] + CONST.SIZE > CONST.DIP_W or self.snake.x[0] < 0
            or self.snake.y[0] + CONST.SIZE > CONST.DIP_H or self.snake.y[0] < 0):

            if self.snake.directions[-1] == 'left':
                self.snake.move_right()
            elif self.snake.directions[-1] == 'right':
                self.snake.move_left()
            elif self.snake.directions[-1] == 'up':
                self.snake.move_down()
            elif self.snake.directions[-1] == 'down':
                self.snake.move_up()

        #スコアの表示
        self.display_score()

        pygame.display.flip()

    #スコアの画面表示
    def display_score(self):
        font = pygame.font.SysFont(CONST.G_OVER_FONT,CONST.G_OVER_FONT_SIZE)
        best_score = font.render(f"Best Score: {self.score.b_score}",True,(200,200,200))
        score = font.render(f"Score: {self.snake.length}",True,(200,200,200))
        self.surface.blit(best_score,(CONST.DIP_W - CONST.DIP_W/3,10))
        self.surface.blit(score,(CONST.DIP_W - CONST.DIP_W/7,10))

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
                        self.play_background_music()

                    if event.key == K_SPACE:
                        if pause == True:
                            pause = False
                            pygame.mixer.music.unpause()
                        else:
                            pause = True
                            pygame.mixer.music.pause()

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