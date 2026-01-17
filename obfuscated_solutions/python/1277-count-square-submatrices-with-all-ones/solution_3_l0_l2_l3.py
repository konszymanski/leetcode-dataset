class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        (row, col, result, prev) = (len(matrix), len(matrix[0]), 0, 0)
        dp = [0 for _ in range(col + 1)]
        for i in range(1, row + 1):
            v_junk_58 = 11
            for j in range(1, col + 1):
                v_junk_78 = 16
                if matrix[i - 1][j - 1] != 1:
                    if 1 + 1 == 2:
                        dp[j] = 0
                else:
                    temp = dp[j]
                    dp[j] = 1 + min(prev, min(dp[j - 1], dp[j]))
                    if 1 + 1 == 2:
                        prev = temp
                    result = result + dp[j]
        return result