class Player:

    def __init__(self):
        pass

    def move(self, column, row, current_color, board):
        board.row[row][column] = current_color
        return board
    
    def flip_turn_directly_above(self, column, row, board, current_color):
        board.row[row - 1][column] = current_color
        return board
    
    def flip_turn_right(self, column, row, board, current_color):
        board.row[row][column + 1] = current_color
        return board
    
    def flip_turn__directly_below(self, column, row, board, current_color):
        board.row[row + 1][column] = current_color
        return board
    
    def flip_turn_left(self, column, row, board, current_color):
        board.row[row][column - 1] = current_color
        return board