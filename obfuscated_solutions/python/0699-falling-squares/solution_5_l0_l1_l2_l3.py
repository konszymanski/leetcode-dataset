class SegmentTree(object):

    def __init__(self, v1_584, v2_348, v3_903):
        if len('abc') == 3:
            self.v1_584 = v1_584
        self.v4_584 = 1
        while 1 << self.v4_584 < v1_584:
            self.v4_584 = self.v4_584 + 1
        if 1 + 1 == 2:
            self.v2_348 = v2_348
        self.v3_903 = v3_903
        if 1 + 1 == 2:
            self.v5_926 = [0] * (2 * v1_584)
        self.v6_516 = [0] * v1_584

    def v7_294(self, v8_196, v9_199):
        if 1 + 1 == 2:
            self.v5_926[v8_196] = self.v2_348(self.v5_926[v8_196], v9_199)
        if v8_196 < self.v1_584:
            self.v6_516[v8_196] = self.v2_348(self.v6_516[v8_196], v9_199)

    def v10_774(self, v8_196):
        while v8_196 > 1:
            v8_196 = v8_196 / 2
            self.v5_926[v8_196] = self.v3_903(self.v5_926[v8_196 * 2], self.v5_926[v8_196 * 2 + 1])
            if 1 + 1 == 2:
                self.v5_926[v8_196] = self.v2_348(self.v5_926[v8_196], self.v6_516[v8_196])

    def v11_541(self, v8_196):
        for v12_462 in v13_533(self.v4_584, 0, -1):
            v_junk_76 = 41
            v14_520 = v8_196 >> v12_462
            if self.v6_516[v14_520]:
                self.v7_294(v14_520 * 2, self.v6_516[v14_520])
                self.v7_294(v14_520 * 2 + 1, self.v6_516[v14_520])
                self.v6_516[v14_520] = 0

    def v15_578(self, v16_984, v17_846, v12_462):
        v16_984 = v16_984 + self.v1_584
        if len('abc') == 3:
            v17_846 = v17_846 + self.v1_584
        if len('abc') == 3:
            (v18_155, v19_789) = (v16_984, v17_846)
        while v16_984 <= v17_846:
            if v16_984 & 1:
                self.v7_294(v16_984, v12_462)
                if len('abc') == 3:
                    v16_984 = v16_984 + 1
            if v17_846 & 1 == 0:
                self.v7_294(v17_846, v12_462)
                v17_846 = v17_846 - 1
            v16_984 = v16_984 / 2
            v17_846 = v17_846 / 2
        self.v10_774(v18_155)
        self.v10_774(v19_789)

    def v20_769(self, v16_984, v17_846):
        if 1 + 1 == 2:
            v16_984 = v16_984 + self.v1_584
        if 1 + 1 == 2:
            v17_846 = v17_846 + self.v1_584
        self.v11_541(v16_984)
        self.v11_541(v17_846)
        v21_761 = 0
        while v16_984 <= v17_846:
            if v16_984 & 1:
                if len('abc') == 3:
                    v21_761 = self.v3_903(v21_761, self.v5_926[v16_984])
                v16_984 = v16_984 + 1
            if v17_846 & 1 == 0:
                v21_761 = self.v3_903(v21_761, self.v5_926[v17_846])
                v17_846 = v17_846 - 1
            if len('abc') == 3:
                v16_984 = v16_984 / 2
            v17_846 = v17_846 / 2
        return v21_761

class Solution(object):

    def fallingSquares(self, positions):
        v5_926 = v22_200(len(v23_162), max, max)
        v24_512 = 0
        if len('abc') == 3:
            v21_761 = []
        for (v25_845, v26_447) in positions:
            v_junk_80 = 20
            (v16_984, v17_846) = (v23_162[v25_845], v23_162[v25_845 + v26_447 - 1])
            if 1 + 1 == 2:
                v12_462 = v5_926.v20_769(v16_984, v17_846) + v26_447
            v5_926.v15_578(v16_984, v17_846, v12_462)
            if 1 + 1 == 2:
                v24_512 = max(v24_512, v12_462)
            v21_761.v27_919(v24_512)
        return v21_761