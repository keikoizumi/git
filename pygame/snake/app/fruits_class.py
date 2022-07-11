#external module
import pygame
#Self-made module
from app.utils_class import Utils
import app.const as const


#様々な果物の親クラス
class Fruits:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        # x座標、yを配列で保持
        self.fruits = []
        # 果物が画面上に存在するか否か
        # 存在する場合はTrue
        self.is_alive = False
        # 画像を読み込む
        self.image = None
    # 果物を作成
    def make(self, bad_apples, number = 1):
        # 果物を生存状態にする
        self.is_alive = True
        # 新しい果物を作る
        if number == 1:
            self.x , self.y = Utils.make_new_x_y()
            # 青りんごと新しい果物のX、Y座標が重なっていないか確認
            Utils.check(self.x, self.y, bad_apples)
            # 果物のみ果物配列に追加
            self.fruits.append([self.x, self.y])
        else:
            for i in range(number -  1):
                self.x , self.y = Utils.make_new_x_y()
                # 青りんごと新しい果物のX、Y座標が重なっていないか確認
                Utils.check(self.x, self.y, bad_apples)
                # 果物のみ果物配列に追加
                self.fruits.append([self.x, self.y])
    # 果物をランダムな位置に移動させる
    def move(self, bad_apples):
        self.x , self.y = Utils.make_new_x_y()
        # 青りんごと新しい果物のX、Y座標が重なっていないか確認
        for i in bad_apples:
            x2 = i[0]
            y2 = i[1]
            while Utils.is_collision(self.x, self.y, x2, y2):
                self.x , self.y = Utils.make_new_x_y()
        self.draw()
    # 果物とヘビが衝突した場合、衝突した果物を削除
    # 削除した場合はTrue、してない場合はFalse
    def remove(self, x1, y1):
        no = 0
        for i in self.fruits:
            x2 = i[0]
            y2 = i[1]
            #ヘビの頭とぶつかった果物を削除
            if Utils.is_collision(x1, y1, x2, y2):
                    #ぶつかったBADりんごを削除
                    del self.fruits[no]
                    return True
            no += 1
        return False
    # 果物を描画する
    def draw(self, target_list):
        #配列の数分描画
        for i in target_list:
            self.x = i[0]
            self.y = i[1]
            self.parent_screen.blit(self.image, (self.x, self.y))

#赤りんごクラス
class Apple(Fruits):
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        # x座標、yを配列で保持
        self.fruits = [
            [int(const.DIP_W / 4), int(const.DIP_H / 4)]
            ,[int(const.DIP_W / 2), int(const.DIP_H / 4)]
        ]
        # 果物が画面上に存在するか否か
        # 存在する場合はTrue
        self.is_alive = True
        # 画像を読み込む
        self.image = pygame.image.load(const.APPLE_IMG_PATH).convert()
    # 果物を作成
    def make(self, bad_apples, number = 1):
        # 果物を生存状態にする
        self.is_alive = True
        # 新しい果物を作る
        if number == 1:
            self.x , self.y = Utils.make_new_x_y()
            # 青りんごと新しい果物のX、Y座標が重なっていないか確認
            Utils.check(self.x, self.y, bad_apples)
            # 果物のみ果物配列に追加
            self.fruits.append([self.x, self.y])
        else:
            for i in range(number - 1):
                self.x , self.y = Utils.make_new_x_y()
                # 青りんごと新しい果物のX、Y座標が重なっていないか確認
                Utils.check(self.x, self.y, bad_apples)
                # 果物のみ果物配列に追加
                self.fruits.append([self.x, self.y])
    # 果物をランダムな位置に移動させる
    #def move(self, bad_apples):
    #    super().move(bad_apples)
    # 果物とヘビが衝突した場合、衝突した果物を削除
    # 削除した場合はTrue、してない場合はFalse
    def remove(self, x1, y1):
        no = 0
        for i in self.fruits:
            x2 = i[0]
            y2 = i[1]

            #ヘビの頭とぶつかった果物を削除
            if Utils.is_collision(x1, y1, x2, y2):
                    #ぶつかったりんごを削除
                    del self.fruits[no]
            no += 1

    def draw(self):
        for i in self.fruits:
            self.x = i[0]
            self.y = i[1]
            self.parent_screen.blit(self.image, (self.x, self.y))

    def make_init(self):
        self.fruits.append([int(const.DIP_W / 4), int(const.DIP_H / 4)])
        self.fruits.append([int(const.DIP_W / 2), int(const.DIP_H / 4)])
        self.draw()

#青りんごクラス
class BadApple(Fruits):
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        # x座標、yを配列で保持
        self.fruits = []
        # 果物が画面上に存在するか否か
        # 存在する場合はTrue
        self.is_alive = False
        # 画像を読み込む
        self.image = pygame.image.load(const.BAD_APPLE_IMG_PATH).convert()
    # 果物を作成
    def make(self, bad_apples, number = 1):
        # 果物を生存状態にする
        self.is_alive = True
        # 新しい果物を作る
        if number == 1:
            self.x , self.y = Utils.make_new_x_y()
            # 青りんごと新しい果物のX、Y座標が重なっていないか確認
            Utils.check(self.x, self.y, bad_apples)
            # 果物のみ果物配列に追加
            self.fruits.append([self.x, self.y])
        else:
            for i in range(number - 1):
                self.x , self.y = Utils.make_new_x_y()
                # 青りんごと新しい果物のX、Y座標が重なっていないか確認
                Utils.check(self.x, self.y, bad_apples)
                # 果物のみ果物配列に追加
                self.fruits.append([self.x, self.y])

    # 果物をランダムな位置に移動させる
    #def move(self, bad_apples):
    #    super().move(bad_apples)
    # 果物とヘビが衝突した場合、衝突した果物を削除
    # 削除した場合はTrue、してない場合はFalse
    def remove(self, x1, y1, number = 1):
        #指定された個数消す
        if number != 1:
            try:
                if len(self.fruits) < number:
                    for i in range(len(self.fruits)):
                        del self.fruits[i]
                else:
                    for i in range(0, number - 1, 1):
                        del self.fruits[i]
            except IndexError as e:
                print('Fruits Bad Apple IndexError')
        else:
            no = 0
            for i in self.fruits:
                x2 = i[0]
                y2 = i[1]
                #ヘビの頭とぶつかった果物を削除
                if Utils.is_collision(x1, y1, x2, y2):
                        #ぶつかったBADりんごを削除
                        del self.fruits[no]
                no += 1

    def draw(self):
        for i in self.fruits:
            self.x = i[0]
            self.y = i[1]
            self.parent_screen.blit(self.image, (self.x, self.y))

#金りんごクラス
class GoldApple(Fruits):
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        # x座標、yを配列で保持
        self.fruits = []
        # 果物が画面上に存在するか否か
        # 存在する場合はTrue
        self.is_alive = False
        # 画像を読み込む
        self.image = pygame.image.load(const.GOLD_APPLE_IMG_PATH).convert()
    # 果物を作成
    def make(self, bad_apples, number = 1):
        # 果物を生存状態にする
        self.is_alive = True
        # 新しい果物を作る
        if number == 1:
            self.x , self.y = Utils.make_new_x_y()
            # 青りんごと新しい果物のX、Y座標が重なっていないか確認
            Utils.check(self.x, self.y, bad_apples)
            # 果物のみ果物配列に追加
            self.fruits.append([self.x, self.y])
        else:
            for i in range(number - 1):
                self.x , self.y = Utils.make_new_x_y()
                # 青りんごと新しい果物のX、Y座標が重なっていないか確認
                Utils.check(self.x, self.y, bad_apples)
                # 果物のみ果物配列に追加
                self.fruits.append([self.x, self.y])
    # 果物をランダムな位置に移動させる
    def move(self, bad_apples):
        super().move(bad_apples)
    # 果物とヘビが衝突した場合、衝突した果物を削除
    # 削除した場合はTrue、してない場合はFalse
    def remove(self, x1, y1):
        if super().remove(x1, y1):
            return True
        return False
    def draw(self):
        super().draw(self.fruits)
