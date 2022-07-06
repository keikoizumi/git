import unittest
import pygame
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from app.creatures_class import Cicada, Bird, Creatures, Frog
from app.utils_class import Utils
import app.const as const

class UtilsTestCase(unittest.TestCase):
        #Util
    def test_is_collision1(self):
        x1, y1, x2, y2 = 0, 0, 0, 0
        self.assertEqual(Utils.is_collision(x1, y1, x2, y2), True)
        x1, y1, x2, y2 = const.SIZE, 0, 1, const.SIZE - 1
        self.assertEqual(Utils.is_collision(x1, y1, x2, y2), True)
        x1, y1, x2, y2 = 0, 0, const.SIZE, const.SIZE
        self.assertEqual(Utils.is_collision(x1, y1, x2, y2), True)
        x1, y1, x2, y2 = const.SIZE, const.SIZE, 0, 0
        self.assertEqual(Utils.is_collision(x1, y1, x2, y2), True)
        x1, y1, x2, y2 = 0, const.SIZE, const.SIZE, 1
        self.assertEqual(Utils.is_collision(x1, y1, x2, y2), True)
        x1, y1, x2, y2 = 0, 0, 1 + const.SIZE, 1 + const.SIZE
        self.assertEqual(Utils.is_collision(x1, y1, x2, y2), False)
        x1, y1, x2, y2 = 0, 0, 10 + const.SIZE, 10 + const.SIZE
        self.assertEqual(Utils.is_collision(x1, y1, x2, y2), False)

    def test_collision_check(self):
        x1, y1 = 0, 0
        list = [[0,0]]
        self.assertEqual(Utils.collision_check(x1, y1, list), True)
        x1, y1 = const.SIZE, 0
        list = [[1, const.SIZE - 1]]
        self.assertEqual(Utils.collision_check(x1, y1, list), True)
        x1, y1 = 0, 0
        list = [[const.SIZE, const.SIZE]]
        self.assertEqual(Utils.collision_check(x1, y1, list), True)
        x1, y1 = const.SIZE, const.SIZE
        list = [[0, 0]]
        self.assertEqual(Utils.collision_check(x1, y1, list), True)
        x1, y1 = 0, const.SIZE
        list = [[const.SIZE, 1]]
        self.assertEqual(Utils.collision_check(x1, y1, list), True)
        x1, y1 = 0, 0
        list = [[1 + const.SIZE, 1 + const.SIZE]]
        self.assertEqual(Utils.collision_check(x1, y1, list), False)
        x1, y1 = 0, 0
        list = [[10 + const.SIZE, 10 + const.SIZE]]
        self.assertEqual(Utils.collision_check(x1, y1, list), False)

parent_screen = None
sut = Creatures(parent_screen)
class CreaturesTestCase(unittest.TestCase):
    def setUp(self):
        # 初期化処理
        pass

    def tearDown(self):
        # 終了処理
        pass

    def test_make1(self):
        bad_apples = [[100, 50]]
        sut.creatures = [[100, 100]]
        sut.make(bad_apples)
        self.assertEqual(sut.is_alive, True)
#
    #def test_make2(self):
    #    bad_apples = [[100, 50],[120, 300]]
    #    sut.make(bad_apples)
    #    self.assertEqual(len(sut.creatures), 3)

    def test_make3(self):
        bad_apples = [[100, 50],[120, 300]]
        sut.make(bad_apples, 5)
        self.assertEqual(len(sut.creatures), 5)

    def test_remove1(self):
        x = 100
        y = 100
        self.assertEqual(sut.remove(x, y), True)
        self.assertEqual(sut.is_alive, True)

    def test_remove2(self):
        x = 10
        y = 10
        self.assertEqual(sut.remove(x, y), False)


parent_screen = pygame.display.set_mode((const.DIP_W, const.DIP_H))
sut = Bird(parent_screen)
class BirdTestCase(unittest.TestCase):
    def setUp(self):
        # 初期化処理
        pass

    def tearDown(self):
        # 終了処理
        pass

    def test_make1(self):
        bad_apples = [[100, 50]]
        sut.creatures = [[100, 100]]
        sut.make(bad_apples, 3)
        self.assertEqual(len(sut.creatures), 3)

    def test_remove1(self):
        x = 100
        y = 100
        self.assertEqual(sut.remove(x, y), True)

    def test_remove2(self):
        x = 10
        y = 10
        self.assertEqual(sut.remove(x, y), False)


parent_screen = pygame.display.set_mode((const.DIP_W, const.DIP_H))
sut = Cicada(parent_screen)
class CicadaTestCase(unittest.TestCase):
    def setUp(self):
        # 初期化処理
        pass

    def tearDown(self):
        # 終了処理
        pass

    def test_make1(self):
        bad_apples = [[100, 50]]
        sut.creatures = [[100, 100]]
        sut.make(bad_apples)
        self.assertEqual(len(sut.creatures), 1)

    def test_remove1(self):
        x = 100
        y = 100
        self.assertEqual(sut.remove(x, y), True)

    def test_remove2(self):
        x = 10
        y = 10
        self.assertEqual(sut.remove(x, y), False)

parent_screen = pygame.display.set_mode((const.DIP_W, const.DIP_H))
sut = Frog(parent_screen)
class FrogTestCase(unittest.TestCase):
    def setUp(self):
        # 初期化処理
        pass

    def tearDown(self):
        # 終了処理
        pass

    def test_make1(self):
        bad_apples = [[100, 50]]
        sut.creatures = [[100, 100]]
        sut.make(bad_apples)
        self.assertEqual(len(sut.creatures), 1)

    def test_remove1(self):
        x = 100
        y = 100
        self.assertEqual(sut.remove(x, y), True)

    def test_remove2(self):
        x = 10
        y = 10
        self.assertEqual(sut.remove(x, y), False)

if __name__ == "__main__":
    unittest.main()