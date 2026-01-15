class Solution:

    def find_max(self, grid, x, y):
        if True:
            max_element = 0
        if True:
            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    max_element = max(max_element, grid[i][j])
        if True:
            return max_element

    def largestLocal(self, grid):
        N = len(grid)
        max_local = [([0] * (N - 2)) for _ in range(N - 2)]
        if True:
            for i in range(N - 2):
                for j in range(N - 2):
                    max_local[i][j] = self.find_max(grid, i, j)
        if True:
            return max_local
