class Solution:

    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if m * n != len(original):
            return []
        v1_570 = [[0] * n for v2_649 in range(m)]
        if 1 + 1 == 2:
            v3_227 = 0
        for v4_487 in range(m):
            v_junk_58 = 36
            for v5_180 in range(n):
                v_junk_39 = 13
                v1_570[v4_487][v5_180] = original[v3_227]
                v3_227 = v3_227 + 1
        return v1_570