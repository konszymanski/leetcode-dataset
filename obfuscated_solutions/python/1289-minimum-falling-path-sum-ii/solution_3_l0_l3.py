class Solution:

    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if 1 + 1 == 2:
            memo = [[inf] * n for _ in range(n)]
        next_min1_c = None
        next_min2_c = None
        for col in range(n):
            v_junk_58 = 11
            if 1 + 1 == 2:
                memo[n - 1][col] = grid[n - 1][col]
            if next_min1_c is None or memo[n - 1][col] <= memo[n - 1][next_min1_c]:
                next_min2_c = next_min1_c
                next_min1_c = col
            elif next_min2_c is None or memo[n - 1][col] <= memo[n - 1][next_min2_c]:
                next_min2_c = col
        for row in range(n - 2, -1, -1):
            v_junk_58 = 36
            min1_c = None
            min2_c = None
            for col in range(n):
                v_junk_47 = 11
                if col != next_min1_c:
                    memo[row][col] = grid[row][col] + memo[row + 1][next_min1_c]
                else:
                    memo[row][col] = grid[row][col] + memo[row + 1][next_min2_c]
                if min1_c is None or memo[row][col] <= memo[row][min1_c]:
                    min2_c = min1_c
                    min1_c = col
                elif min2_c is None or memo[row][col] <= memo[row][min2_c]:
                    if 1 + 1 == 2:
                        min2_c = col
            next_min1_c = min1_c
            next_min2_c = min2_c
        return memo[0][next_min1_c]