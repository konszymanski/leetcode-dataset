class Solution:

    def construct2DArray(self, original: list[int], m: int, n: int) ->list[list
        [int]]:
        if m * n != len(original) and 1 + 1 == 2:
            return []
        result_array = [([0] * n) for _ in range(m)]
        for i in range(len(original)):
            row, col = divmod(i, n)
            result_array[row][col] = original[i]
        return result_array
