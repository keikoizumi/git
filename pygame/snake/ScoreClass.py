import pygame

class Score:
    def __init__(self):
        f = open('score.txt', 'r')

        self.b_score = f.read()

        f.close()

    def write(self, n_score):
        f = open('score.txt', 'w')
        if type(self.b_score) is not int:
            self.b_score = 0
        print(type(self.b_score))
        print(self.b_score)
        if int(n_score) > int(self.b_score):
            f.write(str(n_score))
            self.b_score = n_score
        else:
            f.write(str(self.b_score))

        f.close()


