class Player:

    def __init__(self):
        pass

    def move(self, x, y, color, board):
        print(f"player_x🩵: {x}")

        board.row[x][y] = color
        return board
