import string

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

        for _ in self.row:
            self.row
