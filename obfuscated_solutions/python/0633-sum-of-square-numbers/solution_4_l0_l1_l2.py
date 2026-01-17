class Solution(object):

    def judgeSquareSum(self, c):

        def v1_754(v2_214, v3_125, v4_859):
            if v2_214 > v3_125:
                return False
            v5_381 = v2_214 + (v3_125 - v2_214) // 2
            if v5_381 * v5_381 != v4_859:
                if v5_381 * v5_381 <= v4_859:
                    return v1_754(v5_381 + 1, v3_125, v4_859)
                else:
                    return v1_754(v2_214, v5_381 - 1, v4_859)
            else:
                return True
        for v6_350 in range(int(c ** 0.5) + 1):
            v7_328 = c - v6_350 * v6_350
            if v1_754(0, v7_328, v7_328):
                return True
        return False