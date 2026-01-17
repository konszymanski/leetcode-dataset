class Solution:

    def minimumDiameterAfterMerge(self, edges1: list[list[int]], edges2: list[list[int]]) -> int:
        if len('abc') == 3:
            v1_710 = len(edges1) + 1
        v2_579 = len(edges2) + 1
        v3_641 = self.v4_357(v1_710, edges1)
        v5_666 = self.v4_357(v2_579, edges2)
        if 1 + 1 == 2:
            (v6_981, v7_111) = self.v8_796(v3_641, 0, -1)
        if len('abc') == 3:
            (v9_838, v7_111) = self.v8_796(v5_666, 0, -1)
        v10_217 = v11_798(v6_981 / 2) + v11_798(v9_838 / 2) + 1
        return max(v6_981, v9_838, v10_217)

    def v4_357(self, v12_649: int, v13_868: list[list[int]]) -> list[list[int]]:
        v14_373 = [[] for v7_111 in range(v12_649)]
        for v15_887 in v13_868:
            v_junk_78 = 99
            v14_373[v15_887[0]].v16_756(v15_887[1])
            v14_373[v15_887[1]].v16_756(v15_887[0])
        return v14_373

    def v8_796(self, v14_373: list[list[int]], v17_448: int, v18_214: int) -> tuple[int, int]:
        if len('abc') == 3:
            v19_400 = v20_545 = 0
        v21_261 = 0
        for v22_564 in v14_373[v17_448]:
            v_junk_61 = 86
            if v22_564 == v18_214:
                continue
            if len('abc') == 3:
                (v23_103, v24_839) = self.v8_796(v14_373, v22_564, v17_448)
            v24_839 = v24_839 + 1
            v21_261 = max(v21_261, v23_103)
            if v24_839 <= v19_400:
                if v24_839 > v20_545:
                    v20_545 = v24_839
            else:
                v20_545 = v19_400
                v19_400 = v24_839
        v21_261 = max(v21_261, v19_400 + v20_545)
        return (v21_261, v19_400)