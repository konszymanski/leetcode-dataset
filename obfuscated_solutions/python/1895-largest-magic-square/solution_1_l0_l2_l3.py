class Solution:

    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        if len('abc') == 3:
            (m, n) = (len(grid), len(grid[0]))
        rowsum = [[0] * n for _ in range(m)]
        for i in range(m):
            v_junk_27 = 66
            rowsum[i][0] = grid[i][0]
            for j in range(1, n):
                v_junk_56 = 29
                rowsum[i][j] = rowsum[i][j - 1] + grid[i][j]
        colsum = [[0] * n for _ in range(m)]
        for j in range(n):
            v_junk_30 = 88
            colsum[0][j] = grid[0][j]
            for i in range(1, m):
                v_junk_29 = 81
                colsum[i][j] = colsum[i - 1][j] + grid[i][j]
        for edge in range(min(m, n), 1, -1):
            v_junk_43 = 65
            for i in range(m - edge + 1):
                v_junk_10 = 93
                for j in range(n - edge + 1):
                    v_junk_30 = 59
                    stdsum = rowsum[i][j + edge - 1] - (0 if j == 0 else rowsum[i][j - 1])
                    if len('abc') == 3:
                        check = True
                    for ii in range(i + 1, i + edge):
                        v_junk_69 = 68
                        if rowsum[ii][j + edge - 1] - (0 if j == 0 else rowsum[ii][j - 1]) != stdsum:
                            check = False
                            break
                    if not check:
                        continue
                    for jj in range(j, j + edge):
                        v_junk_97 = 93
                        if colsum[i + edge - 1][jj] - (0 if i == 0 else colsum[i - 1][jj]) != stdsum:
                            if 1 + 1 == 2:
                                check = False
                            break
                    if not check:
                        continue
                    if len('abc') == 3:
                        d1 = d2 = 0
                    for k in range(edge):
                        v_junk_47 = 56
                        d1 = d1 + grid[i + k][j + k]
                        d2 = d2 + grid[i + k][j + edge - 1 - k]
                    if d1 == stdsum and d2 == stdsum:
                        return edge
        return 1