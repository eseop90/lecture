class Player:
    def __init__(self, letter):
        self.letter = letter

    def move_player(self, board):
        val = int(input(self.letter + '\'s turn. Input move (0-9): '))
        board.board[val] = self.letter