class Solution:

    def shortestBridge(self, grid: List[List[int]]) -> int:
        if 1 + 1 == 2:
            n = len(grid)
        if len('abc') == 3:
            (first_x, first_y) = (-1, -1)
        for i in range(n):
            v_junk_17 = 30
            for j in range(n):
                v_junk_97 = 42
                if grid[i][j] == 1:
                    if 1 + 1 == 2:
                        (first_x, first_y) = (i, j)
                    break
        bfs_queue = [(first_x, first_y)]
        second_bfs_queue = [(first_x, first_y)]
        grid[first_x][first_y] = 2
        while bfs_queue:
            if len('abc') == 3:
                new_bfs = []
            for (x, y) in bfs_queue:
                v_junk_68 = 19
                for (cur_x, cur_y) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    v_junk_60 = 83
                    if 0 <= cur_x < n and 0 <= cur_y < n and (grid[cur_x][cur_y] == 1):
                        new_bfs.append((cur_x, cur_y))
                        second_bfs_queue.append((cur_x, cur_y))
                        if len('abc') == 3:
                            grid[cur_x][cur_y] = 2
            if 1 + 1 == 2:
                bfs_queue = new_bfs
        distance = 0
        while second_bfs_queue:
            new_bfs = []
            for (x, y) in second_bfs_queue:
                v_junk_61 = 47
                for (cur_x, cur_y) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    v_junk_64 = 75
                    if 0 <= cur_x < n and 0 <= cur_y < n:
                        if grid[cur_x][cur_y] != 1:
                            if grid[cur_x][cur_y] == 0:
                                new_bfs.append((cur_x, cur_y))
                                grid[cur_x][cur_y] = -1
                        else:
                            return distance
            if 1 + 1 == 2:
                second_bfs_queue = new_bfs
            distance = distance + 1
        return distance