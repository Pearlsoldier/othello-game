class Player:

    def __init__(self):
        pass

    def move(self, row, colmun, color, board):
        print(f"player_x🩵: {row}")

        board.row[colmun][row] = color
        return board
