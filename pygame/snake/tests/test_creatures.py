import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from app.creatures_class import Creatures
import app.const as const


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

    def test_make2(self):
        bad_apples = [[100, 50],[120, 300]]
        sut.make(bad_apples)
        self.assertEqual(len(sut.creatures), 3)

    def test_remove1(self):
        x = 100
        y = 100
        self.assertEqual(sut.remove(x, y), True)
        self.assertEqual(sut.is_alive, True)

    def test_remove2(self):
        x = 10
        y = 10
        self.assertEqual(sut.remove(x, y), False)

    def test_is_collision(self):
        x1, y1, x2, y2 = 0, 0, 0, 0
        self.assertEqual(sut.is_collision(x1, y1, x2, y2), True)
        x1, y1, x2, y2 = const.SIZE, 0, 1, const.SIZE - 1
        self.assertEqual(sut.is_collision(x1, y1, x2, y2), True)
        x1, y1, x2, y2 = 0, 0, const.SIZE, const.SIZE
        self.assertEqual(sut.is_collision(x1, y1, x2, y2), True)
        x1, y1, x2, y2 = const.SIZE, const.SIZE, 0, 0
        self.assertEqual(sut.is_collision(x1, y1, x2, y2), True)
        x1, y1, x2, y2 = 0, const.SIZE, const.SIZE, 1
        self.assertEqual(sut.is_collision(x1, y1, x2, y2), True)
        x1, y1, x2, y2 = 0, 0, 1 + const.SIZE, 1 + const.SIZE
        self.assertEqual(sut.is_collision(x1, y1, x2, y2), False)
        x1, y1, x2, y2 = 0, 0, 10 + const.SIZE, 10 + const.SIZE
        self.assertEqual(sut.is_collision(x1, y1, x2, y2), False)

if __name__ == "__main__":
    unittest.main()