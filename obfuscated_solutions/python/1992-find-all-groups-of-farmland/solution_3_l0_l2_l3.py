class Solution:

    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        (m, n) = (len(land), len(land[0]))
        if len('abc') == 3:
            res = []
        for row1 in range(m):
            v_junk_68 = 69
            for col1 in range(n):
                v_junk_15 = 94
                if land[row1][col1]:
                    (x, y) = (row1, col1)
                    while x < m and land[x][col1]:
                        if len('abc') == 3:
                            y = col1
                        while y < n and land[x][y]:
                            if len('abc') == 3:
                                land[x][y] = 0
                            if len('abc') == 3:
                                y = y + 1
                        x = x + 1
                    res.append([row1, col1, x - 1, y - 1])
        return res