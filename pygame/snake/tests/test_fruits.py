import unittest
import pygame
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from app.fruits_class import Fruits ,Apple, BadApple, GoldApple
#from app.utils_class import Utils
import app.const as const


parent_screen = None
sut = Fruits(parent_screen)
class FruitsTestCase(unittest.TestCase):
    def setUp(self):
        # 初期化処理
        pass

    def tearDown(self):
        # 終了処理
        pass

    def test_make1(self):
        bad_apples = [[100, 50]]
        sut.fruits = [[100, 100]]
        print(sut.fruits)
        sut.make(bad_apples)
        self.assertEqual(sut.is_alive, True)

    def test_make3(self):
        bad_apples = [[100, 50],[120, 300]]
        sut.make(bad_apples, 5)
        self.assertEqual(len(sut.fruits), 5)

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
sut = Apple(parent_screen)
class AppleTestCase(unittest.TestCase):
    def setUp(self):
        # 初期化処理
        pass

    def tearDown(self):
        # 終了処理
        pass

    def test_make1(self):
        bad_apples = [[100, 50]]
        sut.fruits = [[100, 100]]
        sut.make(bad_apples)
        self.assertEqual(len(sut.fruits), 1)

    def test_remove1(self):
        x = 100
        y = 100
        self.assertEqual(sut.remove(x, y), True)

    def test_remove2(self):
        x = 10
        y = 10
        self.assertEqual(sut.remove(x, y), False)

parent_screen = pygame.display.set_mode((const.DIP_W, const.DIP_H))
sut = BadApple(parent_screen)
class BadAppleTestCase(unittest.TestCase):
    def setUp(self):
        # 初期化処理
        pass

    def tearDown(self):
        # 終了処理
        pass

    def test_make1(self):
        bad_apples = [[100, 50]]
        sut.fruits = [[100, 100]]
        sut.make(bad_apples)
        self.assertEqual(len(sut.fruits), 1)

    def test_remove1(self):
        x = 100
        y = 100
        self.assertEqual(sut.remove(x, y), True)

    def test_remove2(self):
        x = 10
        y = 10
        self.assertEqual(sut.remove(x, y), False)

parent_screen = pygame.display.set_mode((const.DIP_W, const.DIP_H))
sut = GoldApple(parent_screen)
class GoldAppleTestCase(unittest.TestCase):
    def setUp(self):
        # 初期化処理
        pass

    def tearDown(self):
        # 終了処理
        pass

    def test_make1(self):
        bad_apples = [[100, 50]]
        sut.fruits = [[100, 100]]
        sut.make(bad_apples)
        self.assertEqual(len(sut.fruits), 1)

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