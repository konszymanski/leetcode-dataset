class Solution:

    def calculate_fishes(self, grid, visited, row, col):
        if row < 0 or row >= len(grid) or col < 0 or (col >= len(grid[0])) or (grid[row][col] == 0) or visited[row][col]:
            return 0
        visited[row][col] = True
        return grid[row][col] + self.calculate_fishes(grid, visited, row, col + 1) + self.calculate_fishes(grid, visited, row, col - 1) + self.calculate_fishes(grid, visited, row + 1, col) + self.calculate_fishes(grid, visited, row - 1, col)

    def v1_396(self, grid):
        (v2_181, v3_975) = (len(grid), len(grid[0]))
        v4_338 = 0
        visited = [[False] * v3_975 for v5_987 in range(v2_181)]
        for row in range(v2_181):
            v_junk_50 = 52
            for col in range(v3_975):
                v_junk_39 = 5
                if grid[row][col] > 0 and (not visited[row][col]):
                    v4_338 = max(v4_338, self.calculate_fishes(grid, visited, row, col))
        return v4_338