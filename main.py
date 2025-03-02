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
    game_over = rules.is_placeable(board)
    while not game_over:
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
        if rules.is_legal_cell(row, column, board, opposite_color, current_color):
            game_over = rules.is_non_capturable(
                row, column, board, opposite_color, current_color
            )
            if game_over:
                break
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
                game_over = rules.is_non_capturable(
                row, column, board, opposite_color, current_color
                )
                if game_over:
                    break

                print("もう一度入力してください！！")
                for i in range(len(rows)):
                    print(*rows[i])
                print("======================")
                column, row = situ.put_disc(input())
                print(not rules.is_legal_cell(
                row, column, board, opposite_color, current_color
            ))

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
            game_over = rules.is_non_capturable(
                row, column, board, opposite_color, current_color
            )
            if game_over:
                break
            situ.reflesh_board(refreshed_board)
            for i in range(len(rows)):
                print(*rows[i])
            print("======================")
        game_over = rules.is_placeable(board)
    print("ゲーム終了")
    print("石を数えます。")
    count_black_discs, count_white_discs = rules.count_stones(board)
    print(f"先手、黒 {count_black_discs} 個")
    print(f"後手、白 {count_white_discs} 個")
    if count_black_discs > count_white_discs:
        print("先手、黒の勝利です")
    elif count_white_discs > count_black_discs:
        print("後手、白の勝利です")
    else:
        print("同数のため引き分けです。")


if __name__ == "__main__":
    main()
