import unittest
from app.creatures_class import Creatures
import traceback

parent_screen = None
sut = Creatures(parent_screen)
class CreaturesTestCase(unittest.TestCase):
    def test_make(self):
        bad_apples = [[100, 50]]
        print(bad_apples)
        self.assertEqual(sut.make(bad_apples),sut.is_alive)
        print(traceback.format_exc())
