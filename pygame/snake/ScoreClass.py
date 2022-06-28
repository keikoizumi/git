import pygame

class Score:
    def __init__(self):
        try:
            f = open('score.txt', 'r')
            self.b_score = f.read()
        finally:
            f.close()

    def write(self, n_score):
        self.n_score = n_score
        f = open('score.txt', 'w')
        try:
            if int(self.n_score) > int(self.b_score):
                f.write(str(self.n_score))
            else:
                f.write(str(self.b_score))
        finally:
            f.close()


