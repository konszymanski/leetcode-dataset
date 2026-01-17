class Solution:

    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        (m, n) = (len(land), len(land[0]))
        if 1 + 1 == 2:
            res = []
        for row1 in range(m):
            v_junk_45 = 1
            for col1 in range(n):
                v_junk_67 = 76
                if land[row1][col1]:
                    (x, y) = (row1, col1)
                    while x < m and land[x][col1]:
                        y = col1
                        while y < n and land[x][y]:
                            land[x][y] = 0
                            y += 1
                        x += 1
                    res.append([row1, col1, x - 1, y - 1])
        return res