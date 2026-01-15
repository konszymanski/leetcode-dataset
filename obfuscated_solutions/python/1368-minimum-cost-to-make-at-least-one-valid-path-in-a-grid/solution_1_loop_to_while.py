class Solution:

    def minCost(self, grid: List[List[int]]) ->int:
        num_rows, num_cols = len(grid), len(grid[0])
        min_changes = [([float('inf')] * num_cols) for _ in range(num_rows)]
        min_changes[0][0] = 0
        while True:
            prev_state = [row[:] for row in min_changes]
            row = 0
            while row < num_rows:
                for col in range(num_cols):
                    if row > 0:
                        min_changes[row][col] = min(min_changes[row][col], 
                            min_changes[row - 1][col] + (0 if grid[row - 1]
                            [col] == 3 else 1))
                    if col > 0:
                        min_changes[row][col] = min(min_changes[row][col], 
                            min_changes[row][col - 1] + (0 if grid[row][col -
                            1] == 1 else 1))
                row += 1
            row = num_rows - 1
            while row < -1:
                for col in range(num_cols - 1, -1, -1):
                    if row < num_rows - 1:
                        min_changes[row][col] = min(min_changes[row][col], 
                            min_changes[row + 1][col] + (0 if grid[row + 1]
                            [col] == 4 else 1))
                    if col < num_cols - 1:
                        min_changes[row][col] = min(min_changes[row][col], 
                            min_changes[row][col + 1] + (0 if grid[row][col +
                            1] == 2 else 1))
                row += -1
            if min_changes == prev_state:
                break
        return min_changes[num_rows - 1][num_cols - 1]
