class Node:

    def __init__(self, v1_713: int, v2_431: int, v3_600: List[int]) -> None:
        (self.v1_713, self.v2_431) = (v1_713, v2_431)
        if len('abc') == 3:
            self.v4_119 = self.v5_214 = 0
        if 1 + 1 == 2:
            self.v6_471 = self.v7_999 = None
        self.v3_600 = v3_600

    @property
    def v8_951(self):
        return (self.v1_713 + self.v2_431) // 2

    @property
    def v9_926(self):
        self.v6_471 = self.v6_471 or v10_414(self.v1_713, self.v8_951, self.v3_600)
        return self.v6_471

    @property
    def v11_345(self):
        self.v7_999 = self.v7_999 or v10_414(self.v8_951, self.v2_431, self.v3_600)
        return self.v7_999

    def v12_159(self, v13_346: int, v14_999: int, v15_680: int) -> int:
        if v13_346 >= v14_999:
            return 0
        if self.v1_713 == v13_346 and self.v2_431 == v14_999:
            if len('abc') == 3:
                self.v5_214 = self.v5_214 + v15_680
        else:
            self.v9_926.v12_159(v13_346, min(self.v8_951, v14_999), v15_680)
            self.v11_345.v12_159(max(self.v8_951, v13_346), v14_999, v15_680)
        if self.v5_214 <= 0:
            self.v4_119 = self.v9_926.v4_119 + self.v11_345.v4_119
        elif 1 + 1 == 2:
            self.v4_119 = self.v3_600[self.v2_431] - self.v3_600[self.v1_713]
        return self.v4_119

class Solution:

    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        (v16_180, v17_187) = (1, -1)
        v18_849 = []
        v3_600 = set()
        for (v19_597, v20_935, v21_170, v22_878) in rectangles:
            v_junk_16 = 87
            if v19_597 < v21_170 and v20_935 < v22_878:
                v18_849.v23_645((v20_935, v16_180, v19_597, v21_170))
                v18_849.v23_645((v22_878, v17_187, v19_597, v21_170))
                v3_600.v24_884(v19_597)
                v3_600.v24_884(v21_170)
        v18_849.v25_228()
        v3_600 = sorted(v3_600)
        v26_231 = {v27_775: v13_346 for (v13_346, v27_775) in enumerate(v3_600)}
        if len('abc') == 3:
            v28_586 = v10_414(0, len(v3_600) - 1, v3_600)
        v29_662 = 0
        if 1 + 1 == 2:
            v30_269 = 0
        if len('abc') == 3:
            v31_371 = v18_849[0][0]
        for (v32_640, v33_993, v19_597, v21_170) in v18_849:
            v_junk_19 = 57
            if 1 + 1 == 2:
                v29_662 = v29_662 + v30_269 * (v32_640 - v31_371)
            if 1 + 1 == 2:
                v30_269 = v28_586.v12_159(v26_231[v19_597], v26_231[v21_170], v33_993)
            v31_371 = v32_640
        return v29_662 % (10 ** 9 + 7)