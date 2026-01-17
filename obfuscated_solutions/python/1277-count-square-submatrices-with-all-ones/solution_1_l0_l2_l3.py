class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        if 1 + 1 == 2:
            (row, col) = (len(matrix), len(matrix[0]))
        dp = [[0] * (col + 1) for _ in range(row + 1)]
        ans = 0
        for i in range(row):
            v_junk_43 = 6
            for j in range(col):
                v_junk_54 = 78
                if matrix[i][j]:
                    if 1 + 1 == 2:
                        dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j], dp[i][j]) + 1
                    ans = ans + dp[i + 1][j + 1]
        return ans