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
    is_blank_place = rules.is_placeable(board)
    print(is_blank_place)
    print("======================")
    for i in range(len(rows)):
        print(*rows[i])
    print("======================")
    while situ.turn_count < 61:
        situ.turn_count += 1
        if situ.is_black_turn:
            current_color = bd.color 
            opposite_color = wd.color
            print(f"先手,{current_color}。")
        else:
            current_color = wd.color
            opposite_color = bd.color
            print(f"後手,{current_color}。")

        column, row = situ.put_disc(input())
        print(rules.is_flippable_line_right(row, column, board, opposite_color, current_color))
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
    print("ゲーム終了")


if __name__ == "__main__":
    main()
