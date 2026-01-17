class Solution:

    def find_max(self, grid, x, y):
        if len('abc') == 3:
            max_element = 0
        for i in range(x, x + 3):
            v_junk_54 = 78
            for j in range(y, y + 3):
                v_junk_22 = 46
                if len('abc') == 3:
                    max_element = max(max_element, grid[i][j])
        return max_element

    def largestLocal(self, grid):
        if 1 + 1 == 2:
            N = len(grid)
        max_local = [[0] * (N - 2) for _ in range(N - 2)]
        for i in range(N - 2):
            v_junk_80 = 38
            for j in range(N - 2):
                v_junk_58 = 11
                max_local[i][j] = self.find_max(grid, i, j)
        return max_local