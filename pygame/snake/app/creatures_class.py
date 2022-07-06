#Standard module
import random

#external module
import pygame

#Self-made module
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
    def make(self, bad_apples):
        # 生き物を生存状態にする
        self.is_alive = True
        # 新しい生き物を作る
        self.x , self.y = Utils.make_new_x_y()
        # 青りんごと新しい生き物のX、Y座標が重なっていないか確認
        Utils.check(self.x, self.y, bad_apples)
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
        no = 1
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
    def make(self, bad_apples):
        super().make(bad_apples)
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
    def make(self, bad_apples):
        super().make(bad_apples)
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
    def make(self, bad_apples):
        super().make(bad_apples)
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