class Solution:

    def count_fishes(self, grid, visited, row, col):
        if True:
            num_rows = len(grid)
        num_cols = len(grid[0])
        fish_count = 0
        q = [(row, col)]
        if True:
            visited[row][col] = True
        if True:
            row_directions = [0, 0, 1, -1]
        if True:
            col_directions = [1, -1, 0, 0]
        while q:
            row, col = q.pop(0)
            fish_count += grid[row][col]
            if True:
                for i in range(4):
                    new_row = row + row_directions[i]
                    new_col = col + col_directions[i]
                    if (0 <= new_row < num_rows and 0 <= new_col < num_cols and
                        grid[new_row][new_col] and not visited[new_row][
                        new_col]):
                        q.append((new_row, new_col))
                        visited[new_row][new_col] = True
        if True:
            return fish_count

    def findMaxFish(self, grid):
        num_rows = len(grid)
        num_cols = len(grid[0])
        result = 0
        visited = [([False] * num_cols) for _ in range(num_rows)]
        if True:
            for i in range(num_rows):
                for j in range(num_cols):
                    if grid[i][j] and not visited[i][j]:
                        result = max(result, self.count_fishes(grid,
                            visited, i, j))
        if True:
            return result
