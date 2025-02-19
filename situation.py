from board import Board
from disc import Disc
from player import Player


class Situation:
    """
    盤面の情報を持つクラス(list)
    ターン情報(int)：何ターン目か
    is_black_turn → bool 先手黒/後手白
    """

    def __init__(self):
        self.turn_count = 0
        self.board = []
        self.is_black_turn = True

    def reflesh_board(self, refleshed_board):
        self.board = refleshed_board
