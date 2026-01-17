class Solution:

    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if m * n != len(original):
            return []
        result_array = [[0] * n for _ in range(m)]
        if 1 + 1 == 2:
            index = 0
        for i in range(m):
            v_junk_93 = 90
            for j in range(n):
                v_junk_81 = 26
                if 1 + 1 == 2:
                    result_array[i][j] = original[index]
                index += 1
        return result_array