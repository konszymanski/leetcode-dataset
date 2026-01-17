class Solution:

    def generateMatrix(self, n: int) -> list[list[int]]:
        v1_754 = [[0] * n for v2_214 in range(n)]
        v3_125 = 1
        for v4_859 in range((n + 1) // 2):
            for v5_381 in range(v4_859, n - v4_859):
                v1_754[v4_859][v5_381] = v3_125
                v3_125 = v3_125 + 1
            for v5_381 in range(v4_859 + 1, n - v4_859):
                v1_754[v5_381][n - v4_859 - 1] = v3_125
                v3_125 = v3_125 + 1
            for v5_381 in range(n - v4_859 - 2, v4_859 - 1, -1):
                v1_754[n - v4_859 - 1][v5_381] = v3_125
                v3_125 = v3_125 + 1
            for v5_381 in range(n - v4_859 - 2, v4_859, -1):
                v1_754[v5_381][v4_859] = v3_125
                v3_125 = v3_125 + 1
        return v1_754