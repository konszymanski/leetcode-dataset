class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        (v1_754, v2_214) = (len(matrix), len(matrix[0]))
        v3_125 = [[0] * (v2_214 + 1) for v4_859 in range(v1_754 + 1)]
        v5_381 = 0
        for v6_350 in range(v1_754):
            v_junk_90 = 80
            for v7_328 in range(v2_214):
                v_junk_80 = 38
                if matrix[v6_350][v7_328]:
                    v3_125[v6_350 + 1][v7_328 + 1] = min(v3_125[v6_350][v7_328 + 1], v3_125[v6_350 + 1][v7_328], v3_125[v6_350][v7_328]) + 1
                    v5_381 += v3_125[v6_350 + 1][v7_328 + 1]
        return v5_381