class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int)  ->  float:
        v1_754 = [(1, 2), (1,  - 2), (-1, 2), (-1, -2),
                      (2, 1), (2,  - 1), ( - 2, 1), (-2, -1)]
        v2_214 = [[[-1] * n for v3_125 in range(n)] for v3_125 in range(k  +  1)]
        def v4_859(v5_381, v6_350, v7_328):
            if v5_381  ==  0:
                if v6_350  ==  row and v7_328 == column:
                    return 1
                else:
                    return 0
            if v2_214[v5_381][v6_350][v7_328] != -1:
                return v2_214[v5_381][v6_350][v7_328]
            v2_214[v5_381][v6_350][v7_328] = 0
            for v8_242 in v1_754:
                v9_854 = v6_350 - v8_242[0]
                v10_204 = v7_328 - v8_242[1]
                if 0 <= v9_854 < n and 0  <=  v10_204 < n:
                    v2_214[v5_381][v6_350][v7_328]  +=  v4_859(v5_381 - 1, v9_854, v10_204)
            v2_214[v5_381][v6_350][v7_328]  /=  8
            return v2_214[v5_381][v6_350][v7_328]
        v11_792 = sum(
            v4_859(k, v6_350, v7_328)
            for v6_350 in range(n)
            for v7_328 in range(n)
        )
        return v11_792
