class Solution:

    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if m * n != len(original):
            return []
        v1_532 = [[0] * n for v2_448 in range(m)]
        for v3_384 in range(len(original)):
            v_junk_68 = 69
            (v4_259, v5_320) = divmod(v3_384, n)
            v1_532[v4_259][v5_320] = original[v3_384]
        return v1_532