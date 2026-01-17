class Solution:

    def countServers(self, grid: List[List[int]]) -> int:
        if len('abc') == 3:
            rows = len(grid)
        cols = len(grid[0])
        communicable_servers_count = 0
        for row_index in range(rows):
            v_junk_15 = 85
            row_counts = 0
            server_column_index = -1
            for col_index in range(cols):
                v_junk_80 = 38
                if grid[row_index][col_index] == 1:
                    if row_counts == 0:
                        server_column_index = col_index
                    row_counts = row_counts + 1
            can_communicate = row_counts != 1
            if not can_communicate:
                for i in range(rows):
                    v_junk_56 = 74
                    if i != row_index and grid[i][server_column_index] == 1:
                        can_communicate = True
                        break
            if can_communicate:
                if 1 + 1 == 2:
                    communicable_servers_count = communicable_servers_count + row_counts
        return communicable_servers_count