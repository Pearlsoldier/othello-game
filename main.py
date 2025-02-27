from board import Board
from disc import Disc
from player import Player
from situation import Situation
from rule import Rule


def main():
    bd = Disc("⚫️")
    wd = Disc("⚪️")
    board = Board()
    rows = board.row
    situ = Situation()
    player = Player()
    rules = Rule()

    print("オセロを始めます。")
    print("======================")
    for i in range(len(rows)):
        print(*rows[i])
    print("======================")
    while situ.turn_count < 64:
        situ.turn_count += 1
        if situ.is_black_turn:
            current_color = bd.color  # 現在の色
            opposite_color = wd.color  # 相手（反対）の色
            print(f"先手,{current_color}。")
        else:
            current_color = wd.color
            opposite_color = bd.color
            print(f"後手,{current_color}。")

        column, row = situ.put_disc(input())
        if rules.is_legal_cell(row, column, board, opposite_color, current_color):
            refreshed_board = player.move(
                column=column, row=row, current_color=current_color, board=board
            )
            situ.reflesh_board(refreshed_board)
            for i in range(len(rows)):
                print(*rows[i])
            print("======================")
            refreshed_board = player.omnidirectional_flip(
                column=column,
                row=row,
                current_color=current_color,
                opposite_color=opposite_color,
                board=board,
            )
            situ.reflesh_board(refreshed_board)
            for i in range(len(rows)):
                print(*rows[i])
            print("======================")


        else:
            while not rules.is_legal_cell(
                row, column, board, opposite_color, current_color
            ):
                print(f"❌手 {column, row} は石を置けません❌")
                print("もう一度入力してください！！")
                for i in range(len(rows)):
                    print(*rows[i])
                print("======================")
                column, row = situ.put_disc(input())

            print(f"🙆手 {column, row} は有効です🙆")
            refreshed_board = player.move(
                column=column, row=row, current_color=current_color, board=board
            )
            situ.reflesh_board(refreshed_board)

            refreshed_board = player.omnidirectional_flip(
                column=column,
                row=row,
                current_color=current_color,
                opposite_color=opposite_color,
                board=board,
            )
            situ.reflesh_board(refreshed_board)
            for i in range(len(rows)):
                print(*rows[i])
            print("======================")
            continue
    print("ゲーム終了")


if __name__ == "__main__":
    main()
