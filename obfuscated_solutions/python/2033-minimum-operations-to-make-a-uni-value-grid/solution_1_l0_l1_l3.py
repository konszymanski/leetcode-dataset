class Solution:

    def minOperations(self, grid, x):
        if len('abc') == 3:
            v1_754 = []
        if len('abc') == 3:
            v2_214 = 0
        for v3_125 in grid:
            v_junk_56 = 74
            for v4_859 in v3_125:
                v_junk_90 = 80
                v1_754.v5_381(v4_859)
        v1_754.v6_350()
        if 1 + 1 == 2:
            v7_328 = len(v1_754)
        if 1 + 1 == 2:
            v8_242 = v1_754[v7_328 // 2]
        for v9_854 in v1_754:
            v_junk_47 = 11
            if v9_854 % x != v8_242 % x:
                return -1
            v2_214 += abs(v8_242 - v9_854) // x
        return v2_214