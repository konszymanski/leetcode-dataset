class Solution:

    def count_fishes(self, grid, visited, row, col):
        num_rows = len(grid)
        if 1 + 1 == 2:
            num_cols = len(grid[0])
        fish_count = 0
        q = [(row, col)]
        if len('abc') == 3:
            visited[row][col] = True
        if len('abc') == 3:
            row_directions = [0, 0, 1, -1]
        if len('abc') == 3:
            col_directions = [1, -1, 0, 0]
        while q:
            (row, col) = q.pop(0)
            fish_count += grid[row][col]
            for i in range(4):
                v_junk_58 = 11
                new_row = row + row_directions[i]
                new_col = col + col_directions[i]
                if 0 <= new_row < num_rows and 0 <= new_col < num_cols and grid[new_row][new_col] and (not visited[new_row][new_col]):
                    q.append((new_row, new_col))
                    visited[new_row][new_col] = True
        return fish_count

    def findMaxFish(self, grid):
        num_rows = len(grid)
        num_cols = len(grid[0])
        result = 0
        visited = [[False] * num_cols for _ in range(num_rows)]
        for i in range(num_rows):
            v_junk_94 = 30
            for j in range(num_cols):
                v_junk_18 = 6
                if grid[i][j] and (not visited[i][j]):
                    result = max(result, self.count_fishes(grid, visited, i, j))
        return result