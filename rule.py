class Rule:
    def __init__(self):
        """
        1.-であること
        2.隣に自分ではない色があること。
        3.２つ以上連続して石があること
        4.連続する石の先が自分の石であること
        """
        pass

    def is_legal_cell(self, row: int, column: int, board) -> bool:
        """
        1.-であること
        石が置けるブランク状態かの判定
        """
        if board.row[row][column] == "-":
            return True



    def is_adjacent_cells_filled(self, row: int, column: int, board, color) -> bool:
        if (
            not (board.row[column][row - 1] == color)
            or not (board.row[column + 1][row - 1] == color)
            or not (board.row[column + 1][row] == color)
            or not (board.row[column + 1][row + 1] == color)
            or not (board.row[column][row + 1] == color)
            or not (board.row[column - 1][row + 1] == color)
            or not (board.row[column - 1][row] == color)
            or not (board.row[column - 1][row - 1] == color)
        ):
            if (
                not (board.row[column][row - 1] == "-")
                or not (board.row[column + 1][row - 1] == "-")
                or not (board.row[column + 1][row] == "-")
                or not (board.row[column + 1][row + 1] == "-")
                or not (board.row[column][row + 1] == "-")
                or not (board.row[column - 1][row + 1] == "-")
                or not (board.row[column - 1][row] == "-")
                or not (board.row[column - 1][row - 1] == "-")
            ):
                return True
            else:
                return False
        else:
            return False

            """
            2.隣に自分ではない色があること。
            """
            return  not ((board.row[column][row] == color) and (board.row[i][row] == "-"))
            


    def is_valid_flank_capture(self, row: int, column: int, board, color) -> bool:
        """
        1方向に対して挟み込み捕獲が有効かどうかの判定
        行（列）末まで確認する。
        置いた位置から、石が連続しているか
        最後の石が自分の石か
        途中で - があれば、判定はFalseになる。
        """
        pass
        