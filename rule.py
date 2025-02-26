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

    def is_adjacent_cells_filled(
        self, row: int, column: int, board, opposite_color
    ) -> bool:
        """
        2.置いた隣に相手の色の石がある事。
        """
        if (
            (board.row[column][row - 1] == opposite_color)
            or (board.row[column + 1][row - 1] == opposite_color)
            or (board.row[column + 1][row] == opposite_color)
            or (board.row[column + 1][row + 1] == opposite_color)
            or (board.row[column][row + 1] == opposite_color)
            or (board.row[column - 1][row + 1] == opposite_color)
            or (board.row[column - 1][row] == opposite_color)
            or (board.row[column - 1][row - 1] == opposite_color)
        ):
            return True
        else:
            return False

    def is_valid_flank_capture_directly_above(self, row: int, column: int, board, current_color, opposite_color) -> bool:
        return (board.row[row - 1][column] == opposite_color) and (board.row[row - 2][column] == current_color)
    
    def is_valid_flank_capture_right(self, row: int, column: int, board, current_color, opposite_color) -> bool:
        return (board.row[row][column + 1] == opposite_color) and (board.row[row][column + 2] == current_color)
    
    def is_valid_flank_capture_directly_below(self, row: int, column: int, board, current_color, opposite_color) -> bool:
        return (board.row[row + 1][column] == opposite_color) and (board.row[row + 2][column] == current_color)
    
    def is_valid_flank_capture_left(self, row: int, column: int, board, current_color, opposite_color) -> bool:
        return (board.row[row][column - 1] == opposite_color) and (board.row[row][column - 2] == current_color)


        
