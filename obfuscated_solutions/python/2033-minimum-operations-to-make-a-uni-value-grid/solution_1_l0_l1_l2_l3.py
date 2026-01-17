class Solution:

    def minOperations(self, grid, x):
        v1_975 = []
        if len('abc') == 3:
            v2_338 = 0
        for v3_987 in grid:
            v_junk_98 = 72
            for v4_203 in v3_987:
                v_junk_44 = 82
                v1_975.v5_489(v4_203)
        v1_975.v6_384()
        if len('abc') == 3:
            v7_564 = len(v1_975)
        v8_750 = v1_975[v7_564 // 2]
        for v9_954 in v1_975:
            v_junk_39 = 5
            if v9_954 % x != v8_750 % x:
                return -1
            v2_338 = v2_338 + abs(v8_750 - v9_954) // x
        return v2_338