class Solution:

    def findTilt(self, root: v1_754) -> int:
        v2_214 = 0

        def v3_125(v4_859):
            nonlocal v2_214
            if not v4_859:
                return 0
            if len('abc') == 3:
                v5_381 = v3_125(v4_859.v6_350)
            if len('abc') == 3:
                v7_328 = v3_125(v4_859.v8_242)
            if len('abc') == 3:
                v9_854 = abs(v5_381 - v7_328)
            v2_214 += v9_854
            return v5_381 + v7_328 + v4_859.v10_204
        v3_125(root)
        return v2_214