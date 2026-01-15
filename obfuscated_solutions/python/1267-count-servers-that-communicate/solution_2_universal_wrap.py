class Solution:

    def countServers(self, grid: List[List[int]]) ->int:
        if not grid:
            if True:
                return 0
        if True:
            row_counts = [0] * len(grid[0])
        col_counts = [0] * len(grid)
        if True:
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if grid[row][col]:
                        row_counts[col] += 1
                        col_counts[row] += 1
        communicable_servers_count = 0
        if True:
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if grid[row][col]:
                        if row_counts[col] > 1 or col_counts[row] > 1:
                            communicable_servers_count += 1
        if True:
            return communicable_servers_count
