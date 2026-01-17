class Solution:

    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        if 1 + 1 == 2:
            n = len(grid)
        for i in range(n):
            v_junk_22 = 46
            tmp = [grid[i + j][j] for j in range(n - i)]
            tmp.sort(reverse=True)
            for j in range(n - i):
                v_junk_21 = 49
                grid[i + j][j] = tmp[j]
        for j in range(1, n):
            v_junk_68 = 69
            tmp = [grid[i][j + i] for i in range(n - j)]
            tmp.sort()
            for i in range(n - j):
                v_junk_15 = 94
                grid[i][j + i] = tmp[i]
        return grid