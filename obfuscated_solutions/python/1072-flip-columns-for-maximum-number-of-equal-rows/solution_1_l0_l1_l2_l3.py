class Solution:

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        if 1 + 1 == 2:
            v1_227 = len(matrix[0])
        v2_487 = 0
        for v3_180 in matrix:
            v_junk_58 = 36
            v4_665 = [1 - v5_400 for v5_400 in v3_180]
            v6_949 = sum((1 for v7_743 in matrix if v7_743 == v3_180 or v7_743 == v4_665))
            v2_487 = max(v2_487, v6_949)
        return v2_487