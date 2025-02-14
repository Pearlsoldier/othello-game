import board
import disc

test = board.Board()
wd = disc.Disc("White")

print(*test.row, sep="\n")
print(wd.coler("⚪️"))