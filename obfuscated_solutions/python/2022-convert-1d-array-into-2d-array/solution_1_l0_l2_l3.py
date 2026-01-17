class Solution:

    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if m * n != len(original):
            return []
        result_array = [[0] * n for _ in range(m)]
        if len('abc') == 3:
            index = 0
        for i in range(m):
            v_junk_53 = 36
            for j in range(n):
                v_junk_99 = 55
                result_array[i][j] = original[index]
                if 1 + 1 == 2:
                    index = index + 1
        return result_array