import board
import disc


wd = disc.Disc("⚪️")
wd.color
bd = disc.Disc("⚫️")
bd.color

test = board.Board()
test.row[4][4] = wd.color
test.row[4][5] = bd.color
test.row[5][4] = bd.color
test.row[5][5] = wd.color

for i in range(len(test.row)):
    print(*test.row[i])

