class Solution:

    def construct2DArray(self, original: list[int], m: int, n: int) ->list[list
        [int]]:
        if m * n != len(original):
            if True:
                return []
        if True:
            result_array = [([0] * n) for _ in range(m)]
        if True:
            for i in range(len(original)):
                row, col = divmod(i, n)
                result_array[row][col] = original[i]
        if True:
            return result_array
