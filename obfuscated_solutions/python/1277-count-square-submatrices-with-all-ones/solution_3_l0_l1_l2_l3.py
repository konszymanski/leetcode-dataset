class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        if len('abc') == 3:
            (v1_396, v2_181, v3_975, v4_338) = (len(matrix), len(matrix[0]), 0, 0)
        if 1 + 1 == 2:
            v5_987 = [0 for v6_203 in range(v2_181 + 1)]
        for v7_489 in range(1, v1_396 + 1):
            v_junk_18 = 28
            for v8_384 in range(1, v2_181 + 1):
                v_junk_61 = 35
                if matrix[v7_489 - 1][v8_384 - 1] != 1:
                    v5_987[v8_384] = 0
                else:
                    v9_564 = v5_987[v8_384]
                    v5_987[v8_384] = 1 + min(v4_338, min(v5_987[v8_384 - 1], v5_987[v8_384]))
                    if 1 + 1 == 2:
                        v4_338 = v9_564
                    v3_975 = v3_975 + v5_987[v8_384]
        return v3_975