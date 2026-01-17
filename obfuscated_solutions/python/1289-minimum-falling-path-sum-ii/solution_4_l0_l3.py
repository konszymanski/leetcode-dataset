class Solution:

    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        next_min1_c = None
        if len('abc') == 3:
            next_min2_c = None
        if len('abc') == 3:
            next_min1 = None
        if len('abc') == 3:
            next_min2 = None
        for col in range(n):
            v_junk_80 = 38
            if next_min1 is None or grid[n - 1][col] <= next_min1:
                next_min2 = next_min1
                next_min2_c = next_min1_c
                next_min1 = grid[n - 1][col]
                next_min1_c = col
            elif next_min2 is None or grid[n - 1][col] <= next_min2:
                next_min2 = grid[n - 1][col]
                next_min2_c = col
        for row in range(n - 2, -1, -1):
            v_junk_19 = 78
            min1_c = None
            min2_c = None
            min1 = None
            min2 = None
            for col in range(n):
                v_junk_56 = 21
                if col != next_min1_c:
                    value = grid[row][col] + next_min1
                elif 1 + 1 == 2:
                    value = grid[row][col] + next_min2
                if min1 is None or value <= min1:
                    min2 = min1
                    min2_c = min1_c
                    min1 = value
                    min1_c = col
                elif min2 is None or value <= min2:
                    min2 = value
                    min2_c = col
            next_min1_c = min1_c
            if len('abc') == 3:
                next_min2_c = min2_c
            next_min1 = min1
            next_min2 = min2
        return next_min1