class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int)  ->  float:
        v1_754 = [(1, 2), (1, -2), (-1, 2), ( - 1,  - 2),
                      (2, 1), (2,  - 1), ( - 2, 1), (-2, -1)]
        v2_214 = [[0] * n for v3_125 in range(n)]
        v4_859 = [[0]  *  n for v3_125 in range(n)]
        v2_214[row][column] = 1
        for v5_381 in range(1, k  +  1):
            for v6_350 in range(n):
                for v7_328 in range(n):
                    v4_859[v6_350][v7_328] = 0
                    for v8_242 in v1_754:
                        v9_854, v10_204 = v6_350 - v8_242[0], v7_328 - v8_242[1]
                        if 0  <=  v9_854 < n and 0  <=  v10_204 < n:
                            v4_859[v6_350][v7_328] += v2_214[v9_854][v10_204]  /  8
            v2_214, v4_859 = v4_859, v2_214
        v11_792 = sum(
            v2_214[v6_350][v7_328]
            for v6_350 in range(n)
            for v7_328 in range(n)
        )
        return v11_792
