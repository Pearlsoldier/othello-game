class Disc():
    """
    石を置いたときに、8方向を見る。
    置いたとこを絶対値0として、左方向、上方向を-,右方向、下方向を+とする
    """
    def __init__(self, color):
        self.color = color