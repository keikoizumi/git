#external module
import pygame

#Self-made module
import const

#様々な果物の親クラス
class Grass:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen