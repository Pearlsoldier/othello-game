from rule import Rule


class Player:

    def __init__(self):
        pass

    def move(self, column, row, current_color, board):
        board.row[row][column] = current_color
        return board
    
    def omnidirectional_flip(self, column, row, board, current_color, opposite_color):
        self.flip_turn_directly_above(column, row, board, current_color, opposite_color),
        self.flip_turn_directly_below(column, row, board, current_color, opposite_color),
        self.flip_turn_left(column, row, board, current_color, opposite_color),
        self.flip_turn_lower_left(column, row, board, current_color, opposite_color),
        self.flip_turn_lower_right(column, row, board, current_color, opposite_color),
        self.flip_turn_right(column, row, board, current_color, opposite_color),
        self.flip_turn_upper_left(column, row, board, current_color, opposite_color),
        self.flip_turn_upper_righ(column, row, board, current_color, opposite_color),

    def flip_turn_directly_above(self, column, row, board, current_color, opposite_color):
        rules = Rule()
        if rules.is_flippable_line_directly_above(row, column, board, opposite_color, current_color):
            i = 1
            while board.row[row - i][column] == opposite_color:
                board.row[row - i][column] = current_color
                i += 1
        return board
    
    def flip_turn_right(self, column, row, board, current_color, opposite_color):
        rules = Rule()
        if rules.is_flippable_line_right(row, column, board, opposite_color, current_color):
            i = 1
            while board.row[row][column + i] == opposite_color:
                board.row[row][column + i] = current_color
                i += 1
            return board
    
    def flip_turn_directly_below(self, column, row, board, current_color, opposite_color):
        rules = Rule()
        if rules.is_flippable_line_directly_below(row, column, board, opposite_color, current_color):
            i = 1
            while board.row[row + i][column] == opposite_color:
                board.row[row + i][column] = current_color
                i += 1
        return board
    
    def flip_turn_left(self, column, row, board, current_color, opposite_color):
        rules = Rule()
        if rules.is_flippable_line_left(row, column, board, opposite_color, current_color):
            i = 1
            while board.row[row][column - i] == opposite_color:
                board.row[row][column - i] = current_color
                i += 1
        return board
    
    def flip_turn_lower_right(self, column, row, board, current_color, opposite_color):
        rules = Rule()
        if rules.is_flippable_line_lower_right(row, column, board, opposite_color, current_color):
            i = 1
            while board.row[row + i][column + i] == opposite_color:
                board.row[row + i][column + i] = current_color
                i += 1
        return board
    
    def flip_turn_upper_left(self, column, row, board, current_color, opposite_color):
        rules = Rule()
        if rules.is_flippable_line_upper_left(row, column, board, opposite_color, current_color):
            i = 1
            while board.row[row - i][column - i] == opposite_color:
                board.row[row - i][column - i] = current_color
                i += 1
        return board
    
    def flip_turn_upper_righ(self, column, row, board, current_color, opposite_color):
        rules = Rule()
        if rules.is_flippable_line_upper_right(row, column, board, opposite_color, current_color):
            i = 1
            while board.row[row - i][column + i] == opposite_color:
                board.row[row - i][column + i] = current_color
                i += 1
        return board
    
    def flip_turn_lower_left(self, column, row, board, current_color, opposite_color):
        rules = Rule()
        if rules.is_flippable_line_right(row, column, board, opposite_color, current_color):
            i = 1
            while board.row[row + i][column - i] == opposite_color:
                board.row[row + i][column - i] = current_color
                i += 1
        return board