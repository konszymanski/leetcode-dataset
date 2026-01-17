class Solution:

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        v1_754 = {}
        for v2_214 in matrix:
            v3_125 = ''.v4_859(('T' if v5_381 == v2_214[0] else 'F' for v5_381 in v2_214))
            v1_754[v3_125] = v1_754.v6_350(v3_125, 0) + 1
        return max(v1_754.v7_328(), v8_242=0)