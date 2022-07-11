#Standard module
import datetime
import random

#external module
import pygame

#Self-made module
import app.life_class as life
import app.const as const
from app.utils_class import Utils

#様々な生き物の親になるクラス
class Creatures:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        # x座標、yを配列で保持
        self.creatures = []
        # 生き物が画面上に存在するか否か
        # 存在する場合はTrue
        self.is_alive = False
        # 画像を読み込む
        self.image = None
    # 生き物を作成
    # bad_applesと個数を引数にとる
    def make(self, targets, number = 1):
        # 生き物を生存状態にする
        self.is_alive = True
        # 新しい生き物を作る
        if number == 1:
            self.x , self.y = Utils.make_new_x_y()
            # 青りんごと新しい生き物のX、Y座標が重なっていないか確認
            Utils.check(self.x, self.y, targets)
            # 生き物のみ生き物配列に追加
            self.creatures.append([self.x, self.y])
        else:
            for i in range(number - 1):
                self.x , self.y = Utils.make_new_x_y()
                # 青りんごと新しい生き物のX、Y座標が重なっていないか確認
                Utils.check(self.x, self.y, targets)
                # 生き物のみ生き物配列に追加
                self.creatures.append([self.x, self.y])
    # 生き物をランダムな位置に移動させる
    def move(self, bad_apples):
        self.x , self.y = Utils.make_new_x_y()
        # 青りんごと新しい生き物のX、Y座標が重なっていないか確認
        for i in bad_apples:
            x2 = i[0]
            y2 = i[1]
            while Utils.is_collision(self.x, self.y, x2, y2):
                self.x , self.y = Utils.make_new_x_y()
        self.draw()
    # 生き物とヘビが衝突した場合、衝突した生き物を削除
    # 削除した場合はTrue、してない場合はFalse
    def remove(self, x1, y1):
        no = 0
        for i in self.creatures:
            x2 = i[0]
            y2 = i[1]
            #ヘビの頭とぶつかった生き物を削除
            if Utils.is_collision(x1, y1, x2, y2):
                    #ぶつかったBADりんごを削除
                    del self.creatures[no]
                    return True
            no += 1
        return False
    # 生き物を描画する
    def draw(self, target_list):
        #配列の数分描画
        for i in target_list:
            self.x = i[0]
            self.y = i[1]
            self.parent_screen.blit(self.image, (self.x, self.y))


#鳥クラス
class Bird(Creatures):
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        # x座標、yを配列で保持
        self.creatures = []
        # 生き物が画面上に存在するか否か
        # 存在する場合はTrue
        self.is_alive = False
        # 画像を読み込む
        self.image = pygame.image.load(const.BIRD_IMG_PATH).convert()
    # 生き物を作成
    def make(self, bad_apples, number = 1):
        # 生き物を生存状態にする
        self.is_alive = True
        # 新しい生き物を作る
        if number == 1:
            self.x , self.y = Utils.make_new_x_y()
            # 青りんごと新しい生き物のX、Y座標が重なっていないか確認
            Utils.check(self.x, self.y, bad_apples)
            # 生き物のみ生き物配列に追加
            self.creatures.append([self.x, self.y])
        else:
            for i in range(number - 1):
                self.x , self.y = Utils.make_new_x_y()
                # 青りんごと新しい生き物のX、Y座標が重なっていないか確認
                Utils.check(self.x, self.y, bad_apples)
                # 生き物のみ生き物配列に追加
                self.creatures.append([self.x, self.y])
    # 生き物をランダムな位置に移動させる
    def move(self, bad_apples):
        super().move(bad_apples)
    # 生き物とヘビが衝突した場合、衝突した生き物を削除
    # 削除した場合はTrue、してない場合はFalse
    def remove(self, x1, y1):
        if super().remove(x1, y1):
            return True
        return False
    def draw(self):
        super().draw(self.creatures)

#セミクラス
class Cicada(Creatures):
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        # x座標、yを配列で保持
        self.creatures = []
        # 生き物が画面上に存在するか否か
        # 存在する場合はTrue
        self.is_alive = False
        # 画像を読み込む
        self.image = pygame.image.load(const.CICADA_IMG_PATH).convert()
    # 生き物を作成
    def make(self, bad_apples, number = 1):
        self.x, self.y = 30, 300
        self.creatures.append([self.x, self.y])
    # 生き物をランダムな位置に移動させる
    def move(self, bad_apples):
        super().move(bad_apples)
    # 生き物とヘビが衝突した場合、衝突した生き物を削除
    # 削除した場合はTrue、してない場合はFalse
    def remove(self, x1, y1):
        if super().remove(x1, y1):
            return True
        return False
    def draw(self):
        #配列の数分描画
        for i in self.creatures:
            self.x = i[0]
            self.y = i[1]
            self.parent_screen.blit(self.image, (self.x, self.y))

#カエルクラス
class Frog(Creatures):
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        # x座標、yを配列で保持
        self.creatures = []
        # 生き物が画面上に存在するか否か
        # 存在する場合はTrue
        self.is_alive = False
        # 画像を読み込む
        self.image = pygame.image.load(const.FROG_IMG_PATH).convert()
    # 生き物を作成
    def make(self, apples, number = 1):
        self.x = random.randint(0, const.PLAY_DIP_W - const.SIZE)
        self.y = random.randint(0, const.DIP_H / 2)
        self.creatures.append([self.x, self.y])
    # 生き物をランダムな位置に移動させる
    def move(self, bad_apples):
        super().move(bad_apples)
    # 生き物とヘビが衝突した場合、衝突した生き物を削除
    # 削除した場合はTrue、してない場合はFalse
    def remove(self, x1, y1):
        if super().remove(x1, y1):
            return True
        return False
    def draw(self):
        #配列の数分描画
        for i in self.creatures:
            self.x = i[0]
            self.y = i[1]
            self.parent_screen.blit(self.image, (self.x, self.y))

#POOPクラス
class Poop(Creatures):
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        # x座標、yを配列で保持
        self.creatures = []
        # 生き物が画面上に存在するか否か
        # 存在する場合はTrue
        self.is_alive = False
        # 画像を読み込む
        self.image = pygame.image.load(const.SNAKE_POOP_IMG_PATH).convert()
    # 生き物を作成
    def make(self, apples, number = 1):
        # 生き物を生存状態にする
        self.is_alive = True
        # 新しい生き物を作る
        super().make(apples, number)
    # 生き物をランダムな位置に移動させる
    def move(self, apples):
        super().move(apples)
    # 生き物とヘビが衝突した場合、衝突した生き物を削除
    # 削除した場合はTrue、してない場合はFalse
    def remove(self):
        self.creatures = []
    def draw(self):
        super().draw(self.creatures)

#ヘビクラス
class Snake(Creatures):
    # x,y は初期位置 （赤りんごの位置を考慮）
    # はじめは必ず赤りんごを食べなければヘビの体がレンダリングされないため
    def __init__(self, parent_screen, name, x, y):
        self.parent_screen = parent_screen
        self.__name = name
        #スキンカラーの設定
        self.__red_body_img = pygame.image.load(const.SNAKE_RED_IMG_PATH).convert()
        self.__red_face_img = pygame.image.load(const.SNAKE_RED_FACE_IMG_PATH).convert()
        self.__red_bad_face_img = pygame.image.load(const.SNAKE_RED_HAD_BAD_APPLE_FACE_IMG_PATH).convert()
        self.__red_eating_face_img = pygame.image.load(const.SNAKE_RED_EATING_FACE_IMG_PATH).convert()
        self.__green_body_img = pygame.image.load(const.SNAKE_GREEN_IMG_PATH).convert()
        self.__green_face_img = pygame.image.load(const.SNAKE_GREEN_FACE_IMG_PATH).convert()
        self.__green_bad_face_img = pygame.image.load(const.SNAKE_GREEN_HAD_BAD_APPLE_FACE_IMG_PATH).convert()
        self.__green_eating_face_img = pygame.image.load(const.SNAKE_GREEN_EATING_FACE_IMG_PATH).convert()
        self.__yellow_body_img = pygame.image.load(const.SNAKE_YELLOW_IMG_PATH).convert()
        self.__yellow_face_img = pygame.image.load(const.SNAKE_YELLOW_FACE_IMG_PATH).convert()
        self.__yellow_bad_face_img = pygame.image.load(const.SNAKE_YELLOW_HAD_BAD_APPLE_FACE_IMG_PATH).convert()
        self.__yellow_eating_face_img = pygame.image.load(const.SNAKE_YELLOW_EATING_FACE_IMG_PATH).convert()
        self.__blue_body_img = pygame.image.load(const.SNAKE_BLUE_IMG_PATH).convert()
        self.__blue_bad_face_img = pygame.image.load(const.SNAKE_BLUE_HAD_BAD_APPLE_FACE_IMG_PATH).convert()
        #初期方向
        self.directions = [
                            'down'
                            ,'down'
        ]
        #初期位置
        self.x = []
        self.x.append(x)
        self.y = []
        self.y.append(y)
        # ライフインスタンスの生成
        # プレイヤーによってライフの表示位置を変える（life_y）
        if self.__name == const.PLAYER1:
            self.color = 1
            life_y = const.SIZE
            self.life = life.Life(self.parent_screen, life_y)
        elif self.__name == const.PLAYER2:
            self.color = 3
            life_y = const.DIP_H / 2
            self.life = life.Life(self.parent_screen, life_y)
        if self.color == 1:
            self.face_img = self.__red_face_img
            self.body_img = self.__red_body_img
        elif self.color == 2:
            self.face_img = self.__green_face_img
            self.body_img = self.__green_body_img
        elif self.color == 3:
            self.face_img = self.__yellow_face_img
            self.body_img = self.__yellow_body_img
        self.face_img = pygame.transform.rotate(self.face_img, 180)
        #最初のお顔を保存
        self.init_face_img = self.face_img
        #最初の体を保存
        self.init_body_img = self.body_img
        #青りんごを食べたあとのスキンエフェクト
        self.effect_af_bad_apple = [
                                    self.init_body_img
                                    ,self.__blue_body_img
        ]
        #金りんごを食べたあとのスキンエフェクト
        self.effect_af_gold_apple = [
                                    self.init_body_img
                                    ,self.__red_body_img
                                    ,self.__green_body_img
                                    ,self.__yellow_body_img
        ]
        self.get_gold_apple = False
        #速く動く
        self.fast_move = False
        #舌を出さない
        self.out = False
        #初期長
        self.length = 1
        #今回のスコア
        self.__this_score = 0
        #取得した体(MAX)
        self.max_length = 1
        #食べたりんごの数
        self.had_apple_cnt = 0
        #食べた青りんごの数
        self.had_bad_apple_cnt = 0
        #食べた金りんごの数
        self.had_gold_apple_cnt = 0
        #食べたうんこの数
        self.had_snake_poop_cnt = 0
        #食べたカエルの数
        self.had_frog_cnt = 0
        #食べたセミの数
        self.had_cicada_cnt = 0
        #食べた鳥の数
        self.had_bird_cnt = 0

        self.draw()
    #名前の取得
    def get_name(self):
        return self.__name

    # ヘビを移動させる
    def move_left(self):
        #お顔の向きを整える
        if self.directions[1] == 'up':
            self.face_img = pygame.transform.rotate(self.face_img, 90)
        elif self.directions[1] == 'down':
            self.face_img = pygame.transform.rotate(self.face_img, -90)
        elif self.directions[1] == 'right':
            self.face_img = pygame.transform.rotate(self.face_img, 180)
        else:
            self.face_img = pygame.transform.rotate(self.face_img, 0)
        self.directions.pop(0)
        self.directions.append('left')

    def move_right(self):
        if self.directions[1] == 'up':
            self.face_img = pygame.transform.rotate(self.face_img, -90)
        elif self.directions[1] == 'down':
            self.face_img = pygame.transform.rotate(self.face_img, 90)
        elif self.directions[1] == 'left':
            self.face_img = pygame.transform.rotate(self.face_img, 180)
        else:
            self.face_img = pygame.transform.rotate(self.face_img, 0)
        self.directions.pop(0)
        self.directions.append('right')

    def move_up(self):
        if self.directions[1] == 'down':
            self.face_img = pygame.transform.rotate(self.face_img, 180)
        elif self.directions[1] == 'left':
            self.face_img = pygame.transform.rotate(self.face_img, -90)
        elif self.directions[1] == 'right':
            self.face_img = pygame.transform.rotate(self.face_img, 90)
        else:
            self.face_img = pygame.transform.rotate(self.face_img, 0)
        self.directions.pop(0)
        self.directions.append('up')

    def move_down(self):
        if self.directions[1] == 'up':
            self.face_img = pygame.transform.rotate(self.face_img, 180)
        elif self.directions[1] == 'left':
            self.face_img = pygame.transform.rotate(self.face_img, 90)
        elif self.directions[1] == 'right':
            self.face_img = pygame.transform.rotate(self.face_img, -90)
        else:
            self.face_img = pygame.transform.rotate(self.face_img, 0)
        self.directions.pop(0)
        self.directions.append('down')

    #ヘビが歩く
    def walk(self):
        # 体をずらす
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
            #しっぽの配列 しっぽはあきらめる！
        #体のポジション
        if self.directions[1] == 'left':
            self.x[0] -= const.SIZE
        if self.directions[1] == 'right':
            self.x[0] += const.SIZE
        if self.directions[1] == 'up':
            self.y[0] -= const.SIZE
        if self.directions[1] == 'down':
            self.y[0] += const.SIZE
        self.draw()

    def draw(self):
        for i in range(self.length - 1):
            self.parent_screen.blit(self.face_img, (self.x[0], self.y[0]))
            self.parent_screen.blit(self.body_img, (self.x[i + 1], self.y[i + 1]))

    #ヘビの体を増やす
    def increase_length(self, number = 1):
        self.length += number
        for i in range(number):
            self.x.append(-1)
            self.y.append(-1)

    #ヘビの体を減らす
    def decrease_length(self):
        if self.length != 1:
            if self.length > 1 and self.length <= 5:
                self.length -= 1
                del self.x[-1]
                del self.y[-1]
            elif self.length > 5 and self.length <= 10:
                self.length -= 3
                del self.x[-3]
                del self.y[-3]
            elif self.length > 10 and self.length <= 15:
                self.length -= 5
                del self.x[-5]
                del self.y[-5]
            elif self.length > 15 and self.length <= 30:
                self.length -= 5
                del self.x[-5]
                del self.y[-5]
            elif self.length > 30:
                self.length -= 10
                del self.x[-10]
                del self.y[-10]
    #goldを食べたときのスキンエフェクト
    def skin_effect_af_gold_apple(self):
        if self.get_gold_apple:
            cnt = 0
            while cnt < 100:
                for i in self.effect_af_gold_apple:
                    self.body_img = i
                    self.draw()
                    #pygame.display.flip()
                cnt += 1
            self.get_gold_apple = False
            self.body_img = self.init_body_img
            #pygame.display.flip()

    # 青りんごを食べた後のスキン
    def skin_effect_af_bad_apple(self):
        #bad face 表示
        if self.color == 1:
            self.face_img = self.__red_bad_face_img
        elif self.color == 2:
            self.face_img = self.__green_bad_face_img
        elif self.color == 3:
            self.face_img = self.__yellow_bad_face_img
        #顔の向き
        if self.directions[1] == 'up':
            self.face_img = pygame.transform.rotate(self.face_img, 0)
        elif self.directions[1] == 'down':
            self.face_img = pygame.transform.rotate(self.face_img, 180)
        elif self.directions[1] == 'right':
            self.face_img = pygame.transform.rotate(self.face_img, -90)
        else:
            self.face_img = pygame.transform.rotate(self.face_img, 90)
        #スキンエフェクト
        cnt = 0
        while cnt < 100:
            #スキンエフェクト 青色
            for i in self.effect_af_bad_apple:
                    self.body_img = i
                    self.draw()
                    #pygame.display.flip()
            cnt += 1
        self.get_gold_apple = False

        #体を元の状態に戻す
        self.face_img = self.init_face_img
        self.body_img = self.init_body_img
        #pygame.display.flip()

    def while_having_bad_apple(self):
        #顔色を変える
        #お顔を整える
        self.face_img = self.__blue_bad_face_img
        if self.directions[1] == 'up':
            self.face_img = pygame.transform.rotate(self.face_img, 0)
        elif self.directions[1] == 'down':
            self.face_img = pygame.transform.rotate(self.face_img, 180)
        elif self.directions[1] == 'right':
            self.face_img = pygame.transform.rotate(self.face_img, -90)
        else:
            self.face_img = pygame.transform.rotate(self.face_img, 90)

    def turn_back_skin_color(self):
        #お顔をもとに戻す
        self.face_img = self.init_face_img
        #お体をもとに戻す
        self.body_img = self.init_body_img
        if self.directions[1] == 'up':
            self.face_img = pygame.transform.rotate(self.face_img, 180)
        elif self.directions[1] == 'down':
            self.face_img = pygame.transform.rotate(self.face_img, 0)
        elif self.directions[1] == 'right':
            self.face_img = pygame.transform.rotate(self.face_img, 90)
        else:
            self.face_img = pygame.transform.rotate(self.face_img, -90)
        #パニック状態の解除
        self.panic = False

    def tongue(self):
        #舌を出すフェクト
        if self.out:
            if self.color == 1:
                self.face_img = self.__red_eating_face_img
            elif self.color == 2:
                self.face_img = self.__green_eating_face_img
            elif self.color == 3:
                self.face_img = self.__yellow_eating_face_img

            if self.directions[1] == 'up':
                self.face_img = pygame.transform.rotate(self.face_img, 0)
            elif self.directions[1] == 'down':
                self.face_img = pygame.transform.rotate(self.face_img, 180)
            elif self.directions[1] == 'right':
                self.face_img = pygame.transform.rotate(self.face_img, -90)
            else:
                self.face_img = pygame.transform.rotate(self.face_img, 90)
        else:
            self.face_img = self.init_face_img
            if self.directions[1] == 'up':
                self.face_img = pygame.transform.rotate(self.face_img, 180)
            elif self.directions[1] == 'down':
                self.face_img = pygame.transform.rotate(self.face_img, 0)
            elif self.directions[1] == 'right':
                self.face_img = pygame.transform.rotate(self.face_img, 90)
            else:
                self.face_img = pygame.transform.rotate(self.face_img, -90)

    def get_score(self):
        #スコアの計算
        #赤りんご x 10
        #青りんご x -5
        #金りんご x 30
        #鳥 x 20
        #カエル x 10
        #セミ x 5
        #ヘビの長さ x 30
        self.__this_score = self.had_apple_cnt * 10 \
                + self.max_length * 30 \
                + self.had_bad_apple_cnt * (-5) \
                + self.had_gold_apple_cnt * 30 \
                + self.had_snake_poop_cnt * (-10) \
                + self.had_frog_cnt * 10 \
                + self.had_cicada_cnt * 5 \
                + self.had_bird_cnt * 20

        return self.__this_score