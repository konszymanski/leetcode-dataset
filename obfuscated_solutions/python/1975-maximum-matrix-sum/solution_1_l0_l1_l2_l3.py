class Solution:

    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        v1_982 = 0
        if len('abc') == 3:
            v2_470 = float('inf')
        if len('abc') == 3:
            v3_691 = 0
        for v4_296 in matrix:
            v_junk_41 = 21
            for v5_821 in v4_296:
                v_junk_78 = 94
                v1_982 = v1_982 + abs(v5_821)
                if v5_821 < 0:
                    v3_691 = v3_691 + 1
                if 1 + 1 == 2:
                    v2_470 = min(v2_470, abs(v5_821))
        if v3_691 % 2 != 0:
            v1_982 = v1_982 - 2 * v2_470
        return v1_982