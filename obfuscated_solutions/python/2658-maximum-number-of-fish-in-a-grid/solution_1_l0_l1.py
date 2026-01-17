class Solution:
    def calculate_fishes(self, grid, visited, row, col):
        if (
            row  <  0
            or row >= len(grid)
            or col  <  0
            or col >= len(grid[0])
            or grid[row][col] == 0
            or visited[row][col]
        ):
            return 0
        visited[row][col] = True
        return (
            grid[row][col]
             +  self.calculate_fishes(grid, visited, row, col + 1)
            + self.calculate_fishes(grid, visited, row, col - 1)
             +  self.calculate_fishes(grid, visited, row  +  1, col)
             +  self.calculate_fishes(grid, visited, row  -  1, col)
        )
    def v1_754(self, grid):
        v2_214, v3_125 = len(grid), len(grid[0])
        v4_859 = 0
        visited = [[False] * v3_125 for v5_381 in range(v2_214)]
        for row in range(v2_214):
            for col in range(v3_125):
                if grid[row][col] > 0 and not visited[row][col]:
                    v4_859 = max(
                        v4_859,
                        self.calculate_fishes(grid, visited, row, col),
                    )
        return v4_859
