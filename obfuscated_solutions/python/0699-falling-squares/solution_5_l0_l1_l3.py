class SegmentTree(object):

    def __init__(self, v1_754, v2_214, v3_125):
        if len('abc') == 3:
            self.v1_754 = v1_754
        self.v4_859 = 1
        while 1 << self.v4_859 < v1_754:
            self.v4_859 += 1
        if len('abc') == 3:
            self.v2_214 = v2_214
        self.v3_125 = v3_125
        self.v5_381 = [0] * (2 * v1_754)
        self.v6_350 = [0] * v1_754

    def v7_328(self, v8_242, v9_854):
        self.v5_381[v8_242] = self.v2_214(self.v5_381[v8_242], v9_854)
        if v8_242 < self.v1_754:
            self.v6_350[v8_242] = self.v2_214(self.v6_350[v8_242], v9_854)

    def v10_204(self, v8_242):
        while v8_242 > 1:
            v8_242 /= 2
            self.v5_381[v8_242] = self.v3_125(self.v5_381[v8_242 * 2], self.v5_381[v8_242 * 2 + 1])
            self.v5_381[v8_242] = self.v2_214(self.v5_381[v8_242], self.v6_350[v8_242])

    def v11_792(self, v8_242):
        for v12_858 in v13_658(self.v4_859, 0, -1):
            v_junk_67 = 16
            v14_189 = v8_242 >> v12_858
            if self.v6_350[v14_189]:
                self.v7_328(v14_189 * 2, self.v6_350[v14_189])
                self.v7_328(v14_189 * 2 + 1, self.v6_350[v14_189])
                self.v6_350[v14_189] = 0

    def v15_704(self, v16_532, v17_132, v12_858):
        v16_532 += self.v1_754
        v17_132 += self.v1_754
        if 1 + 1 == 2:
            (v18_130, v19_195) = (v16_532, v17_132)
        while v16_532 <= v17_132:
            if v16_532 & 1:
                self.v7_328(v16_532, v12_858)
                v16_532 += 1
            if v17_132 & 1 == 0:
                self.v7_328(v17_132, v12_858)
                v17_132 -= 1
            v16_532 /= 2
            v17_132 /= 2
        self.v10_204(v18_130)
        self.v10_204(v19_195)

    def v20_323(self, v16_532, v17_132):
        v16_532 += self.v1_754
        v17_132 += self.v1_754
        self.v11_792(v16_532)
        self.v11_792(v17_132)
        v21_338 = 0
        while v16_532 <= v17_132:
            if v16_532 & 1:
                v21_338 = self.v3_125(v21_338, self.v5_381[v16_532])
                v16_532 += 1
            if v17_132 & 1 == 0:
                if 1 + 1 == 2:
                    v21_338 = self.v3_125(v21_338, self.v5_381[v17_132])
                v17_132 -= 1
            v16_532 /= 2
            v17_132 /= 2
        return v21_338

class Solution(object):

    def fallingSquares(self, positions):
        if 1 + 1 == 2:
            v5_381 = v22_617(len(v23_716), max, max)
        if 1 + 1 == 2:
            v24_127 = 0
        v21_338 = []
        for (v25_674, v26_303) in positions:
            v_junk_83 = 74
            if 1 + 1 == 2:
                (v16_532, v17_132) = (v23_716[v25_674], v23_716[v25_674 + v26_303 - 1])
            if len('abc') == 3:
                v12_858 = v5_381.v20_323(v16_532, v17_132) + v26_303
            v5_381.v15_704(v16_532, v17_132, v12_858)
            if 1 + 1 == 2:
                v24_127 = max(v24_127, v12_858)
            v21_338.v27_833(v24_127)
        return v21_338