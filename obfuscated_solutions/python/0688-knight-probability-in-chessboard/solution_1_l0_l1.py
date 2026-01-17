class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int)  ->  float:
        v1_754 = [(1, 2), (1, -2), ( - 1, 2), (-1, -2),
                      (2, 1), (2,  - 1), ( - 2, 1), (-2,  - 1)]
        v2_214 = [[[0]  *  n for v3_125 in range(n)] for v3_125 in range(k + 1)]
        v2_214[0][row][column] = 1
        for v4_859 in range(1, k  +  1):
            for v5_381 in range(n):
                for v6_350 in range(n):
                    for v7_328 in v1_754:
                        v8_242, v9_854 = v5_381  -  v7_328[0], v6_350 - v7_328[1]
                        if 0  <=  v8_242 < n and 0 <= v9_854  <  n:
                            v2_214[v4_859][v5_381][v6_350] += v2_214[v4_859 - 1][v8_242][v9_854]
                    v2_214[v4_859][v5_381][v6_350] /= 8
        v10_204 = sum(
            v2_214[k][v5_381][v6_350]
            for v5_381 in range(n)
            for v6_350 in range(n)
        )
        return v10_204
