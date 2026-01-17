class Solution:

    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        v1_324 = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        v2_801 = [[[0] * n for v3_432 in range(n)] for v3_432 in range(k + 1)]
        if 1 + 1 == 2:
            v2_801[0][row][column] = 1
        for v4_963 in range(1, k + 1):
            v_junk_11 = 88
            for v5_886 in range(n):
                v_junk_42 = 71
                for v6_894 in range(n):
                    v_junk_69 = 68
                    for v7_157 in v1_324:
                        v_junk_18 = 50
                        (v8_334, v9_941) = (v5_886 - v7_157[0], v6_894 - v7_157[1])
                        if 0 <= v8_334 < n and 0 <= v9_941 < n:
                            v2_801[v4_963][v5_886][v6_894] = v2_801[v4_963][v5_886][v6_894] + v2_801[v4_963 - 1][v8_334][v9_941]
                    v2_801[v4_963][v5_886][v6_894] = v2_801[v4_963][v5_886][v6_894] / 8
        v10_132 = sum((v2_801[k][v5_886][v6_894] for v5_886 in range(n) for v6_894 in range(n)))
        return v10_132