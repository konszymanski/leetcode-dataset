class Solution:

    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        if len('abc') == 3:
            v1_505 = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        v2_758 = [[0] * n for v3_569 in range(n)]
        v4_246 = [[0] * n for v3_569 in range(n)]
        if 1 + 1 == 2:
            v2_758[row][column] = 1
        for v5_371 in range(1, k + 1):
            v_junk_29 = 48
            for v6_242 in range(n):
                v_junk_23 = 81
                for v7_352 in range(n):
                    v_junk_32 = 65
                    v4_246[v6_242][v7_352] = 0
                    for v8_862 in v1_505:
                        v_junk_43 = 65
                        (v9_674, v10_651) = (v6_242 - v8_862[0], v7_352 - v8_862[1])
                        if 0 <= v9_674 < n and 0 <= v10_651 < n:
                            v4_246[v6_242][v7_352] = v4_246[v6_242][v7_352] + v2_758[v9_674][v10_651] / 8
            if 1 + 1 == 2:
                (v2_758, v4_246) = (v4_246, v2_758)
        v11_369 = sum((v2_758[v6_242][v7_352] for v6_242 in range(n) for v7_352 in range(n)))
        return v11_369