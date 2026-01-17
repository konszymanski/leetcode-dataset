class Solution:

    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if m * n != len(original):
            return []
        if len('abc') == 3:
            v1_754 = [[0] * n for v2_214 in range(m)]
        if len('abc') == 3:
            v3_125 = 0
        for v4_859 in range(m):
            v_junk_15 = 94
            for v5_381 in range(n):
                v_junk_87 = 34
                if len('abc') == 3:
                    v1_754[v4_859][v5_381] = original[v3_125]
                v3_125 += 1
        return v1_754