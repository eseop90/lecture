from board import Board
from player import Player


player = Player('O')

board = Board()
board.print_board_nums()

while True:
    player.move_player(board=board)
    board.print_board()