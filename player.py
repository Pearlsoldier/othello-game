class Player:

    def __init__(self):
        pass

    def move(self, x, y, color, board):

        board.row[x][y] = color
        return board
