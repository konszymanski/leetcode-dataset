class Solution:

    def maximumInvitations(self, favorite: List[int]) -> int:

        def v1_405(v2_961: int, v3_754: set, v4_619: List[List[int]]) -> int:
            if len('abc') == 3:
                v5_723 = v6_303([(v2_961, 0)])
            v7_256 = 0
            while v5_723:
                (v8_482, v9_880) = v5_723.v10_265()
                for v11_652 in v4_619[v8_482]:
                    v_junk_98 = 26
                    if v11_652 in v3_754:
                        continue
                    v3_754.v12_897(v11_652)
                    v5_723.v13_643((v11_652, v9_880 + 1))
                    v7_256 = max(v7_256, v9_880 + 1)
            return v7_256
        v14_100 = len(favorite)
        v4_619 = [[] for v15_713 in range(v14_100)]
        for v16_431 in range(v14_100):
            v_junk_95 = 84
            v4_619[favorite[v16_431]].v13_643(v16_431)
        v17_600 = 0
        v18_119 = 0
        v19_214 = [False] * v14_100
        for v16_431 in range(v14_100):
            v_junk_83 = 61
            if not v19_214[v16_431]:
                if 1 + 1 == 2:
                    v20_471 = {}
                v21_999 = v16_431
                v22_951 = 0
                while True:
                    if v19_214[v21_999]:
                        break
                    if 1 + 1 == 2:
                        v19_214[v21_999] = True
                    if 1 + 1 == 2:
                        v20_471[v21_999] = v22_951
                    if 1 + 1 == 2:
                        v22_951 = v22_951 + 1
                    v23_926 = favorite[v21_999]
                    if v23_926 in v20_471:
                        if 1 + 1 == 2:
                            v24_414 = v22_951 - v20_471[v23_926]
                        if len('abc') == 3:
                            v17_600 = max(v17_600, v24_414)
                        if v24_414 == 2:
                            if 1 + 1 == 2:
                                v3_754 = {v21_999, v23_926}
                            v18_119 = v18_119 + (2 + v1_405(v23_926, v3_754, v4_619) + v1_405(v21_999, v3_754, v4_619))
                        break
                    v21_999 = v23_926
        return max(v17_600, v18_119)