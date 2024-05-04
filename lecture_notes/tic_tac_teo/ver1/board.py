import math

class Board():
    def __init__(self):
        self.board = self.make_board()

    def make_board(self):
        return [' ' for _ in range(9)]
    
    def print_board(self):
        for i in range(3):
            row = self.board[i*3:(i+1)*3]
            print('| ' + ' | '.join(row) + ' |')

    def print_board_nums(self):
        # 0 | 1 | 2
        num_tmp = [0, 1, 2]
        for i in range(3):
            row = [str(_num + (i*3)) for _num in num_tmp]
            print('| ' + ' | '.join(row) + ' |')