class Situation:
    """
    盤面の情報を持つクラス(list)
    ターン情報(int)：何ターン目か
    is_black_turn → bool 先手黒/後手白
    """

    def __init__(self):
        self.turn_count = 0
        self.board = []
        self.alp_num_map = {
            "a": 1,
            "b": 2,
            "c": 3,
            "d": 4,
            "e": 5,
            "f": 6,
            "g": 7,
            "h": 8,
        }

    def reflesh_board(self, refleshed_board):
        self.board = refleshed_board

    def put_disc(self, cell):
        self.disc_move = cell
        splitted_row = self.disc_move.split()
        print(f"splitted_row :{splitted_row}")
        str_x = splitted_row[0]
        row = self.alp_num_map[str_x]
        str_y = splitted_row[1]
        column = int(str_y)
        print(f"put_x🩵: {row}")

        return row, column

    @property
    def is_black_turn(self) -> bool:
        return self.turn_count % 2 == 1
