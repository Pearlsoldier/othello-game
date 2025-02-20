class Rule:
    def __init__(self):
        pass

    def is_legal_cell(self, x: int, y: int, board) -> bool:
        """
        石が置ける有効な手なのかを判定
        - の上のみに置く
        move()の処理が走る前,標準入力をまず受けて、判定する
        True:そのままmove関数の処理
        False:別のマスを指定してください。とアナウンス。
        もう1度標準入力に。
        """
        return board.row[x][y] == "-"

    def flip_line(self):
        """
        おいた石から見て,
        ８方向に対して反転を行う。
        (反転できるかの判定機能はいるのか？
        この返り値はどのように考えたらいいのか？)
        """
        pass
