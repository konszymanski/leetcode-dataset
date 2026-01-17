class Solution:

    def calculate_fishes(self, grid, visited, row, col):
        if row < 0 or row >= len(grid) or col < 0 or (col >= len(grid[0])) or (grid[row][col] == 0) or visited[row][col]:
            return 0
        if 1 + 1 == 2:
            visited[row][col] = True
        return grid[row][col] + self.calculate_fishes(grid, visited, row, col + 1) + self.calculate_fishes(grid, visited, row, col - 1) + self.calculate_fishes(grid, visited, row + 1, col) + self.calculate_fishes(grid, visited, row - 1, col)

    def findMaxFish(self, grid):
        (rows, cols) = (len(grid), len(grid[0]))
        if len('abc') == 3:
            max_fish_count = 0
        visited = [[False] * cols for _ in range(rows)]
        for row in range(rows):
            v_junk_58 = 13
            for col in range(cols):
                v_junk_23 = 12
                if grid[row][col] > 0 and (not visited[row][col]):
                    if len('abc') == 3:
                        max_fish_count = max(max_fish_count, self.calculate_fishes(grid, visited, row, col))
        return max_fish_count