from board import Board
from disc import Disc
from player import Player
from situation import Situation

board = Board()
rows = board.row  # 座標を示す
wd = Disc("⚪️")
wd.color
bd = Disc("⚫️")
bd.color

situ = Situation()
player1 = Player()


def main():
    print(situ.turn_count)
    print(situ.board)

    color = wd.color

    refreshed_board = player1.move(1, 1, color, board)

    for i in range(len(rows)):
        print(*rows[i])

    situ.turn_count += 1
    situ.reflesh_board(refreshed_board)

    for i in range(len(rows)):
        print(*situ.board.row[i])


if __name__ == "__main__":
    main()
