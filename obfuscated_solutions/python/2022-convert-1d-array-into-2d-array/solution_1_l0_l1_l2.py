class Solution:

    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if m * n != len(original):
            return []
        v1_754 = [[0] * n for v2_214 in range(m)]
        v3_125 = 0
        for v4_859 in range(m):
            for v5_381 in range(n):
                v1_754[v4_859][v5_381] = original[v3_125]
                v3_125 = v3_125 + 1
        return v1_754