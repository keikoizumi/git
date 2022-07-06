import random

#external module
import pygame

#Self-made module
import app.const as const

#共通クラス
class Utils:
    # 新しいconst.SIZEpx × const.SIZEpxと既存の
    # const.SIZEpx × const.SIZEpxが重なっていないか確認
    # 戻り値: 重なりがる場合 True, 重ならない場合 False
    def is_collision(x1, y1, x2, y2):
        if ((x1 <= x2 + const.SIZE and y1 <= y2 + const.SIZE)
            and (x2 <= x1 + const.SIZE and y1 <= y2 + const.SIZE)
            and (x1 <= x2 + const.SIZE and y2 <= y1 + const.SIZE)
            and (x2 <= x1 + const.SIZE and y2 <= y1 + const.SIZE)):
            return True
        else:
            return False

    # 既存のリストと既存の
    # const.SIZEpx × const.SIZEpxが重なっていないか確認
    # 重なりがある場合はTrue、重ならない場合はFalse
    def collision_check(x1, y1, target_list):
        for i in target_list:
            x2 = i[0]
            y2 = i[1]
            if Utils.is_collision(x1, y1, x2, y2):
                return True
        return False

    # 新しいX座標、Y座標を作成する
    def make_new_x_y():
        x = random.randint(const.SIZE, const.DIP_W - const.SIZE)
        y = random.randint(const.SIZE, const.DIP_H - const.SIZE)
        return x, y

    # 新しいconst.SIZEpx × const.SIZEpxと既存の
    # const.SIZEpx × const.SIZEpxが重なっていないか確認
    # 重なりがある場合は再作成を行う
    # 重ならないx、yを返却
    def check(x1, y1, target_list):
        for i in target_list:
            x2 = i[0]
            y2 = i[1]
            # 重なりがある場合は再作成
            while Utils.is_collision(x1, y1, x2, y2):
                x1 , y1 = Utils.make_new_x_y()
        return x1 , y1
