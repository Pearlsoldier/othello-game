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
    for i in range(1, 61):
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
        is_legal = (rules.is_legal_cell(row, column, board) and (rules.is_adjacent_cells_filled(row, column, board, opposite_color)))
        if is_legal:
            # if rules.is_valid_flank_capture(row, column, board, current_color, opposite_color):
            #     print(f"🩷{column + 1}")
                refreshed_board = player.move(column=column, row=row, current_color=current_color, board=board)
                situ.reflesh_board(refreshed_board)
                if rules.is_valid_flank_capture_directly_above(row, column, board, current_color, opposite_color):
                    refreshed_board = player.flip_turn_directly_above(column=column, row=row, current_color=current_color, board=board)

                if rules.is_valid_flank_capture_right(row, column, board, current_color, opposite_color):
                    refreshed_board = player.flip_turn_right(column=column, row=row, current_color=current_color, board=board)

                if rules.is_valid_flank_capture_directly_below(row, column, board, current_color, opposite_color):
                    refreshed_board = player.flip_turn__directly_below(column=column, row=row, current_color=current_color, board=board)
                
                if rules.is_valid_flank_capture_left(row, column, board, current_color, opposite_color):
                    refreshed_board = player.flip_turn_left(column=column, row=row, current_color=current_color, board=board)

                situ.reflesh_board(refreshed_board)
                for i in range(len(rows)):
                    print(*rows[i])
                print("======================")

        else:
            while not is_legal:
                print(f"❌手 {row, column} は石を置けません❌")
                print("もう一度入力してください！！")
                for i in range(len(rows)):
                    print(*rows[i])
                row, column = situ.put_disc(input())
                if rules.is_legal_cell(row, column, board):
                    is_legal = rules.is_adjacent_cells_filled(
                        row, column, board, current_color
                    )
                print(f"ac :{is_legal}")
                if is_legal:
                    print(f"🙆手 {row, column} は有効です🙆")
                    refreshed_board = player.move(row, column, current_color, board)
                    situ.reflesh_board(refreshed_board)
                    for i in range(len(rows)):
                        print(*rows[i])
                    print("======================")
                    continue

    else:
        while not is_legal:
            print(f"❌手 {row, column} は石を置けません❌")
            print("もう一度入力してください！！")
            for i in range(len(rows)):
                print(*rows[i])
            print("======================")
            row, column = situ.put_disc(input())
            if rules.is_legal_cell(row, column, board):
                is_legal = rules.is_adjacent_cells_filled(
                    row, column, board, current_color
                )
            print(f"ac :{is_legal}")
            if is_legal:
                print(f"🙆手 {row, column} は有効です🙆")
                refreshed_board = player.move(row, column, current_color, board)
                situ.reflesh_board(refreshed_board)
                for i in range(len(rows)):
                    print(*rows[i])
                print("======================")
                continue


if __name__ == "__main__":
    main()
