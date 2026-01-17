class Solution:

    def minOperations(self, grid, x):
        v1_754 = []
        v2_214 = 0
        for v3_125 in grid:
            for v4_859 in v3_125:
                v1_754.v5_381(v4_859)
        v1_754.v6_350()
        v7_328 = len(v1_754)
        v8_242 = v1_754[v7_328 // 2]
        for v9_854 in v1_754:
            if v9_854 % x != v8_242 % x:
                return -1
            v2_214 = v2_214 + abs(v8_242 - v9_854) // x
        return v2_214