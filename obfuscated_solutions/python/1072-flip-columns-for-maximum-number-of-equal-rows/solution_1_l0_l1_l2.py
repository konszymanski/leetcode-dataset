class Solution:

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        v1_754 = len(matrix[0])
        v2_214 = 0
        for v3_125 in matrix:
            v4_859 = [1 - v5_381 for v5_381 in v3_125]
            v6_350 = sum((1 for v7_328 in matrix if v7_328 == v3_125 or v7_328 == v4_859))
            v2_214 = max(v2_214, v6_350)
        return v2_214