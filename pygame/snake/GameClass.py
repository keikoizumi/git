from pickle import FALSE
import random
from telnetlib import COM_PORT_OPTION
import pygame
import time
import datetime
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
        #取得した体
        self.max = 1
        #死因
        self.causeofdeath = 'unknown'

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
        if (x1 >= x2 and x1 < x2 + CONST.SIZE) or (x1 + CONST.SIZE >= x2 and x1 + CONST.SIZE < x2 + CONST.SIZE):
            if (y1 >= y2 and y1 < y2 + CONST.SIZE) or (y1 + CONST.SIZE >= y2 and y1 + CONST.SIZE < y2 + CONST.SIZE):
                #蛇が切り返したときに死なない
                if ((self.snake.directions[0] == 'up' and self.snake.directions[1] == 'down')
                    or (self.snake.directions[0] == 'down' and self.snake.directions[1] == 'up')
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

    #fast move
    def fastmove(self):
        CONST.SPEED = CONST.FAST_SPEED

    def play(self):
        print(f"x: {self.snake.x[0]}")
        print(f"y: {self.snake.y[0]}")
        print(self.snake.directions)
        #背景の描画
        self.render_background()

        self.snake.walk()
        self.apple.draw()
        self.badapple.draw()

        #舌を出す・出さない
        if self.snake.out:
            self.snake.out = False
            self.snake.tongue()
        else:
            self.snake.out = True
            self.snake.tongue()

        #golden appleを作る
        if ((self.snake.length%10 == 0 and self.goldapple.cnt == 1) and self.badapple.cnt >= 10):
            self.goldapple.mkapple()
            self.goldapple.cnt+=1
            self.play_background_music()
        self.goldapple.draw()

        # 蛇がりんごを食べた！
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.play_sound('ding')
            #体を減らす
            self.snake.increase_length()
            #すでにりんごがある場所に配置しない
            for i in range(random.randint(1,2)):
                self.badapple.mkapple(self.apple.x, self.apple.y)
            #for i in range(random.randint(1,2)):
            self.apple.move(self.badapple.badapples)

        # 蛇がgold appleを食べた！
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.goldapple.x, self.goldapple.y):
            self.play_sound('gold')
            #self.badapple = BadappleClass.Badapple(self.surface)
            self.badapple.delapples(10)
            self.goldapple = GoldappleClass.Goldapple(self.surface)
            self.goldapple.cnt = 1
            self.snake.get_gold_apple = True
            self.snake.chcg()

        # 蛇がbad appleを食べた！
        if self.had_badapple(self.snake.x[0], self.snake.y[0]):
            self.play_sound('bad')
            self.snake.had_badapple()
            self.badapple.delapples(1)
            #体の数を減らす
            self.snake.decrease_length()
            self.snake.scnt = 1
            self.snake.speedup()
            if self.snake.length == 1:
                self.causeofdeath = 'bad apple'
                print("Snake had too many bad apples and R.I.P")
                raise "Snake had too many bad apples and R.I.P"

        # 蛇が自分自身にぶつかった！
        #for i in range(5, self.snake.length):
        #    if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
        #        self.play_sound('crash')
        #        self.causeofdeath = 'Collision'
        #        print("Collision Occurred")
        #        raise "Collision Occurred"

        # 枠を出たらUターン
        if ((self.snake.x[0] + CONST.SIZE > CONST.DIP_W) or (self.snake.x[0] < 0)
            or (self.snake.y[0] + CONST.SIZE > CONST.DIP_H) or (self.snake.y[0] < 0)):

            #画面超えたら軸を初期化
            if self.snake.x[0] >= CONST.DIP_W:
                self.snake.x[0] = CONST.DIP_W - CONST.SIZE
            if self.snake.x[0] < 0:
                self.snake.x[0] = 0
            if self.snake.y[0] >= CONST.DIP_H:
                self.snake.y[0] = CONST.DIP_H - CONST.SIZE
            if self.snake.y[0] < 0:
                self.snake.y[0] = 0

            #一つ前の方向と反対方向へすすめ
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

        #SPEED PANIC 確認
        if self.snake.scnt == 1:
            if datetime.datetime.now() < self.snake.d:
                #スピードのパラメータ変更
                CONST.SPEED = CONST.PANIC_SPEED
                #顔色を変える
                #お顔を整える
                self.snake.face = pygame.image.load(CONST.SNAKE_BLUE_HAD_BAD_APPLE_FACE_IMG_PATH).convert()
                if self.snake.directions[1] == 'up':
                    self.snake.face = pygame.transform.rotate(self.snake.face,0)
                elif self.snake.directions[1] == 'down':
                    self.snake.face = pygame.transform.rotate(self.snake.face,180)
                elif self.snake.directions[1] == 'right':
                    self.snake.face = pygame.transform.rotate(self.snake.face,-90)
                else:
                    self.snake.face = pygame.transform.rotate(self.snake.face,90)

                #スキンエフェクト 青色
                self.snake.paniccnt += 1
                if self.snake.paniccnt%2 == 0:
                    self.snake.image = pygame.image.load(CONST.SNAKE_BLUE_IMG_PATH).convert()
                    self.snake.draw()
                    pygame.display.flip()
                else:
                    self.snake.image = self.snake.inibody
                    self.snake.draw()
                    pygame.display.flip()
            else:
                #お体をもとに戻す
                self.snake.image = self.snake.inibody
                #お顔をもとに戻す
                self.snake.face = self.snake.iniface
                if self.snake.directions[1] == 'up':
                    self.snake.face = pygame.transform.rotate(self.snake.face,180)
                elif self.snake.directions[1] == 'down':
                    self.snake.face = pygame.transform.rotate(self.snake.face,0)
                elif self.snake.directions[1] == 'right':
                    self.snake.face = pygame.transform.rotate(self.snake.face,90)
                else:
                    self.snake.face = pygame.transform.rotate(self.snake.face,-90)
                self.snake.scnt = 0
                #スピードをもとに戻す
                CONST.SPEED = CONST.NORMAL_SPEED

        #最大長を保持
        if self.max <= self.snake.length:
            self.max = self.snake.length

        #画面の更新
        pygame.display.flip()

    #スコアの画面表示
    def display_score(self):
        font = pygame.font.SysFont(CONST.G_OVER_FONT,CONST.G_OVER_FONT_SIZE)

        if CONST.SPEED == CONST.NORMAL_SPEED:
            speed = font.render("speed: normal",True,(200,200,200))
        elif CONST.SPEED == CONST.FAST_SPEED:
            speed = font.render("speed: fast",True,(200,200,200))
        else:
            speed = font.render("speed: panic",True,(200,200,200))
        count_bad = font.render(f"number of bad apples: {self.badapple.cnt}",True,(200,200,200))
        score = font.render(f"body length: {self.snake.length}",True,(200,200,200))
        best_score = font.render(f"best record: {self.score.b_score}",True,(200,200,200))

        self.surface.blit(speed,(30,10))
        self.surface.blit(count_bad,(180,10))
        self.surface.blit(score,(420,10))
        self.surface.blit(best_score,(570,10))

    #Game Over画面
    def show_game_over(self):
        #スコアをファイルに書込む
        self.score.write(self.max)
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
        line1 = font.render(f'{CONST.G_OVER + str(self.max)}.', True, (255, 255, 255))
        self.surface.blit(line1, (CONST.DIP_W/4, CONST.DIP_H/2 - 20,))

        line2 = font.render(CONST.G_OVER_OP , True, (255, 255, 255))
        self.surface.blit(line2, (CONST.DIP_W/4, CONST.DIP_H/2 + 40))

        if self.causeofdeath == 'bad apple':
            line3 = font.render(f'Cause of death: {CONST.G_OVER_CAUSE_BAD_APPLE}' , True, (255, 255, 255))
        elif self.causeofdeath == 'Collision':
            line3 = font.render(f'Cause of death: {CONST.G_OVER_CAUSE_COLLISION}' , True, (255, 255, 255))
        else:
            line3 = font.render(f'Cause of death: {CONST.G_OVER_UNKNOWN}' , True, (255, 255, 255))

        self.surface.blit(line3, (CONST.DIP_W/4, CONST.DIP_H/2 + 10))

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

                        if event.key == K_RCTRL or event.key == K_LCTRL :

                            if self.snake.fastmove:
                                self.snake.fastmove = False
                                self.fastmove()
                            else:
                                self.snake.fastmove = True
                                CONST.SPEED = CONST.NORMAL_SPEED

                elif event.type == QUIT:
                    running = False
            try:

                if not pause:
                    self.play()

            except Exception as e:
                self.show_game_over()
                self.reset()
                pause = True
                CONST.SPEED = CONST.NORMAL_SPEED
            print(CONST.SPEED)
            time.sleep(CONST.SPEED)