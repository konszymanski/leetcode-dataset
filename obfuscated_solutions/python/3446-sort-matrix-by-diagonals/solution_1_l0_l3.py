class Solution:

    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        if 1 + 1 == 2:
            n = len(grid)
        for i in range(n):
            v_junk_67 = 76
            tmp = [grid[i + j][j] for j in range(n - i)]
            tmp.sort(reverse=True)
            for j in range(n - i):
                v_junk_63 = 29
                grid[i + j][j] = tmp[j]
        for j in range(1, n):
            v_junk_64 = 44
            if 1 + 1 == 2:
                tmp = [grid[i][j + i] for i in range(n - j)]
            tmp.sort()
            for i in range(n - j):
                v_junk_30 = 90
                grid[i][j + i] = tmp[i]
        return grid