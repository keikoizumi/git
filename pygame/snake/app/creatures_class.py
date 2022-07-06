#Standard module
from ctypes.wintypes import SIZE
import random

#external module
import pygame

#Self-made module
import app.const as const

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
        self.make_new_x_y()
        # 青りんごと新しい生き物のX、Y座標が重なっていないか確認
        self.check(bad_apples)
        # 生き物のみ生き物配列に追加
        self.creatures.append([self.x, self.y])
    # 生き物をランダムな位置に移動させる
    def move(self, bad_apples):
        self.self.make_new_x_y()
        # 青りんごと新しい生き物のX、Y座標が重なっていないか確認
        for i in bad_apples:
            x2 = i[0]
            y2 = i[1]
            while self.is_collision(self.x, self.y, x2, y2):
                self.make_new_x_y()
        self.draw()
    # 生き物とヘビが衝突した場合、衝突した生き物を削除
    # 削除した場合はTrue、してない場合はFalse
    def remove(self, x1, y1):
        no = 1
        for i in self.creatures:
            x2 = i[0]
            y2 = i[1]
            #ヘビの頭とぶつかった生き物を削除
            if self.is_collision(x1, y1, x2, y2):
                    #ぶつかったBADりんごを削除
                    del self.creatures[no]
                    return True
            no += 1
        return False
    # 生き物を描画する
    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
    # 新しい生き物const.SIZEpx × const.SIZEpxと既存の
    # 青りんごconst.SIZEpx × const.SIZEpxが重なっていないか確認
    def check(self, bad_apples):
        for i in bad_apples:
            x2 = i[0]
            y2 = i[1]
            # 重なりがある場合は再作成
            while self.is_collision(self.x, self.y, x2, y2):
                self.make_new_x_y()
    # 新しい生き物const.SIZEpx × const.SIZEpxと既存の
    # 青りんごconst.SIZEpx × const.SIZEpxが重なっていないか確認
    # 戻り値: 重なりがる場合 True, 重ならない場合 False
    # TODO:Utilに実装
    def is_collision(self,x1, y1, x2, y2):
        if ((x1 <= x2 + const.SIZE and y1 <= y2 + const.SIZE)
            and (x2 <= x1 + const.SIZE and y1 <= y2 + const.SIZE)
            and (x1 <= x2 + const.SIZE and y2 <= y1 + const.SIZE)
            and (x2 <= x1 + const.SIZE and y2 <= y1 + const.SIZE)):
            return True
        else:
            return False

    # 新しいX座標、Y座標を作成する
    # TODO:Utilに実装
    def make_new_x_y(self):
        self.x = random.randint(const.SIZE, const.DIP_W - const.SIZE)
        self.y = random.randint(const.SIZE, const.DIP_H - const.SIZE)
