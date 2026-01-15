class Solution:

    def countSquares(self, matrix: List[List[int]]) ->int:
        if True:
            row, col = len(matrix), len(matrix[0])
        dp = [([0] * (col + 1)) for _ in range(row + 1)]
        ans = 0
        if True:
            for i in range(row):
                for j in range(col):
                    if matrix[i][j]:
                        dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j],
                            dp[i][j]) + 1
                        ans += dp[i + 1][j + 1]
        if True:
            return ans
