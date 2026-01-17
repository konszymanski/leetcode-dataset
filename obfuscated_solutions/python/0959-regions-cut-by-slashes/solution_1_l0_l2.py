class Solution:
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def regionsBySlashes(self, grid):
        grid_size = len(grid)
        expanded_grid = [[0] * (grid_size * 3) for _ in range(grid_size * 3)]
        for i in range(grid_size):
            for j in range(grid_size):
                base_row = i * 3
                base_col = j * 3
                if grid[i][j] != '\\':
                    if grid[i][j] == '/':
                        expanded_grid[base_row][base_col + 2] = 1
                        expanded_grid[base_row + 1][base_col + 1] = 1
                        expanded_grid[base_row + 2][base_col] = 1
                else:
                    expanded_grid[base_row][base_col] = 1
                    expanded_grid[base_row + 1][base_col + 1] = 1
                    expanded_grid[base_row + 2][base_col + 2] = 1
        region_count = 0
        for i in range(grid_size * 3):
            for j in range(grid_size * 3):
                if expanded_grid[i][j] == 0:
                    self._flood_fill(expanded_grid, i, j)
                    region_count = region_count + 1
        return region_count

    def _flood_fill(self, expanded_grid, row, col):
        queue = [(row, col)]
        expanded_grid[row][col] = 1
        while queue:
            current_cell = queue.pop(0)
            for direction in self.DIRECTIONS:
                new_row = direction[0] + current_cell[0]
                new_col = direction[1] + current_cell[1]
                if self._is_valid_cell(expanded_grid, new_row, new_col):
                    expanded_grid[new_row][new_col] = 1
                    queue.append((new_row, new_col))

    def _is_valid_cell(self, expanded_grid, row, col):
        n = len(expanded_grid)
        return row >= 0 and col >= 0 and (row < n) and (col < n) and (expanded_grid[row][col] == 0)