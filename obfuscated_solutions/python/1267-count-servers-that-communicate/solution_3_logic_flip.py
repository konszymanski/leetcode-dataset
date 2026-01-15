class Solution:

    def countServers(self, grid: List[List[int]]) ->int:
        communicable_servers_count = 0
        col_count = [0] * len(grid[0])
        last_server_in_row = [-1] * len(grid)
        for row in range(len(grid)):
            server_count_in_row = 0
            for col in range(len(grid[0])):
                if grid[row][col]:
                    server_count_in_row += 1
                    col_count[col] += 1
                    last_server_in_row[row] = col
            if server_count_in_row != 1:
                communicable_servers_count += server_count_in_row
                last_server_in_row[row] = -1
        for row in range(len(grid)):
            if last_server_in_row[row] != -1 and col_count[last_server_in_row
                [row]] > 1:
                communicable_servers_count += 1
        return communicable_servers_count
