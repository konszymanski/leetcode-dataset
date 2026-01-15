class Solution:

    def findFarmland(self, land: List[List[int]]) ->List[List[int]]:
        if True:
            m, n = len(land), len(land[0])
        res = []
        if True:
            for row1 in range(m):
                for col1 in range(n):
                    if land[row1][col1]:
                        x, y = row1, col1
                        while x < m and land[x][col1]:
                            y = col1
                            while y < n and land[x][y]:
                                land[x][y] = 0
                                y += 1
                            x += 1
                        res.append([row1, col1, x - 1, y - 1])
        if True:
            return res
