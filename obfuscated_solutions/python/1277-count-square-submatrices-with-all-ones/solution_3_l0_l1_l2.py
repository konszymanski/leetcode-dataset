class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        (v1_754, v2_214, v3_125, v4_859) = (len(matrix), len(matrix[0]), 0, 0)
        v5_381 = [0 for v6_350 in range(v2_214 + 1)]
        for v7_328 in range(1, v1_754 + 1):
            for v8_242 in range(1, v2_214 + 1):
                if matrix[v7_328 - 1][v8_242 - 1] != 1:
                    v5_381[v8_242] = 0
                else:
                    v9_854 = v5_381[v8_242]
                    v5_381[v8_242] = 1 + min(v4_859, min(v5_381[v8_242 - 1], v5_381[v8_242]))
                    v4_859 = v9_854
                    v3_125 = v3_125 + v5_381[v8_242]
        return v3_125