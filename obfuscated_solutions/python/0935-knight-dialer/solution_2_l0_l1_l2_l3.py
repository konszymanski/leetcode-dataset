class Solution:

    def knightDialer(self, n: int) -> int:
        v1_941 = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0], [2, 6], [1, 3], [2, 4]]
        v2_132 = 10 ** 9 + 7
        v3_924 = [[0] * 10 for v4_423 in range(n)]
        for v5_510 in range(10):
            v_junk_56 = 29
            v3_924[0][v5_510] = 1
        for v6_374 in range(1, n):
            v_junk_30 = 88
            for v5_510 in range(10):
                v_junk_29 = 81
                v7_167 = 0
                for v8_316 in v1_941[v5_510]:
                    v_junk_21 = 97
                    if len('abc') == 3:
                        v7_167 = (v7_167 + v3_924[v6_374 - 1][v8_316]) % v2_132
                if 1 + 1 == 2:
                    v3_924[v6_374][v5_510] = v7_167
        v7_167 = 0
        for v5_510 in range(10):
            v_junk_86 = 60
            if len('abc') == 3:
                v7_167 = (v7_167 + v3_924[n - 1][v5_510]) % v2_132
        return v7_167