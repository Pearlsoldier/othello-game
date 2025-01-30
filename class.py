class basetile:
    """
    石クラス
    白石、黒石の基底になるクラス
    """
    def __init__(self):
        pass


class whitetile(basetile):
    """
    石クラスを基底した白石クラス
    期待する振る舞いとして、
    1. 置いた時に、隣自身から見て8方向を見て、
        黒石がないかを確認する
    2.置いた白石が黒石を囲むとその黒石は白石に苗う
    """
    def __init__(self):
        super().__init__()


class blacktile(basetile):
    """
    白石と同じ
    """
    def __init__(self):
        super().__init__()


class turn:
    """
    役割としてターンを保持する。
    白石、黒石のターンを分ける
    現在のターンを明示する。
    """
    def __init__(self):
        pass


class player:
    """
    プレイヤーを基底するクラス
    """
    def __init__(self):
        pass


class white_player(player):
    """
    役割としては、
    白石を扱う
    期待する振る舞いは
    白石を置くことができる。
    黒石を白石にひっくり返すことができる。
    """
    def __init__(self):
        super().__init__()


class black_player(player):
    """
    黒石を扱い、
    黒石をおき、白石をひっくり返すことができる
    """
    def __init__(self):
        super().__init__()


class bord:
    """
    8*8の64に石を置くことができる。
    bordの一番最初に、白黒の石が２個ずつボードの中心に置く
    """
    def __init__(self):
        pass
