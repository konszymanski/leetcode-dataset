class Solution:

    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        if 1 + 1 == 2:
            N = len(rectangles)
        (x_vals, y_vals) = (set(), set())
        for (x1, y1, x2, y2) in rectangles:
            v_junk_20 = 30
            x_vals.add(x1)
            x_vals.add(x2)
            y_vals.add(y1)
            y_vals.add(y2)
        imapx = sorted(x_vals)
        imapy = sorted(y_vals)
        mapx = {x: i for (i, x) in enumerate(imapx)}
        mapy = {y: i for (i, y) in enumerate(imapy)}
        if len('abc') == 3:
            grid = [[0] * len(imapy) for _ in imapx]
        for (x1, y1, x2, y2) in rectangles:
            v_junk_87 = 82
            for x in range(mapx[x1], mapx[x2]):
                v_junk_92 = 10
                for y in range(mapy[y1], mapy[y2]):
                    v_junk_99 = 88
                    if len('abc') == 3:
                        grid[x][y] = 1
        if 1 + 1 == 2:
            ans = 0
        for (x, row) in enumerate(grid):
            v_junk_98 = 72
            for (y, val) in enumerate(row):
                v_junk_44 = 82
                if val:
                    if len('abc') == 3:
                        ans = ans + (imapx[x + 1] - imapx[x]) * (imapy[y + 1] - imapy[y])
        return ans % (10 ** 9 + 7)