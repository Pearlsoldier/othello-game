class Rule:
    def __init__(self):
        """
        1.-であること
        2.隣に自分ではない色があること。
        3.２つ以上連続して石があること
        4.連続する石の先が自分の石であること
        """
        pass

    def is_legal_cell(self, row, column, board, opposite_color, current_color) -> bool:
        # 空欄か？
        if not board.row[row][column] == "-":
            return False

        # 空欄じゃないなら、隣に石はあるか？
        if not self.is_adjacent_cells_filled(row, column, board, opposite_color, current_color):
            return False

        # 挟み込めているか？
        return self.is_captured(row, column, board, opposite_color, current_color)

    def is_adjacent_cells_filled(
        self, row, column, board, opposite_color, current_color
    ) -> bool:
        """
        2.置いた隣に相手の色の石がある事。
        """

        omnidirectional_search = [
            (board.row[column][row - 1] == opposite_color),
            (board.row[column + 1][row - 1] == opposite_color),
            (board.row[column + 1][row] == opposite_color),
            (board.row[column + 1][row + 1] == opposite_color),
            (board.row[column][row + 1] == opposite_color),
            (board.row[column - 1][row + 1] == opposite_color),
            (board.row[column - 1][row] == opposite_color),
            (board.row[column - 1][row - 1] == opposite_color),
        ]
        return any(omnidirectional_search)

    def is_flippable_line_directly_above(
        self, row: int, column: int, board, opposite_color, current_color
    ) -> bool:
        """
        True
        真上に相手の石であるとき
        False
        真上に相手の石以外のとき
        """
        i = 1
        while board.row[row - i][column] == opposite_color:
            i += 1
        return board.row[row - i][column] == current_color

    def is_flippable_line_right(
        self, row: int, column: int, board, opposite_color, current_color
    ) -> bool:
        i = 1
        while board.row[row][column + i] == opposite_color:
            i += 1
        return board.row[row][column + i] == current_color

    def is_flippable_line_directly_below(
        self, row: int, column: int, board, opposite_color, current_color
    ) -> bool:
        i = 1
        while board.row[row + i][column] == opposite_color:
            i += 1
        return board.row[row + i][column] == current_color

    def is_flippable_line_left(
        self, row: int, column: int, board, opposite_color, current_color
    ) -> bool:
        i = 1
        while board.row[row][column - i] == opposite_color:
            i += 1
        return board.row[row][column - i] == current_color

    def is_flippable_line_lower_right(
        self, row: int, column: int, board, opposite_color, current_color
    ) -> bool:
        i = 1
        while board.row[row + i][column + i] == opposite_color:
            print(board.row[row + i][column + i])
            i += 1
        return board.row[row + i][column + i] == current_color

    def is_flippable_line_upper_left(
        self, row: int, column: int, board, opposite_color, current_color
    ) -> bool:

        i = 1
        while board.row[row - i][column - i] == opposite_color:
            print(board.row[row - i][column - i])
            i += 1
        return board.row[row - i][column - i] == current_color

    def is_flippable_line_upper_right(
        self, row: int, column: int, board, opposite_color, current_color
    ) -> bool:

        i = 1
        while board.row[row - i][column + i] == opposite_color:
            print(board.row[row - i][column + i])
            i += 1
        return board.row[row - i][column + i] == current_color

    def is_flippable_line_lower_left(
        self, row: int, column: int, board, opposite_color, current_color
    ) -> bool:

        i = 1
        while board.row[row + i][column - i] == opposite_color:
            print(board.row[row + i][column - i])
            i += 1
        return board.row[row + i][column - i] == current_color
    
    def is_captured(self, row, column, board, opposite_color, current_color) -> bool:
        return any([
                    (self.is_flippable_line_directly_above(row, column, board, opposite_color, current_color)),
                    (self.is_flippable_line_upper_right(row, column, board, opposite_color, current_color)),
                    (self.is_flippable_line_right(row, column, board, opposite_color, current_color)),
                    (self.is_flippable_line_lower_right(row, column, board, opposite_color, current_color)),
                    (self.is_flippable_line_directly_below(row, column, board, opposite_color, current_color)),
                    (self.is_flippable_line_lower_left(row, column, board, opposite_color, current_color)),
                    (self.is_flippable_line_left(row, column, board, opposite_color, current_color)),
                    (self.is_flippable_line_upper_left(row, column, board, opposite_color, current_color))
                ] )
