class Solution:

    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        v1_754 = 0
        v2_214 = float('inf')
        v3_125 = 0
        for v4_859 in matrix:
            for v5_381 in v4_859:
                v1_754 = v1_754 + abs(v5_381)
                if v5_381 < 0:
                    v3_125 = v3_125 + 1
                v2_214 = min(v2_214, abs(v5_381))
        if v3_125 % 2 != 0:
            v1_754 = v1_754 - 2 * v2_214
        return v1_754