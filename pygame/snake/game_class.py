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
from app.utils_class import Utils
import app.const as const
from app.creatures_class import Cicada, Bird, Frog, Snake, Poop
from app.fruits_class import Apple, BadApple, GoldApple
import app.grass_class as grass_class
import app.rain_class as rain_class
import app.score_class as score_class


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(const.CAPTION)
        pygame.mixer.init()
        #インスタンスの初期化
        self.surface = pygame.display.set_mode((const.DIP_W, const.DIP_H))
        self.grass = grass_class.Grass(self.surface)
        self.apple = Apple(self.surface)
        self.snake = Snake(self.surface)
        self.bad_apple = BadApple(self.surface)
        self.gold_apple = GoldApple(self.surface)
        self.snake_poop =  Poop(self.surface)
        self.score = score_class.Score()
        #セミをインスタンス化
        self.cicada = Cicada(self.surface)
        #カエルをインスタンス化
        self.frog =  Frog(self.surface)
        #雨をインスタンス化
        self.rain = rain_class.Rain(self.surface)
        #鳥をインスタンス化
        self.bird = Bird(self.surface)
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
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface)
        self.bad_apple = BadApple(self.surface)
        self.gold_apple = GoldApple(self.surface)
        self.snake_poop = Poop(self.surface)
        self.frog = Frog(self.surface)
        self.rain = rain_class.Rain(self.surface)
        self.cicada = Cicada(self.surface)
        self.bird = Bird(self.surface)
        self.score = score_class.Score()
        #取ったりんごの数を0にリセット
        self.had_apple_cnt = 0

    #背景
    def render_background(self):
        bg = pygame.image.load(const.B_IMG_PATH)
        self.surface.blit(bg, (0, 0))
    #fast move
    def fast_move(self):
        const.SPEED = const.FAST_SPEED

    def play(self):
        #背景の描画self.frog.is_alive
        self.render_background()
        #草を描く
        self.grass.draw()
        #音楽毎の設定
        if self.m == 1:
            self.bird.draw()
        elif self.m == 2:
            #雨が降る
            self.rain.draw()
            # カエルの鳴き声
            if self.frog.is_alive:
                self.play_sound('frog')
            self.frog.draw()
        elif self.m == 3:
            self.cicada.draw()
        #ヘビ歩く
        self.snake.walk()
        #りんごを描く
        self.apple.draw()
        #青りんごを描く
        self.bad_apple.draw()
        #舌を出す・出さない
        if self.snake.out:
            self.snake.out = False
            self.snake.tongue()
        else:
            self.snake.out = True
            self.snake.tongue()
        #ゴールドアップルを作る
        if ((self.snake.length % 10 == 0
            and len(self.gold_apple.fruits) == 1)
            and len(self.bad_apple.fruits) >= 10):
            self.gold_apple.make_gold_apple()
            self.gold_apple.cnt += 1
            self.play_background_music()
        self.gold_apple.draw()
        # 蛇がりんごを食べた！
        if Utils.collision_check(int(self.snake.x[0]),
            int(self.snake.y[0]), self.apple.fruits):
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
                self.bad_apple.make(self.bad_apple.fruits)
            #りんごの再配置
            #ブッロクと重ならないように配置
            #青りんごと重ならないように配置
            self.apple.remove(self.apple.x, self.apple.y)
            self.apple.make(self.bad_apple.fruits)
            #生き物たち
            if self.m == 1:
                #鳥を放出
                if (len(self.bad_apple.fruits) > 5
                    and self.snake.length % 7 == 0):
                    if self.bird.is_alive is False:
                        self.bird.make(self.bad_apple.fruits)
            elif self.m == 2:
                #カエルを放出
                if (len(self.bad_apple.fruits) > 5
                    and self.snake.length % 7 == 0):
                    if self.had_frog is False:
                        self.frog.move(self.bad_apple.fruits)
            elif self.m == 3:
                #セミ放出
                if (len(self.bad_apple.fruits) > 5
                    and self.snake.length % 7 == 0):
                    if self.cicada.is_alive is False:
                        self.cicada.make(self.bad_apple.fruits)
        # 蛇が金のりんごを食べた！
        if Utils.collision_check(int(self.snake.x[0]),
            int(self.snake.y[0]), self.gold_apple.fruits):
            self.play_sound('gold')
            self.bad_apple.del_apples(10)
            self.gold_apple = GoldApple(self.surface)
            self.gold_apple.cnt = 1
            self.snake.get_gold_apple = True
            #うんこをする
            self.snake_poop.make_poop(self.snake.x, self.snake.y)
            #goldを食べたときのスキンエフェクト
            self.snake.skin_effect_af_gold_apple()
            #うんこ放出
            self.snake_poop.make_poop(self.snake.x, self.snake.y)
            #音楽を変更
            self.play_background_music()
        self.snake_poop.draw()
        # 蛇が腐ったりんごを食べた！
        if Utils.collision_check(int(self.snake.x[0]),
            int(self.snake.y[0]), self.bad_apple.fruits):
            #食べた青りんごを削除
            self.bad_apple.remove(self.snake.x[0], self.snake.y[0])
            self.play_sound('bad')
            self.snake.skin_effect_af_bad_apple()
            #体の数を減らす
            self.snake.decrease_length()
            #パニック状態にする
            self.snake.s_cnt = 1
            self.snake.speedup()
            if self.snake.length == 1:
                self.play_sound('die')
                self.cause_of_death = const.G_OVER_CAUSE_BAD_APPLE
                raise Exception(const.G_OVER_CAUSE_BAD_APPLE)
        # 蛇がうんこを食べた！
        if Utils.collision_check(int(self.snake.x[0]),
            int(self.snake.y[0]), self.snake_poop.creatures):
            self.play_sound('die')
            self.cause_of_death = const.G_OVER_CAUSE_POOP
            raise Exception(const.G_OVER_CAUSE_POOP)
        # 蛇がカエルを食べた！
        if Utils.collision_check(int(self.snake.x[0]),
            int(self.snake.y[0]), self.frog.creatures):
            #蛇がカエルを食べた
            self.had_frog = True
            #カエルが死んだ
            self.frog.is_alive = False
            #体を増やす
            self.snake.increase_length(3)
            self.snake.draw()
            self.frog = Frog(self.surface)
        # 蛇がセミを食べた！
        if Utils.collision_check(int(self.snake.x[0]),
            int(self.snake.y[0]), self.cicada.creatures):
            self.cicada.is_alive = False
            #体を増やす
            self.snake.increase_length(3)
            self.snake.draw()
            self.cicada = Cicada(self.surface)
        # 蛇が鳥を食べた！
        if Utils.collision_check(int(self.snake.x[0]),
            int(self.snake.y[0]), self.bird.creatures):
            self.bird.is_bird = False
            #体を増やす
            self.snake.increase_length(3)
            self.snake.draw()
            self.bird = Bird(self.surface)
        # 枠を出たらUターン
        if (   (self.snake.x[0] + const.SIZE > const.DIP_W)
            or (self.snake.x[0] < 0)
            or (self.snake.y[0] + const.SIZE > const.DIP_H)
            or (self.snake.y[0] < 0)):
            #基準軸を超えたら軸を初期化
            if self.snake.x[0] > const.DIP_W:
                self.snake.x[0] = const.DIP_W
            elif self.snake.x[0] <  0:
                self.snake.x[0] =  0
            elif self.snake.y[0] + const.SIZE * 2 > const.DIP_H:
                self.snake.y[0] = const.DIP_H - const.SIZE * 2
            elif self.snake.y[0] < 0:
                self.snake.y[0] = 0
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
            #設定された時間ない
            #蛇がカエルを食べていない
            #パニックにする
            if (datetime.datetime.now() < self.snake.d
                and self.had_frog is False):
                #スピードのパラメータ変更
                const.SPEED = const.PANIC_SPEED
                self.snake.while_having_bad_apple()
            else:
                self.snake.turn_back_skin_color()
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
        had_apple_cnt = font.render(f'Number of apples your snake had: {self.had_apple_cnt}', True, const.WHITE)
        best_score  = font.render(f'Best record ever: {self.score.b_score}', True, const.WHITE)
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

if __name__ == '__main__':
    game = Game()
    game.run()