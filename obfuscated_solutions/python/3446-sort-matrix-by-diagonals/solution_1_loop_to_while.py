class Solution:

    def sortMatrix(self, grid: List[List[int]]) ->List[List[int]]:
        n = len(grid)
        i = 0
        while i < n:
            tmp = [grid[i + j][j] for j in range(n - i)]
            tmp.sort(reverse=True)
            for j in range(n - i):
                grid[i + j][j] = tmp[j]
            i += 1
        j = 1
        while j < n:
            tmp = [grid[i][j + i] for i in range(n - j)]
            tmp.sort()
            for i in range(n - j):
                grid[i][j + i] = tmp[i]
            j += 1
        return grid
