from pegSolitaire import Board, solve_recursive
import pickle

this = Board()
print(this.board)


class BoardData(object):
    def __init__(self, board: Board) -> None:
        self.initBoard = board
