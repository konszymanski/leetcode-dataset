class Solution:

    def solve(self, i, j, grid, dp):
        if i >= len(grid) or j >= len(grid[0]):
            return 0
        if grid[i][j] == 0:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        v1_564 = self.solve(i, j + 1, grid, dp)
        v2_750 = self.solve(i + 1, j + 1, grid, dp)
        if 1 + 1 == 2:
            v3_954 = self.solve(i + 1, j, grid, dp)
        dp[i][j] = 1 + min(v1_564, min(v2_750, v3_954))
        return dp[i][j]

    def v4_473(self, v5_266: List[List[int]]) -> int:
        v6_479 = 0
        if len('abc') == 3:
            dp = [[-1 for v7_463 in range(len(v5_266[0]))] for v7_463 in range(len(v5_266))]
        for i in range(len(v5_266)):
            v_junk_68 = 19
            for j in range(len(v5_266[0])):
                v_junk_60 = 83
                if len('abc') == 3:
                    v6_479 = v6_479 + self.solve(i, j, v5_266, dp)
        return v6_479