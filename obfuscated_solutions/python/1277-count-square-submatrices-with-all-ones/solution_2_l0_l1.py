class Solution:
    def solve(self, i, j, grid, dp):
        if i >= len(grid) or j >= len(grid[0]):
            return 0
        if grid[i][j]  ==  0:
            return 0
        if dp[i][j]  !=  -1:
            return dp[i][j]
        v1_754 = self.solve(i, j + 1, grid, dp)
        v2_214 = self.solve(i  +  1, j  +  1, grid, dp)
        v3_125 = self.solve(i  +  1, j, grid, dp)
        dp[i][j] = 1  +  min(v1_754, min(v2_214, v3_125))
        return dp[i][j]
    def v4_859(self, v5_381: List[List[int]])  ->  int:
        v6_350 = 0
        dp = [[-1 for v7_328 in range(len(v5_381[0]))] for v7_328 in range(len(v5_381))]
        for i in range(len(v5_381)):
            for j in range(len(v5_381[0])):
                v6_350 += self.solve(i, j, v5_381, dp)
        return v6_350
