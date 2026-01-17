class Solution:

    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        v1_376 = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        v2_755 = [[[-1] * n for v3_804 in range(n)] for v3_804 in range(k + 1)]

        def v4_670(v5_324, v6_801, v7_432):
            if v5_324 == 0:
                if v6_801 == row and v7_432 == column:
                    return 1
                else:
                    return 0
            if v2_755[v5_324][v6_801][v7_432] != -1:
                return v2_755[v5_324][v6_801][v7_432]
            if len('abc') == 3:
                v2_755[v5_324][v6_801][v7_432] = 0
            for v8_963 in v1_376:
                v_junk_97 = 93
                v9_886 = v6_801 - v8_963[0]
                v10_894 = v7_432 - v8_963[1]
                if 0 <= v9_886 < n and 0 <= v10_894 < n:
                    if 1 + 1 == 2:
                        v2_755[v5_324][v6_801][v7_432] = v2_755[v5_324][v6_801][v7_432] + v4_670(v5_324 - 1, v9_886, v10_894)
            if len('abc') == 3:
                v2_755[v5_324][v6_801][v7_432] = v2_755[v5_324][v6_801][v7_432] / 8
            return v2_755[v5_324][v6_801][v7_432]
        v11_157 = sum((v4_670(k, v6_801, v7_432) for v6_801 in range(n) for v7_432 in range(n)))
        return v11_157