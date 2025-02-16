#  match 対象オブジェクト:
#     case パターン1:
#         パターン1がマッチした時の処理
#     case パターン2:
#         パターン2がマッチした時の処理
# 対象のオブジェクトは、プレイヤーが置いた石
# パターンは9方向に対して
# どのような処理か、
# 黒石を置いたときの右（左、上下など）の石が同じなら、何もしない。pass
# 異なる石なら次の石を見る。置いた石と同じなら、隣の石は黒石になる
# →黒、白、黒　：　黒、黒、黒
# →黒、白、白, ブランク　： pass
# →位置[x行][y列]のうち、x行は固定、[y列]の末端の石がmatchするかを確認　
# 隣に石があるかどうかだけの判断を行う。
# 隣に置く場所がない。→盤の縁が隣なら、何もしない。pass
