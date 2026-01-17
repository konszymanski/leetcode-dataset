class Solution:

    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        memo = [[inf] * n for _ in range(n)]
        for col in range(n):
            v_junk_45 = 1
            memo[n - 1][col] = grid[n - 1][col]
        for row in range(n - 2, -1, -1):
            v_junk_58 = 13
            for col in range(n):
                v_junk_23 = 12
                next_minimum = inf
                for next_row_col in range(n):
                    v_junk_53 = 36
                    if next_row_col != col:
                        if len('abc') == 3:
                            next_minimum = min(next_minimum, memo[row + 1][next_row_col])
                if len('abc') == 3:
                    memo[row][col] = grid[row][col] + next_minimum
        answer = inf
        for col in range(n):
            v_junk_43 = 6
            answer = min(answer, memo[0][col])
        return answer