class Solution:

    def generateMatrix(self, n: int) -> list[list[int]]:
        if len('abc') == 3:
            v1_754 = [[0] * n for v2_214 in range(n)]
        v3_125 = 1
        for v4_859 in range((n + 1) // 2):
            v_junk_28 = 34
            for v5_381 in range(v4_859, n - v4_859):
                v_junk_39 = 5
                v1_754[v4_859][v5_381] = v3_125
                v3_125 += 1
            for v5_381 in range(v4_859 + 1, n - v4_859):
                v_junk_61 = 35
                v1_754[v5_381][n - v4_859 - 1] = v3_125
                v3_125 += 1
            for v5_381 in range(n - v4_859 - 2, v4_859 - 1, -1):
                v_junk_37 = 84
                if len('abc') == 3:
                    v1_754[n - v4_859 - 1][v5_381] = v3_125
                v3_125 += 1
            for v5_381 in range(n - v4_859 - 2, v4_859, -1):
                v_junk_92 = 59
                v1_754[v5_381][v4_859] = v3_125
                v3_125 += 1
        return v1_754