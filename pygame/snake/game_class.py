#Standard module
import datetime
import pygame
import random
import time
import traceback

#external module
import pygame
from pygame.locals import *

#Self-made module
import apple_class
import bad_apple_class
import block_class
import const
import frog_class
import gold_apple_class
import rain_class
import cicada_class
import snake_class
import score_class
import snake_poop_class


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(const.CAPTION)
        pygame.mixer.init()
        #インスタンスの初期化
        self.surface = pygame.display.set_mode((const.DIP_W, const.DIP_H))
        self.block = block_class.Block(self.surface)
        self.snake = snake_class.Snake(self.surface)
        self.apple = apple_class.Apple(self.surface)
        self.bad_apple = bad_apple_class.BadApple(self.surface)
        self.gold_apple = gold_apple_class.GoldApple(self.surface)
        self.snake_poop =  snake_poop_class.Poop(self.surface)
        self.score = score_class.Score()
        #セミをインスタンス化
        self.cicada = cicada_class.Cicada(self.surface)
        #カエルをインスタンス化
        self.frog =  frog_class.Frog(self.surface)
        #雨をインスタンス化
        self.rain = rain_class.Rain(self.surface)
        #バックグラウンド音楽
        self.play_background_music()
        #取得した体
        self.max = 1
        #死因
        self.cause_of_death = 'unknown'
        #蛇がカエルを食べたらTrue
        self.had_frog = False
        #食べたりんごの数
        self.had_apple_cnt = 0

    def play_background_music(self):
        if const.SOUND:
            self.m = random.randint(1, 3)
            if self.m == 1:
                pygame.mixer.music.load(const.B_MUSIC_PATH)
            elif self.m == 2:
                #音量を下げる
                pygame.mixer.music.set_volume(0.5)
                pygame.mixer.music.load(const.B_RAIN_PATH)
            elif self.m == 3:
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
            elif sound_name == 'die':
                sound = pygame.mixer.Sound(const.GET_POOP_SOUND_PATH)
            elif sound_name == 'frog':
                sound = pygame.mixer.Sound(const.GET_FROG_SOUND_PATH)
            elif sound_name == 'had_poop':
                sound = pygame.mixer.Sound(const.GET_POOP_SOUND_PATH)
            pygame.mixer.Sound.play(sound)

    #インスタンスのリセット
    def reset(self):
        self.snake = snake_class.Snake(self.surface)
        self.apple = apple_class.Apple(self.surface)
        self.bad_apple = bad_apple_class.BadApple(self.surface)
        self.gold_apple = gold_apple_class.GoldApple(self.surface)
        self.snake_poop = snake_poop_class.Poop(self.surface)
        self.frog = frog_class.Frog(self.surface)
        self.rain = rain_class.Rain(self.surface)
        self.score = score_class.Score()
        #取ったりんごの数を0にリセット
        self.had_apple_cnt = 0
    #衝突判定
    def is_collision(self, x1, y1, x2, y2):
        if (x1 >= x2 and x1 < x2 + const.SIZE) or (x1 + const.SIZE >= x2 and x1 + const.SIZE < x2 + const.SIZE):
            if (y1 >= y2 and y1 < y2 + const.SIZE) or (y1 + const.SIZE >= y2 and y1 + const.SIZE < y2 + const.SIZE):
                    return True
        return False

    def had_bad_apple(self, x1, y1):
        cnt = -1
        for i in self.bad_apple.bad_apples:
            cnt += 1
            x2 = i[0]
            y2 = i[1]
            if x1 >= x2 and x1 < x2 + const.SIZE:
                if y1 >= y2 and y1 < y2 + const.SIZE:
                    #ぶつかったBADりんごを削除
                    del self.bad_apple.bad_apples[cnt]
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
        #雨が降る
        if self.m == 2:
            self.rain.draw()
        elif self.m == 3:
            self.cicada.draw()
        self.block.draw()
        self.snake.walk()


        #りんごを描く
        self.apple.draw()
        self.bad_apple.draw()
        #舌を出す・出さない
        if self.snake.out:
            self.snake.out = False
            self.snake.tongue()
        else:
            self.snake.out = True
            self.snake.tongue()

        #ゴールドアップルを作る
        if ((self.snake.length % 10 == 0 and self.gold_apple.cnt == 1) and len(self.bad_apple.bad_apples) >= 10):
            self.gold_apple.make_gold_apple()
            self.gold_apple.cnt += 1
            self.play_background_music()
        self.gold_apple.draw()
        # 蛇がりんごを食べた！
        if self.is_collision(int(self.snake.x[0]), int(self.snake.y[0]), int(self.apple.x), int(self.apple.y)):
            self.play_sound('ding')
            #食べた数をカウントアップ
            self.had_apple_cnt += 1
            #体を増やす
            self.snake.increase_length()
            #腐ったりんごの配置
            if self.had_apple_cnt < 50:
                random_ = random.randint(1, 2)
            elif self.had_apple_cnt < 100:
                random_ = random.randint(1, 4)
            else:
                random_ = random.randint(2, 4)
            for i in range(random_):
                self.bad_apple.make_bad_apple(self.apple.x, self.apple.y, self.block.blocks)
            #りんごの再配置
            #ブッロクと重ならないように配置
            #青りんごと重ならないように配置
            self.apple.move(self.bad_apple.bad_apples, self.block.blocks)
            #カエルを放出
            if (len(self.bad_apple.bad_apples) > 10 and self.snake.length % 15 == 0):
                self.frog.is_frog = True
                self.frog.move(self.bad_apple.bad_apples)
        # カエルの鳴き声
        if self.frog.is_frog:
            self.play_sound('frog')
        self.frog.draw()
        # 蛇が金のりんごを食べた！
        if self.is_collision(int(self.snake.x[0]), int(self.snake.y[0]), int(self.gold_apple.x), int(self.gold_apple.y)):
            self.play_sound('gold')
            self.bad_apple.del_apples(10)
            self.gold_apple = gold_apple_class.GoldApple(self.surface)
            self.gold_apple.cnt = 1
            self.snake.get_gold_apple = True
            #うんこをする
            self.snake_poop.make_poop(self.apple.x, self.apple.y, self.snake.x, self.snake.y)
            #goldを食べたときのスキンエフェクト
            self.snake.chcg()
            #うんこ放出
            self.snake_poop.make_poop(self.snake.x, self.snake.y)
        self.snake_poop.draw()
        # 蛇が腐ったりんごを食べた！
        if self.had_bad_apple(int(self.snake.x[0]), int(self.snake.y[0])):
            self.play_sound('bad')
            self.snake.had_bad_apple_skin_effect()
            #体の数を減らす
            self.snake.decrease_length()
            self.snake.s_cnt = 1
            self.snake.speedup()
            if self.snake.length == 1:
                self.play_sound('die')
                self.cause_of_death = const.G_OVER_CAUSE_BAD_APPLE
                raise Exception(const.G_OVER_CAUSE_BAD_APPLE)
        # 蛇がうんこを食べた！
        if self.is_collision(int(self.snake.x[0]), int(self.snake.y[0]),
                                int(self.snake_poop.poop_x - 10), int(self.snake_poop.poop_y - 10)):
            self.play_sound('die')
            self.cause_of_death = const.G_OVER_CAUSE_POOP
            raise Exception(const.G_OVER_CAUSE_POOP)
        # 蛇がカエルを食べた！
        if self.is_collision(int(self.snake.x[0]), int(self.snake.y[0]), int(self.frog.x), int(self.frog.y)):
            #蛇がカエルを食べた
            self.had_frog = True
            #カエルが死んだ
            self.frog.is_frog = False
            #体を増やす
            self.snake.increase_length()
            self.snake.increase_length()
            self.frog = frog_class.Frog(self.surface)
        # 枠を出たらUターン
        if ((self.snake.x[0] + const.SIZE * 2 > const.DIP_W) or (self.snake.x[0] < 0 + const.SIZE * 1)
            or (self.snake.y[0] + const.SIZE * 2 > const.DIP_H) or (self.snake.y[0] < 0 + const.SIZE * 1)):
            #基準軸を超えたら軸を初期化
            if self.snake.x[0] + const.SIZE * 3 > const.DIP_W:
                self.snake.x[0] = const.DIP_W - const.SIZE * 2
            if self.snake.x[0] <  0 + const.SIZE * 2:
                self.snake.x[0] =  0 + const.SIZE
            if self.snake.y[0] + const.SIZE * 3  > const.DIP_H:
                self.snake.y[0] = const.DIP_H - const.SIZE * 2
            if self.snake.y[0] < 0 + const.SIZE * 2:
                self.snake.y[0] = 0 + const.SIZE
            if self.snake.directions[-1] == 'left':
                self.snake.move_right()
            elif self.snake.directions[-1] == 'right':
                self.snake.move_left()
            elif self.snake.directions[-1] == 'up':
                self.snake.move_down()
            elif self.snake.directions[-1] == 'down':
                self.snake.move_up()
            #蛇が枠外に侵攻
            #蛇の動きと逆方向に座標をずらす
            #if self.snake.directions[-1] == 'up':
            #    self.apple.out_of_range_move_up()
            #    self.bad_apple.out_of_range_move_up()
            #    self.gold_apple.out_of_range_move_up()
            #    self.frog.out_of_range_move_up()
            #    self.snake_poop.out_of_range_move_up()
            #elif self.snake.directions[-1] == 'down':
            #    self.apple.out_of_range_move_down()
            #    self.bad_apple.out_of_range_move_down()
            #    self.gold_apple.out_of_range_move_down()
            #    self.frog.out_of_range_move_down()
            #    self.snake_poop.out_of_range_move_down()
            #elif self.snake.directions[-1] == 'right':
            #    self.apple.out_of_range_move_right()
            #    self.bad_apple.out_of_range_move_right()
            #    self.gold_apple.out_of_range_move_right()
            #    self.frog.out_of_range_move_right()
            #    self.snake_poop.out_of_range_move_right()
            #elif self.snake.directions[-1] == 'left':
            #    self.apple.out_of_range_move_left()
            #    self.bad_apple.out_of_range_move_left()
            #    self.gold_apple.out_of_range_move_left()
            #    self.frog.out_of_range_move_left()
            #    self.snake_poop.out_of_range_move_left()
        #スコアの表示
        self.display_score()

        #SPEED PANIC 確認
        if self.snake.s_cnt == 1:
            #設定された時間ない
            #蛇がカエルを食べていない
            #パニックにする
            if datetime.datetime.now() < self.snake.d and self.had_frog is False:
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
                #self.snake.panic_cnt += 1
                #if self.snake.panic_cnt % 2 == 0:
                #    self.snake.image = pygame.image.load(const.SNAKE_BLUE_IMG_PATH).convert()
                #    self.snake.draw()
                #    pygame.display.flip()
                #else:
                #    self.snake.image = self.snake.init_body
                #    self.snake.draw()
                #    pygame.display.flip()
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
        #蛇がカエルを食べたらTrue
        self.had_frog = False
        #最大長を保持
        if self.max <= self.had_apple_cnt:
            self.max = self.had_apple_cnt
        #画面の更新
        pygame.display.flip()

    #スコアの画面表示
    def display_score(self):
        font = pygame.font.SysFont(const.G_OVER_FONT,const.G_OVER_FONT_SIZE)
        #if const.SPEED == const.NORMAL_SPEED:
        #    speed = font.render('speed: normal', True, const.WHITE)
        #elif const.SPEED == const.FAST_SPEED:
        #    speed = font.render('speed: fast', True, const.WHITE)
        #else:
        #    speed = font.render('speed: panic', True, const.WHITE)
        #count_bad = font.render(f'number of bad apples: {self.bad_apple.cnt}', True, const.WHITE)
        #snake_length = font.render(f'Body length: {self.snake.length}', True, const.WHITE)
        had_apple_cnt = font.render(f'Number of apples your snake had: {self.had_apple_cnt}', True, const.WHITE)
        best_score  = font.render(f'Best record ever: {self.score.b_score}', True, const.GOLD)

        #self.surface.blit(speed, (30, 10))
        #self.surface.blit(count_bad,(180, 10))
        #self.surface.blit(snake_length, (420, 10))
        self.surface.blit(had_apple_cnt, (const.SIZE, 10))
        self.surface.blit(best_score, (const.SIZE, const.DIP_H - const.SIZE * 2))

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
                raise Exception(const.INVALID_NUM_ERR)

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
        line2 = font.render(const.G_OVER_OP + 'apples', True, const.WHITE)
        self.surface.blit(line2, (const.DIP_W / 4, const.DIP_H / 2 + 40))
        if self.cause_of_death == const.G_OVER_CAUSE_BAD_APPLE:
            line3 = font.render(f'Cause of death: {const.G_OVER_CAUSE_BAD_APPLE}' , True, const.GOLD)
        elif self.cause_of_death == const.G_OVER_CAUSE_POOP:
            line3 = font.render(f'Cause of death: {const.G_OVER_CAUSE_POOP}' , True, const.GOLD)

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
                print(e)
                self.show_game_over()
                self.reset()
                pause = True
                const.SPEED = const.NORMAL_SPEED
                print(traceback.format_exc())
            time.sleep(const.SPEED)