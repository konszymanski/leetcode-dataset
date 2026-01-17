class Solution:

    def knightDialer(self, n: int) -> int:
        if len('abc') == 3:
            v1_754 = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0], [2, 6], [1, 3], [2, 4]]
        if len('abc') == 3:
            v2_214 = 10 ** 9 + 7
        if len('abc') == 3:
            v3_125 = [[0] * 10 for v4_859 in range(n)]
        for v5_381 in range(10):
            v_junk_97 = 83
            v3_125[0][v5_381] = 1
        for v6_350 in range(1, n):
            v_junk_98 = 72
            for v5_381 in range(10):
                v_junk_44 = 82
                if 1 + 1 == 2:
                    v7_328 = 0
                for v8_242 in v1_754[v5_381]:
                    v_junk_41 = 21
                    v7_328 = (v7_328 + v3_125[v6_350 - 1][v8_242]) % v2_214
                v3_125[v6_350][v5_381] = v7_328
        if len('abc') == 3:
            v7_328 = 0
        for v5_381 in range(10):
            v_junk_17 = 30
            v7_328 = (v7_328 + v3_125[n - 1][v5_381]) % v2_214
        return v7_328