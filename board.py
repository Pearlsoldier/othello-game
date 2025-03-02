from disc import Disc
import string

wd = Disc("⚪️")
wd.color
bd = Disc("⚫️")
bd.color

uppercase_letter = list(string.ascii_uppercase)
line = uppercase_letter[0:3]


class Board:
    """
    10*10のマスを用意
    内側の8*8を盤面
    X行: A-H ([0]行目[9]行目)
    Y行: 1-8
    """

    def __init__(self):
        self.row = []
        x = 5
        for i in range(x):
            self.row.append([])
            for j in range(x):
                self.row[i].append("-")
                self.row[i][0] = i
            for t in range(x):
                self.row[i][j] = i

        zero_line = []
        for i in range(x):
            zero_line.append(0)

        alphabet_string = []
        for j in range(len(line)):
            alphabet_string.append(line[j])

        zero_line[1:4] = alphabet_string
        self.row[0] = zero_line
        self.row[4] = zero_line

        self.row[1][1] = bd.color
        self.row[1][2] = bd.color
        self.row[1][3] = wd.color


        self.row[2][1] = bd.color
        self.row[2][2] = bd.color
        self.row[2][3] = wd.color
        self.row[3][1] = bd.color
        self.row[3][2] = bd.color
        self.row[3][3] = wd.color

        self.row[4][1] = bd.color
        self.row[4][2] = bd.color
        self.row[4][3] = wd.color