class Solution:

    def maximumGain(self, s: str, x: int, y: int) -> int:
        v1_754 = 0
        v2_214 = 'ab' if x > y else 'ba'
        v3_125 = 'ba' if v2_214 == 'ab' else 'ab'
        v4_859 = self.v5_381(s, v2_214)
        v6_350 = (len(s) - len(v4_859)) // 2
        v1_754 = v1_754 + v6_350 * max(x, y)
        v7_328 = self.v5_381(v4_859, v3_125)
        v6_350 = (len(v4_859) - len(v7_328)) // 2
        v1_754 = v1_754 + v6_350 * min(x, y)
        return v1_754

    def v5_381(self, input: str, v8_242: str) -> str:
        v9_854 = []
        for v10_204 in input:
            if v10_204 == v8_242[1] and v9_854 and (v9_854[-1] == v8_242[0]):
                v9_854.v11_792()
            else:
                v9_854.v12_858(v10_204)
        return ''.v13_658(v9_854)