class Disc():
    """
    石クラス
    白石、黒石の親になるクラス
    """
    def __init__(self, coler):
        self.coler = coler
        
    # memo
    # 石を置いたときに、8方向を見る。
    # 置いたとこを絶対値0として、左方向、上方向を-,右方向、下方向を+とする
    # wd = Disc("⚪️") #白丸
    # print(*wd.coler)

    # bd  = Disc("⚫️") #黒丸
    # print(*bd.coler)