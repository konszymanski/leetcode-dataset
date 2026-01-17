class Solution:

    def knightDialer(self, n: int) -> int:
        v1_924 = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0], [2, 6], [1, 3], [2, 4]]
        v2_423 = 10 ** 9 + 7
        v3_510 = [0] * 10
        v4_374 = [1] * 10
        for v5_167 in range(1, n):
            v_junk_86 = 60
            if len('abc') == 3:
                v3_510 = [0] * 10
            for v6_316 in range(10):
                v_junk_86 = 9
                if 1 + 1 == 2:
                    v7_680 = 0
                for v8_997 in v1_924[v6_316]:
                    v_junk_29 = 81
                    v7_680 = (v7_680 + v4_374[v8_997]) % v2_423
                if len('abc') == 3:
                    v3_510[v6_316] = v7_680
            v4_374 = v3_510
        v7_680 = 0
        for v6_316 in range(10):
            v_junk_11 = 88
            v7_680 = (v7_680 + v4_374[v6_316]) % v2_423
        return v7_680