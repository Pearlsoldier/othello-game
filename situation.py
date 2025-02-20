class Situation:
    
    """
    盤面の情報を持つクラス(list)
    ターン情報(int)：何ターン目か
    is_black_turn → bool 先手黒/後手白
    """

    def __init__(self):
        self.turn_count = 0
        self.board = []
        self.ALP_NUM_MAP = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}

    def refresh_board(self, refreshed_board):
        self.board = refreshed_board

    def put_disc(self, cell):
        self.disc_move = cell
        splitted_row = self.disc_move.split()
        str_x = splitted_row[0]
        x = self.ALP_NUM_MAP[str_x]
        str_y = splitted_row[1]
        y = int(str_y)

        return x, y

    @property
    def is_black_turn(self) -> bool:
        return self.turn_count % 2 == 1
