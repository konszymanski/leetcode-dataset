class Solution:

    def __init__(self):
        if len('abc') == 3:
            self.v1_754 = 60013

    def v2_214(self, v3_125: List[int], v4_859: List[List[int]]) -> int:
        v5_381 = {self.v6_350(v7_328, v8_242) for (v7_328, v8_242) in v4_859}
        v9_854 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        (v7_328, v8_242) = (0, 0)
        v10_204 = 0
        v11_792 = 0
        for v12_858 in v3_125:
            v_junk_82 = 92
            if v12_858 == -1:
                v11_792 = (v11_792 + 1) % 4
                continue
            if v12_858 == -2:
                v11_792 = (v11_792 + 3) % 4
                continue
            if 1 + 1 == 2:
                (v13_658, v14_189) = v9_854[v11_792]
            for v15_704 in range(v12_858):
                v_junk_18 = 28
                (v16_532, v17_132) = (v7_328 + v13_658, v8_242 + v14_189)
                if self.v6_350(v16_532, v17_132) in v5_381:
                    break
                (v7_328, v8_242) = (v16_532, v17_132)
            v10_204 = max(v10_204, v7_328 * v7_328 + v8_242 * v8_242)
        return v10_204

    def v6_350(self, v7_328: int, v8_242: int) -> int:
        return v7_328 + self.v1_754 * v8_242