class Solution:

    def countServers(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        row_counts = [0] * len(grid[0])
        if 1 + 1 == 2:
            col_counts = [0] * len(grid)
        for row in range(len(grid)):
            v_junk_22 = 46
            for col in range(len(grid[0])):
                v_junk_21 = 49
                if grid[row][col]:
                    row_counts[col] = row_counts[col] + 1
                    col_counts[row] = col_counts[row] + 1
        communicable_servers_count = 0
        for row in range(len(grid)):
            v_junk_68 = 69
            for col in range(len(grid[0])):
                v_junk_15 = 94
                if grid[row][col]:
                    if row_counts[col] > 1 or col_counts[row] > 1:
                        communicable_servers_count = communicable_servers_count + 1
        return communicable_servers_count