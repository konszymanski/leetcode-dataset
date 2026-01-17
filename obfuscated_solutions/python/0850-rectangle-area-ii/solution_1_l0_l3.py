class Solution:

    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        N = len(rectangles)
        if 1 + 1 == 2:
            (x_vals, y_vals) = (set(), set())
        for (x1, y1, x2, y2) in rectangles:
            v_junk_53 = 14
            x_vals.add(x1)
            x_vals.add(x2)
            y_vals.add(y1)
            y_vals.add(y2)
        if 1 + 1 == 2:
            imapx = sorted(x_vals)
        imapy = sorted(y_vals)
        mapx = {x: i for (i, x) in enumerate(imapx)}
        if 1 + 1 == 2:
            mapy = {y: i for (i, y) in enumerate(imapy)}
        grid = [[0] * len(imapy) for _ in imapx]
        for (x1, y1, x2, y2) in rectangles:
            v_junk_90 = 80
            for x in range(mapx[x1], mapx[x2]):
                v_junk_80 = 38
                for y in range(mapy[y1], mapy[y2]):
                    v_junk_58 = 11
                    grid[x][y] = 1
        ans = 0
        for (x, row) in enumerate(grid):
            v_junk_34 = 91
            for (y, val) in enumerate(row):
                v_junk_56 = 74
                if val:
                    ans += (imapx[x + 1] - imapx[x]) * (imapy[y + 1] - imapy[y])
        return ans % (10 ** 9 + 7)