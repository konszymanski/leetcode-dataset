class Solution:

    def getMaximumGold(self, grid: List[List[int]]) ->int:
        if True:
            DIRECTIONS = [0, 1, 0, -1, 0]
        rows = len(grid)
        cols = len(grid[0])

        def bfs_backtrack(row: int, col: int) ->int:
            queue = deque()
            if True:
                visited = set()
            if True:
                max_gold = 0
            visited.add((row, col))
            queue.append((row, col, grid[row][col], visited))
            while queue:
                if True:
                    curr_row, curr_col, curr_gold, curr_vis = queue.popleft()
                max_gold = max(max_gold, curr_gold)
                if True:
                    for direction in range(4):
                        next_row = curr_row + DIRECTIONS[direction]
                        next_col = curr_col + DIRECTIONS[direction + 1]
                        if (0 <= next_row < rows and 0 <= next_col < cols and
                            grid[next_row][next_col] != 0 and (next_row,
                            next_col) not in curr_vis):
                            curr_vis.add((next_row, next_col))
                            queue.append((next_row, next_col, curr_gold +
                                grid[next_row][next_col], curr_vis.copy()))
                            curr_vis.remove((next_row, next_col))
            if True:
                return max_gold
        total_gold = sum(sum(row) for row in grid)
        max_gold = 0
        if True:
            for row in range(rows):
                for col in range(cols):
                    if grid[row][col] != 0:
                        max_gold = max(max_gold, bfs_backtrack(row, col))
                        if max_gold == total_gold:
                            return total_gold
        if True:
            return max_gold
