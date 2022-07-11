#Standard module
import datetime
import pygame
import random
import time
import traceback

#external module
import pygame
from pygame.locals import *
#import win32gui
#from PIL import ImageGrab

#Self-made module
from app.utils_class import Utils
import app.const as const
from app.creatures_class import Cicada, Bird, Frog, Snake, Poop
from app.fruits_class import Apple, BadApple, GoldApple
import app.grass_class as grass_class
import app.life_class as life_class
import app.rain_class as rain_class


class Game:
    def __init__(self):
        pygame.init()
        #pygame.display.set_caption(const.CAPTION)
        pygame.mixer.init()
        self.surface = pygame.display.set_mode((const.DIP_W, const.DIP_H), FULLSCREEN)
        width, height = pygame.display.get_surface().get_size()
        if width - 1250 > 0:
            #スタート画像(700px x 1250px)が起動されたPCのフルスクリーンより小さい場合、
            #中央に配置
            const.START_DIP_W = (width - 1250) / 2
        else:
            const.START_DIP_W = width
        #ゲーム中の背景画面
        const.DIP_W = width

        if height - 700 > 0:
            #スタート画像(700px x 1250px)が起動されたPCのフルスクリーンより小さい場合、
            #中央に配置
            const.START_DIP_H = (height - 700) / 2
        else:
            const.START_DIP_H = height
        #ゲーム中の背景画面
        const.DIP_H = height
        #バックグラウンド音楽
        self.play_background_music()
        # インスタンスの初期化
        self.grass = grass_class.Grass(self.surface)
        self.apple = Apple(self.surface)
        self.snakes = [
            Snake(self.surface, const.PLAYER1,int(const.DIP_W / 4), int(const.DIP_H / 4 - const.SIZE / 4))
            ,Snake(self.surface, const.PLAYER2,int(const.DIP_W / 2), int(const.DIP_H / 4 - const.SIZE / 4))
        ]
        self.bad_apple = BadApple(self.surface)
        self.gold_apple = GoldApple(self.surface)
        self.snake_poop =  Poop(self.surface)
        #セミをインスタンス化
        self.cicada = Cicada(self.surface)
        #カエルをインスタンス化
        self.frog =  Frog(self.surface)
        #雨をインスタンス化
        self.rain = rain_class.Rain(self.surface)
        #鳥をインスタンス化
        self.bird = Bird(self.surface)

    # スタート画面
    def render_start(self):
        st = pygame.image.load(const.START_IMG_PATH)
        self.surface.blit(st, (const.START_DIP_W, const.START_DIP_H))
        pygame.display.flip()

    #背景
    def render_background(self):
        pass
        bg = pygame.image.load(const.B_IMG_PATH)
        self.surface.blit(bg, (0, 0))

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
        self.apple = Apple(self.surface)
        self.snakes = [
            Snake(self.surface, const.PLAYER1,const.DIP_W / 4, const.DIP_H / 4 - const.SIZE / 4)
            ,Snake(self.surface, const.PLAYER2,const.DIP_W / 2, const.DIP_H / 4 - const.SIZE / 4)
        ]
        self.bad_apple = BadApple(self.surface)
        self.gold_apple = GoldApple(self.surface)
        self.snake_poop = Poop(self.surface)
        self.frog = Frog(self.surface)
        self.rain = rain_class.Rain(self.surface)
        self.cicada = Cicada(self.surface)
        self.bird = Bird(self.surface)

    def play(self):
        #背景の描画
        self.render_background()

        #草を描く
        self.grass.draw()
        #音楽毎の設定
        if self.m == 1:
            self.bird.draw()
            self.cicada = Cicada(self.surface)
            self.frog = Frog(self.surface)
        elif self.m == 2:
            #雨が降る
            self.cicada = Cicada(self.surface)
            self.bird = Bird(self.surface)
            self.rain.draw()
            # カエルの鳴き声
            if self.frog.is_alive:
                self.play_sound('frog')
            self.frog.draw()
        elif self.m == 3:
            self.bird = Bird(self.surface)
            self.frog = Frog(self.surface)
            self.cicada.draw()
        #ヘビ歩く
        for self.snake in self.snakes:
            #ヘビが生きているかライフチェック
            #ヘビのライフがなければ原因オーバー
            if self.snake.life.death_check():
                raise Exception('game over')
            else:
            #ライフポイントを表示
                self.snake.life.draw()
                self.snake.walk()
                #舌を出す・出さない
                if self.snake.out:
                    self.snake.out = False
                    self.snake.tongue()
                else:
                    self.snake.out = True
                    self.snake.tongue()
        #りんごを描く
        self.apple.draw()
        #青りんごを描く
        self.bad_apple.draw()
        # 蛇がりんごを食べた！
        for self.snake in self.snakes:
            if Utils.collision_check(int(self.snake.x[0]),
                int(self.snake.y[0]), self.apple.fruits):
                self.play_sound('ding')
                #食べた数をカウントアップ
                self.snake.had_apple_cnt += 1
                #体を増やす
                self.snake.increase_length()
                #アップの獲得数で青りんごの数を変える
                if self.snake.had_apple_cnt < 10:
                    self.bad_apple.make(self.bad_apple.fruits, 1)
                elif 10 <= self.snake.had_apple_cnt and self.snake.had_apple_cnt < 50:
                    self.bad_apple.make(self.bad_apple.fruits, 2)
                elif 50 <= self.snake.had_apple_cnt and self.snake.had_apple_cnt < 100:
                    self.bad_apple.make(self.bad_apple.fruits, 3)
                elif 100 <= self.snake.had_apple_cnt and self.snake.had_apple_cnt < 200:
                    self.bad_apple.make(self.bad_apple.fruits, 4)
                else:
                    self.bad_apple.make(self.bad_apple.fruits, 5)
                #りんごの再配置
                #ブッロクと重ならないように配置
                #青りんごと重ならないように配置
                self.apple.remove(self.snake.x[0], self.snake.y[0])
                if len(self.apple.fruits) <= 1:
                    self.apple.make(self.bad_apple.fruits, 1)
                #生き物たち
                if self.m == 1:
                    #鳥を放出
                    if (len(self.bad_apple.fruits) > 10
                        and self.snake.had_apple_cnt % 5 == 0
                        and len(self.bird.creatures) <= 2):
                            self.bird.is_alive = True
                            self.bird.make(self.bad_apple.fruits, 1)
                elif self.m == 2:
                    #カエルを放出
                    if (len(self.bad_apple.fruits) > 10
                        and self.snake.had_apple_cnt % 4 == 0
                        and len(self.frog.creatures) <= 5):
                            self.frog.is_alive = True
                            self.frog.make(self.bad_apple.fruits, 1)
                elif self.m == 3:
                    #セミ放出
                    if (len(self.bad_apple.fruits) > 10
                        and self.snake.had_apple_cnt % 3 == 0
                        and len(self.cicada.creatures) <= 1):
                            self.cicada.is_alive = True
                            self.cicada.make(self.bad_apple.fruits, 1)
                #金りんごを作る
                if (self.snake.had_apple_cnt % 4 == 0
                    and len(self.gold_apple.fruits) == 0
                    and len(self.bad_apple.fruits) > 10):
                    self.gold_apple.make(self.bad_apple.fruits, 1)
        self.bird.draw()
        self.frog.draw()
        self.cicada.draw()
        self.gold_apple.draw()
        # 蛇が金のりんごを食べた！
        for self.snake in self.snakes:
            if Utils.collision_check(self.snake.x[0],
                self.snake.y[0], self.gold_apple.fruits):
                self.snake.had_gold_apple_cnt += 1
                self.play_sound('gold')
                self.snake.increase_length(5)
                self.bad_apple.remove(self.snake.x[0], self.snake.y[0], 10)
                self.gold_apple = GoldApple(self.surface)
                self.snake.get_gold_apple = True
                #うんこをする
                if len(self.snake_poop.creatures) <= 2:
                    self.snake_poop.make(self.apple.fruits, 1)
                else:
                    self.snake_poop.move(self.apple.fruits)
                #goldを食べたときのスキンエフェクト
                self.snake.skin_effect_af_gold_apple()
                #音楽を変更
                self.play_background_music()
            self.snake_poop.draw()
            # 蛇が腐ったりんごを食べた！
            if Utils.collision_check(int(self.snake.x[0]),
                int(self.snake.y[0]), self.bad_apple.fruits):
                self.snake.had_bad_apple_cnt += 1
                #食べた青りんごを削除
                self.bad_apple.remove(self.snake.x[0], self.snake.y[0], 1)
                self.play_sound('bad')
                self.snake.skin_effect_af_bad_apple()
                #体の数を減らす
                self.snake.decrease_length()
                if self.snake.length == 1:
                    #ライフを一つ減らす
                    self.play_sound('die')
                    self.snake.life.remove()
                    #初期化
                    self.snake.directions = []
                    self.snake.directions = [
                                            'down'
                                            ,'down'
                    ]
                    self.snake.x = []
                    self.snake.y = []
                    if self.snake == self.snakes[0]:
                        self.snake.x.append(int(const.DIP_W / 4))
                    elif self.snake == self.snakes[1]:
                        self.snake.x.append(int(const.DIP_W / 2))
                    self.snake.y.append(int(const.DIP_H / 4 - const.SIZE / 4))
                    self.apple.make_init()
                    self.bad_apple = BadApple(self.surface)
                    self.snake_poop = Poop(self.surface)
            # 蛇がうんこを食べた！
            if Utils.collision_check(self.snake.x[0],
                int(self.snake.y[0]), self.snake_poop.creatures):
                self.snake.had_snake_poop_cnt += 1
                self.play_sound('die')
                self.snake.skin_effect_af_bad_apple()
                self.snake_poop.remove()
                self.snake.life.remove()

            # 蛇がカエルを食べた！
            if Utils.collision_check(int(self.snake.x[0]),
                int(self.snake.y[0]), self.frog.creatures):
                self.snake.had_frog_cnt += 1
                self.play_sound('gold')
                #カエルが死んだ
                self.frog.is_alive = False
                #りんごを増やす
                self.apple.make(self.bad_apple.fruits,5)
                self.frog.remove(self.snake.x[0], self.snake.y[0])
            # 蛇がセミを食べた！
            if Utils.collision_check(int(self.snake.x[0]),
                int(self.snake.y[0]), self.cicada.creatures):
                self.snake.had_cicada_cnt += 1
                self.play_sound('gold')
                #りんごを増やす
                self.apple.make(self.bad_apple.fruits,3)
                self.cicada = Cicada(self.surface)
            # 蛇が鳥を食べた！
            if Utils.collision_check(int(self.snake.x[0]),
                int(self.snake.y[0]), self.bird.creatures):
                self.snake.had_frog_cnt += 1
                self.play_sound('gold')
                #りんごを増やす
                self.apple.make(self.bad_apple.fruits,3)
                self.snake.increase_length(3)
                self.bird.remove(self.snake.x[0], self.snake.y[0])
            if (   (self.snake.x[0]  > const.PLAY_DIP_W)
                or (self.snake.x[0] < 0)
                or (self.snake.y[0] + const.SIZE > const.DIP_H)
                or (self.snake.y[0] < 0)):
                #基準軸を超えたら軸を初期化
                if self.snake.x[0] > const.PLAY_DIP_W - const.SIZE:
                    self.snake.x[0] = const.PLAY_DIP_W
                elif self.snake.x[0] < 0:
                    self.snake.x[0] = 0
                elif self.snake.y[0] + const.SIZE * 2 > const.DIP_H:
                    self.snake.y[0] = const.DIP_H - const.SIZE
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

            #最大長を保持
            if self.snake.max_length <= self.snake.length:
                self.snake.max_length = self.snake.length
            self.snake.draw()
        #画面の更新
        pygame.display.flip()

    #スコアの画面表示
    def display_score(self):
        font = pygame.font.SysFont(const.G_OVER_FONT,const.G_OVER_FONT_SIZE)
        for self.snake in self.snakes:
            if self.snake == self.snakes[0]:
                y = [3, 1, 2, 3, 4, 5, 6]
            elif self.snake == self.snakes[1]:
                y = [const.SIZE * 8, 9, 10, 11, 12, 13, 14]
            player_name = font.render(self.snake.get_name(), True, const.WHITE)
            life  = font.render('Life: ', True, const.WHITE)
            had_red_apple = font.render('Red Apple: ' + str(self.snake.had_apple_cnt), True, const.WHITE)
            snake_length  = font.render('Snake Length: ' + str(self.snake.length), True, const.WHITE)
            snake_length_max  = font.render('(MAX Length): ' + str(self.snake.max_length), True, const.WHITE)
            note1 = font.render('Space: Pause', True, const.WHITE)
            note2 = font.render('Esc: Exit', True, const.WHITE)

            self.surface.blit(player_name, (const.DIP_W - const.SIZE * 5.5, y[0]))
            self.surface.blit(life, (const.DIP_W - const.SIZE * 5.5, const.SIZE * y[1]))
            self.surface.blit(had_red_apple, (const.DIP_W - const.SIZE * 5.5, const.SIZE * y[2]))
            self.surface.blit(snake_length, (const.DIP_W - const.SIZE * 5.5, const.SIZE * y[3]))
            self.surface.blit(snake_length_max, (const.DIP_W - const.SIZE * 5.5, const.SIZE * y[4]))
            score_str = font.render('Score: ' + str(self.snake.get_score()), True, const.GOLD)
            self.surface.blit(score_str, (const.DIP_W - const.SIZE * 5.5, const.SIZE * y[5]))


        self.surface.blit(note1, (const.DIP_W - const.SIZE * 5.5, const.DIP_H - const.SIZE * 3))
        self.surface.blit(note2, (const.DIP_W - const.SIZE * 5.5, const.DIP_H - const.SIZE * 2))
        #スコアアイテム表示
        score_items = pygame.image.load(const.SCORE_ITEMS_IMG_PATH)
        self.surface.blit(score_items, (0, 0))

    #Game Over画面
    def show_game_over(self):
        font = pygame.font.SysFont(const.G_OVER_FONT, const.G_OVER_FONT_SIZE)
        for self.snake in self.snakes:
            line1 = font.render(self.snake.get_name() + ' had ' + str(self.snake.get_score()) + '.', True, const.WHITE)
            if self.snake == self.snakes[0]:
                self.surface.blit(line1, (const.DIP_W / 4, const.DIP_H / 2 - const.SIZE))
            elif self.snake == self.snakes[1]:
                self.surface.blit(line1, (const.DIP_W / 4, const.DIP_H / 2 + const.SIZE))
        line3 = font.render(const.G_OVER_OP, True, const.WHITE)
        self.surface.blit(line3, (const.DIP_W / 4, const.DIP_H / 2 + const.SIZE * 3))
        #画面の更新
        pygame.display.flip()

    def run(self):
        running = True
        first_time = True
        pause = False
        cnt = 0
        while running:

                if first_time:
                    self.render_start()
                    first_time = False
                    pause = True
                    for event in pygame.event.get():
                        if event.type == KEYDOWN:
                            if event.key == K_RETURN:
                                pause = False
                                cnt += 1
                            elif event.type == QUIT:
                                running = False
                else:
                    for event in pygame.event.get():
                        if event.type == KEYDOWN:
                            if event.key == K_RETURN:
                                pause = False
                                self.play_background_music()
                            if event.key == K_ESCAPE:
                                running = False
                            if event.key == K_SPACE:
                                if pause == True:
                                    pause = False
                                    pygame.mixer.music.unpause()
                                else:
                                    pause = True
                                    pygame.mixer.music.pause()
                            if not pause:
                                #Snake 1P
                                if event.key == K_LEFT:
                                    self.snakes[0].move_left()
                                if event.key == K_RIGHT:
                                    self.snakes[0].move_right()
                                if event.key == K_UP:
                                    self.snakes[0].move_up()
                                if event.key == K_DOWN:
                                    self.snakes[0].move_down()

                                #Snake 2P
                                if event.key == K_z:
                                    self.snakes[1].move_left()
                                if event.key == K_c:
                                    self.snakes[1].move_right()
                                if event.key == K_s:
                                    self.snakes[1].move_up()
                                if event.key == K_x:
                                    self.snakes[1].move_down()

                        elif event.type == QUIT:
                            running = False
                    try:
                        if not pause:
                            self.play()
                    except Exception as e:
                        pause = True
                        print(traceback.format_exc())
                        self.show_game_over()
                        self.reset()

                    time.sleep(const.SPEED)

if __name__ == '__main__':
    game = Game()
    game.run()