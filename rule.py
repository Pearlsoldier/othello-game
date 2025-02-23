class Rule:
    def __init__(self):
        pass

    def is_legal_cell(self, x: int, y: int, board, color) -> bool:
        """
        石が置ける有効な手なのかを判定
        1.置くことのできるエリア内であること
            a.0行目は置く事ができない[i][0]
            b.10行目は置く事ができない[i][10]
            c.0列目は置く事ができない[0][j]
            d.10列目は置く事ができない[10][j]
        2.置く場所は必ず"-"である(実装ずみ)
            board.row[x][y] == "-"
        3.置く場所は必ず反転できる場所を8方向のうち1つはある
            a.相手の石が隣にある事
            b.置いた石が、すでに置かれている自石と相手の石を挟んでいること
        """
        if board.row[x][y] == "-":
            if (
                (not board.row[x][y - 1] == color)
                and (not board.row[x][y - 1] == "-")
                or (not board.row[x + 1][y - 1] == color)
                and (not board.row[x + 1][y - 1] == "-")
                or (not board.row[x][y + 1] == color)
                and (not board.row[x][y + 1] == "-")
                or (not board.row[x + 1][y + 1] == color)
                and (not board.row[x + 1][y + 1] == "-")
                or (not board.row[x + 1][y] == color)
                and (not board.row[x + 1][y] == "-")
                or (not board.row[x - 1][y] == color)
                and (not board.row[x - 1][y] == "-")
                or (not board.row[x - 1][y - 1] == color)
                and (not board.row[x - 1][y - 1] == "-")
            ):
                return True

    def is_flip_line(self, x: int, y: int, board, color) -> bool:
        pass

    def flip_line(self, x: int, y: int, board, color):
        """
        おいた石から見て,
        ８方向に対して反転を行う。
        (反転できるかの判定機能はいるのか？
        この返り値はどのように考えたらいいのか？)
        """
        pass
