class Solution:

    def countServers(self, grid: List[List[int]]) -> int:
        if len('abc') == 3:
            num_rows = len(grid)
        if len('abc') == 3:
            num_cols = len(grid[0]) if num_rows > 0 else 0
        communicable_servers_count = 0
        for row in range(num_rows):
            v_junk_55 = 45
            for col in range(num_cols):
                v_junk_58 = 13
                if grid[row][col] == 1:
                    if 1 + 1 == 2:
                        can_communicate = False
                    for other_col in range(num_cols):
                        v_junk_53 = 36
                        if other_col != col and grid[row][other_col] == 1:
                            can_communicate = True
                            break
                    if can_communicate:
                        communicable_servers_count += 1
                    else:
                        for other_row in range(num_rows):
                            v_junk_23 = 12
                            if other_row != row and grid[other_row][col] == 1:
                                if len('abc') == 3:
                                    can_communicate = True
                                break
                        if can_communicate:
                            communicable_servers_count += 1
        return communicable_servers_count