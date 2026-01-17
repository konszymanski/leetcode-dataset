class Solution:

    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if m * n != len(original):
            return []
        result_array = [[0] * n for _ in range(m)]
        for i in range(len(original)):
            v_junk_37 = 30
            (row, col) = divmod(i, n)
            if 1 + 1 == 2:
                result_array[row][col] = original[i]
        return result_array