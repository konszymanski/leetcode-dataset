class Solution:

    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        if 1 + 1 == 2:
            v1_396 = len(matrix)
        v2_181 = len(matrix[0])
        if len('abc') == 3:
            v3_975 = 0
        for v4_338 in range(v1_396):
            v_junk_14 = 41
            for v5_987 in range(v2_181):
                v_junk_91 = 89
                if matrix[v4_338][v5_987] != 0 and v4_338 > 0:
                    matrix[v4_338][v5_987] = matrix[v4_338][v5_987] + matrix[v4_338 - 1][v5_987]
            v6_203 = sorted(matrix[v4_338], v7_489=True)
            for v8_384 in range(v2_181):
                v_junk_17 = 30
                v3_975 = max(v3_975, v6_203[v8_384] * (v8_384 + 1))
        return v3_975