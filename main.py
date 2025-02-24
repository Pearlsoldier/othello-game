from board import Board
from disc import Disc
from player import Player
from situation import Situation
from rule import Rule

board = Board()
rows = board.row  # 座標を示す
wd = Disc("⚪️")
wd.color
bd = Disc("⚫️")
bd.color

situ = Situation()
player = Player()
rules = Rule()


def main():
    print("オセロを始めます。")
    for i in range(len(rows)):
        print(*rows[i])
    for i in range(1, 61):
        situ.turn_count += 1
        if situ.is_black_turn:
            color = bd.color
            print(f"先手,{color}。")
        else:
            color = wd.color
            print(f"後手,{color}。")

        row, column = situ.put_disc(input())
        is_legal = rules.is_legal_cell(row, column, board)

        if is_legal:
            is_legal = rules.is_adjacent_cells_filled(
                row, column, board, color
                )
            if is_legal:
                refreshed_board = player.move(row, column, color, board)
                situ.reflesh_board(refreshed_board)
                for i in range(len(rows)):
                    print(*rows[i])
            else:
                while not is_legal:
                    print(f"❌手 {row, column} は石を置けません❌")
                    print("もう一度入力してください！！")
                    for i in range(len(rows)):
                        print(*rows[i])
                    row, column = situ.put_disc(input())
                    if rules.is_legal_cell(row, column, board):
                        is_legal = rules.is_adjacent_cells_filled(
                            row, column, board, color
                        )
                    print(f"ac :{is_legal}")
                    if is_legal:
                        print(f"🙆手 {row, column} は有効です🙆")
                        refreshed_board = player.move(row, column, color, board)
                        situ.reflesh_board(refreshed_board)
                        for i in range(len(rows)):
                            print(*rows[i])
                        continue

        else:
            while not is_legal:
                print(f"❌手 {row, column} は石を置けません❌")
                print("もう一度入力してください！！")
                for i in range(len(rows)):
                    print(*rows[i])
                row, column = situ.put_disc(input())
                if rules.is_legal_cell(row, column, board):
                    is_legal = rules.is_adjacent_cells_filled(row, column, board, color)
                print(f"ac :{is_legal}")
                if is_legal:
                    print(f"🙆手 {row, column} は有効です🙆")
                    refreshed_board = player.move(row, column, color, board)
                    situ.reflesh_board(refreshed_board)
                    for i in range(len(rows)):
                        print(*rows[i])
                    continue


if __name__ == "__main__":
    main()
