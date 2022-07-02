import const

class Score:
    def __init__(self):
        try:
            f = open(const.SCORE_FILE_PATH, 'r')
        except FileNotFoundError as e:
            print(f'ファイルが開けない: {e}')
        else:
            self.b_score = f.read()
        finally:
            f.close()

    def write(self, n_score):
        self.n_score = n_score
        try:
            f = open(const.SCORE_FILE_PATH, 'w')
            if int(self.n_score) > int(self.b_score):
                pass
        except (FileNotFoundError, ValueError) as e:
            f.write('1')
            print(f'ファイルの書き込みでエラー: {e}')
        else:
            if int(self.n_score) > int(self.b_score):
                f.write(str(self.n_score))
            else:
                f.write(str(self.b_score))
        finally:
            f.close()


