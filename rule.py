class Rule:
    def __init__(self):
        pass

    def is_legal_cell(self, row: int, column: int, board) -> bool:
        return board.row[row][column] == "-"

    def flip_line(self):

        pass

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
