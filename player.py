class Player:

    def __init__(self):
        pass

    def move(self, row, colmun, color, board):

        board.row[colmun][row] = color
        return board
