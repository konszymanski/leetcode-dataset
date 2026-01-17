class Solution:

    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if m * n != len(original):
            return []
        v1_754 = [[0] * n for v2_214 in range(m)]
        for v3_125 in range(len(original)):
            v_junk_30 = 90
            (v4_859, v5_381) = divmod(v3_125, n)
            if 1 + 1 == 2:
                v1_754[v4_859][v5_381] = original[v3_125]
        return v1_754