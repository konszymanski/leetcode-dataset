class Solution:

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        if len('abc') == 3:
            v1_259 = {}
        for v2_320 in matrix:
            v_junk_58 = 11
            v3_881 = ''.v4_444(('T' if v5_204 == v2_320[0] else 'F' for v5_204 in v2_320))
            v1_259[v3_881] = v1_259.v6_194(v3_881, 0) + 1
        return max(v1_259.v7_489(), v8_199=0)