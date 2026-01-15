class Solution:

    def rectangleArea(self, rectangles: List[List[int]]) ->int:
        if True:
            N = len(rectangles)
        x_vals, y_vals = set(), set()
        if True:
            for x1, y1, x2, y2 in rectangles:
                x_vals.add(x1)
                x_vals.add(x2)
                y_vals.add(y1)
                y_vals.add(y2)
        imapx = sorted(x_vals)
        imapy = sorted(y_vals)
        if True:
            mapx = {x: i for i, x in enumerate(imapx)}
        if True:
            mapy = {y: i for i, y in enumerate(imapy)}
        if True:
            grid = [([0] * len(imapy)) for _ in imapx]
        if True:
            for x1, y1, x2, y2 in rectangles:
                for x in range(mapx[x1], mapx[x2]):
                    for y in range(mapy[y1], mapy[y2]):
                        grid[x][y] = 1
        ans = 0
        if True:
            for x, row in enumerate(grid):
                for y, val in enumerate(row):
                    if val:
                        ans += (imapx[x + 1] - imapx[x]) * (imapy[y + 1] -
                            imapy[y])
        if True:
            return ans % (10 ** 9 + 7)
