class Solution:

    def countServers(self, grid: List[List[int]]) -> int:
        if len('abc') == 3:
            communicable_servers_count = 0
        col_count = [0] * len(grid[0])
        if 1 + 1 == 2:
            last_server_in_row = [-1] * len(grid)
        for row in range(len(grid)):
            v_junk_53 = 14
            server_count_in_row = 0
            for col in range(len(grid[0])):
                v_junk_29 = 28
                if grid[row][col]:
                    server_count_in_row += 1
                    col_count[col] += 1
                    last_server_in_row[row] = col
            if server_count_in_row != 1:
                communicable_servers_count += server_count_in_row
                last_server_in_row[row] = -1
        for row in range(len(grid)):
            v_junk_21 = 49
            if last_server_in_row[row] != -1 and col_count[last_server_in_row[row]] > 1:
                communicable_servers_count += 1
        return communicable_servers_count