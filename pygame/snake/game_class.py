#Standard module
import datetime
import pygame
import random
import time
import traceback

#external module
from pygame.locals import *

#Self-made module
import apple_class
import bad_apple_class
import const
import gold_apple_class
import snake_class
import score_class


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(const.CAPTION)

        pygame.mixer.init()
        self.play_background_music()
        #インスタンスの初期化
        self.surface = pygame.display.set_mode((const.DIP_W, const.DIP_H))
        self.snake = snake_class.Snake(self.surface)
        self.apple = apple_class.Apple(self.surface)
        self.bad_apple = bad_apple_class.BadApple(self.surface)
        self.gold_apple = gold_apple_class.GoldApple(self.surface)
        self.score = score_class.Score()
        #取得した体
        self.max = 1
        #死因
        self.cause_of_death = 'unknown'

    def play_background_music(self):
        if const.SOUND:
            m = random.randint(1, 3)
            if m == 1:
                pygame.mixer.music.load(const.B_MUSIC_PATH)
            elif m == 2:
                pygame.mixer.music.load(const.B_RAIN_PATH)
            else:
                pygame.mixer.music.load(const.B_SUMMER_PATH)
            pygame.mixer.music.play(-1, 0)

    def play_sound(self, sound_name):
        if const.SOUND:
            if sound_name == 'crash':
                sound = pygame.mixer.Sound(const.CRASH_SOUND_PATH)
            elif sound_name == 'ding':
                sound = pygame.mixer.Sound(const.DING_SOUND_PATH)
            elif sound_name == 'gold':
                sound = pygame.mixer.Sound(const.GET_GOLD_SOUND_PATH)
            elif sound_name == 'bad':
                sound = pygame.mixer.Sound(const.GET_BAD_SOUND_PATH)
            pygame.mixer.Sound.play(sound)

    #インスタンスのリセット
    def reset(self):
        self.snake = snake_class.Snake(self.surface)
        self.apple = apple_class.Apple(self.surface)
        self.bad_apple = bad_apple_class.BadApple(self.surface)
        self.gold_apple = gold_apple_class.GoldApple(self.surface)
        self.score = score_class.Score()

    #衝突判定
    def is_collision(self, x1, y1, x2, y2):
        if (x1 >= x2 and x1 < x2 + const.SIZE) or (x1 + const.SIZE >= x2 and x1 + const.SIZE < x2 + const.SIZE):
            if (y1 >= y2 and y1 < y2 + const.SIZE) or (y1 + const.SIZE >= y2 and y1 + const.SIZE < y2 + const.SIZE):
                #蛇が切り返したときに死なない
                #if ((self.snake.directions[0] == 'up' and self.snake.directions[1] == 'down')
                #    or (self.snake.directions[0] == 'down' and self.snake.directions[1] == 'up')
                #    or (self.snake.directions[0] == 'left' and self.snake.directions[1] == 'right')
                #    or (self.snake.directions[0] == 'right' and self.snake.directions[1] == 'left')):
                #    return False
                #else:
                    return True
        return False

    def had_bad_apple(self, x1, y1):
        for i in self.bad_apple.bad_apples:
            x2 = i[0]
            y2 = i[1]
            if x1 >= x2 and x1 < x2 + const.SIZE:
                if y1 >= y2 and y1 < y2 + const.SIZE:
                    return True
        return False
    #背景
    def render_background(self):
        bg = pygame.image.load(const.B_IMG_PATH)
        self.surface.blit(bg, (0, 0))
    #fast move
    def fast_move(self):
        const.SPEED = const.FAST_SPEED

    def play(self):
        #背景の描画
        self.render_background()
        self.snake.walk()
        self.apple.draw()
        self.bad_apple.draw()
        #舌を出す・出さない
        if self.snake.out:
            self.snake.out = False
            self.snake.tongue()
        else:
            self.snake.out = True
            self.snake.tongue()
        #golden appleを作る
        if ((self.snake.length%10 == 0 and self.gold_apple.cnt == 1) and self.bad_apple.cnt >= 10):
            self.gold_apple.mkapple()
            self.gold_apple.cnt+=1
            self.play_background_music()
        self.gold_apple.draw()
        # 蛇がりんごを食べた！
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.play_sound('ding')
            #体を減らす
            self.snake.increase_length()
            #すでにりんごがある場所に配置しない
            for i in range(random.randint(1, 2)):
                self.bad_apple.mkapple(self.apple.x, self.apple.y)
            #for i in range(random.randint(1,2)):
            self.apple.move(self.bad_apple.bad_apples)
        # 蛇がgold appleを食べた！
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.gold_apple.x, self.gold_apple.y):
            self.play_sound('gold')
            self.bad_apple.del_apples(10)
            self.gold_apple = gold_apple_class.GoldApple(self.surface)
            self.gold_apple.cnt = 1
            self.snake.get_gold_apple = True
            self.snake.chcg()
        # 蛇がbad appleを食べた！
        if self.had_bad_apple(self.snake.x[0], self.snake.y[0]):
            self.play_sound('bad')
            self.snake.had_bad_apple()
            self.bad_apple.del_apples(1)
            #体の数を減らす
            self.snake.decrease_length()
            self.snake.s_cnt = 1
            self.snake.speedup()
            if self.snake.length == 1:
                self.cause_of_death = 'bad apple'
                print('Snake had too many bad apples and R.I.P')
                raise 'Snake had too many bad apples and R.I.P'
        # 蛇が自分自身にぶつかった！
        #for i in range(5, self.snake.length):
        #    if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
        #        self.play_sound('crash')
        #        self.cause_of_death = 'Collision'
        #        print('Collision Occurred')
        #        raise 'Collision Occurred'
        # 枠を出たらUターン
        if ((self.snake.x[0] + const.SIZE > const.DIP_W) or (self.snake.x[0] < 0)
            or (self.snake.y[0] + const.SIZE > const.DIP_H) or (self.snake.y[0] < 0)):
            #画面超えたら軸を初期化
            if self.snake.x[0] >= const.DIP_W:
                self.snake.x[0] = const.DIP_W - const.SIZE
            if self.snake.x[0] < 0:
                self.snake.x[0] = 0
            if self.snake.y[0] >= const.DIP_H:
                self.snake.y[0] = const.DIP_H - const.SIZE
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
        if self.snake.s_cnt == 1:
            if datetime.datetime.now() < self.snake.d:
                #スピードのパラメータ変更
                const.SPEED = const.PANIC_SPEED
                #顔色を変える
                #お顔を整える
                self.snake.face = pygame.image.load(const.SNAKE_BLUE_HAD_BAD_APPLE_FACE_IMG_PATH).convert()
                if self.snake.directions[1] == 'up':
                    self.snake.face = pygame.transform.rotate(self.snake.face, 0)
                elif self.snake.directions[1] == 'down':
                    self.snake.face = pygame.transform.rotate(self.snake.face, 180)
                elif self.snake.directions[1] == 'right':
                    self.snake.face = pygame.transform.rotate(self.snake.face, -90)
                else:
                    self.snake.face = pygame.transform.rotate(self.snake.face, 90)
                #スキンエフェクト 青色
                self.snake.panic_cnt += 1
                if self.snake.panic_cnt % 2 == 0:
                    self.snake.image = pygame.image.load(const.SNAKE_BLUE_IMG_PATH).convert()
                    self.snake.draw()
                    pygame.display.flip()
                else:
                    self.snake.image = self.snake.init_body
                    self.snake.draw()
                    pygame.display.flip()
            else:
                #お体をもとに戻す
                self.snake.image = self.snake.init_body
                #お顔をもとに戻す
                self.snake.face = self.snake.init_face
                if self.snake.directions[1] == 'up':
                    self.snake.face = pygame.transform.rotate(self.snake.face, 180)
                elif self.snake.directions[1] == 'down':
                    self.snake.face = pygame.transform.rotate(self.snake.face, 0)
                elif self.snake.directions[1] == 'right':
                    self.snake.face = pygame.transform.rotate(self.snake.face, 90)
                else:
                    self.snake.face = pygame.transform.rotate(self.snake.face, -90)
                self.snake.s_cnt = 0
                #スピードをもとに戻す
                const.SPEED = const.NORMAL_SPEED
        #最大長を保持
        if self.max <= self.snake.length:
            self.max = self.snake.length
        #画面の更新
        pygame.display.flip()

    #スコアの画面表示
    def display_score(self):
        font = pygame.font.SysFont(const.G_OVER_FONT,const.G_OVER_FONT_SIZE)
        if const.SPEED == const.NORMAL_SPEED:
            speed = font.render('speed: normal', True, const.WHITE)
        elif const.SPEED == const.FAST_SPEED:
            speed = font.render('speed: fast', True, const.WHITE)
        else:
            speed = font.render('speed: panic', True, const.WHITE)
        count_bad = font.render(f'number of bad apples: {self.bad_apple.cnt}', True, const.WHITE)
        score = font.render(f'body length: {self.snake.length}', True, const.GOLD) #黄色
        best_score = font.render(f'best record: {self.score.b_score}', True, const.WHITE)
        self.surface.blit(speed, (30, 10))
        self.surface.blit(count_bad,(180, 10))
        self.surface.blit(score, (420, 10))
        self.surface.blit(best_score, (570, 10))

    #Game Over画面
    def show_game_over(self):
        #スコアをファイルに書込む
        self.score.write(self.max)
        self.render_background()
        font = pygame.font.SysFont(const.G_OVER_FONT, const.G_OVER_FONT_SIZE)
        #NEW RECORD達成時
        try:
            if int(self.score.b_score) < int(self.score.n_score):
                pass
        except ValueError as e:
                line0 = font.render('invalid score' , True, const.GOLD)
                self.surface.blit(line0, (const.DIP_W/4, const.DIP_H/3 - 20))
                self.score.write('1')
                print(f'不正なスコアを発見しました: {e}')
        else:
            if int(self.score.b_score) < int(self.score.n_score):
                line0 = font.render(const.G_BEST , True, const.GOLD)
                self.surface.blit(line0, (const.DIP_W/4, const.DIP_H/3 - 20))
                self.score.write(self.score.n_score)
            else:
                self.score.write(self.score.b_score)
        #結果スコア
        line1 = font.render(f'{const.G_OVER + str(self.max)}.', True, const.WHITE)
        self.surface.blit(line1, (const.DIP_W / 4, const.DIP_H / 2 - 20))
        line2 = font.render(const.G_OVER_OP , True, const.WHITE)
        self.surface.blit(line2, (const.DIP_W / 4, const.DIP_H / 2 + 40))
        if self.cause_of_death == 'bad apple':
            line3 = font.render(f'Cause of death: {const.G_OVER_CAUSE_BAD_APPLE}' , True, const.WHITE)
        elif self.cause_of_death == 'Collision':
            line3 = font.render(f'Cause of death: {const.G_OVER_CAUSE_COLLISION}' , True, const.WHITE)
        else:
            line3 = font.render(f'Cause of death: {const.G_OVER_UNKNOWN}' , True, const.WHITE)
        self.surface.blit(line3, (const.DIP_W / 4, const.DIP_H / 2 + 10))
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
                        if event.key == K_RCTRL or event.key == K_LCTRL:
                            if self.snake.fast_move:
                                self.snake.fast_move = False
                                self.fast_move()
                            else:
                                self.snake.fast_move = True
                                const.SPEED = const.NORMAL_SPEED
                elif event.type == QUIT:
                    running = False
            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                self.reset()
                pause = True
                const.SPEED = const.NORMAL_SPEED
                print(traceback.format_exc())
            time.sleep(const.SPEED)