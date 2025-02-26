from disc import Disc
import string

wd = Disc("⚪️")
wd.color
bd = Disc("⚫️")
bd.color

uppercase_letter = list(string.ascii_uppercase)
line = uppercase_letter[0:8]


class Board:
    """
    10*10のマスを用意
    内側の8*8を盤面
    X行: A-H ([0]行目[9]行目)
    Y行: 1-8
    """

    def __init__(self):
        self.row = []
        x = 10
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

        zero_line[1:9] = alphabet_string
        self.row[0] = zero_line
        self.row[9] = zero_line

        self.row[4][3] = wd.color
        self.row[4][4] = wd.color
        self.row[4][5] = wd.color
        self.row[6][3] = wd.color
        self.row[6][4] = wd.color
        self.row[6][5] = wd.color
        self.row[5][3] = wd.color
        self.row[5][5] = wd.color

        self.row[3][3] = bd.color
        self.row[3][4] = bd.color
        self.row[3][5] = bd.color
        self.row[3][3] = bd.color
        self.row[3][2] = bd.color
        self.row[3][6] = bd.color

        self.row[7][3] = bd.color
        self.row[7][4] = bd.color
        self.row[7][5] = bd.color
        self.row[7][3] = bd.color
        self.row[7][2] = bd.color
        self.row[7][6] = bd.color

        self.row[4][2] = bd.color
        self.row[5][2] = bd.color
        self.row[6][2] = bd.color

        self.row[4][6] = bd.color
        self.row[5][6] = bd.color
        self.row[6][6] = bd.color
      

        
       
