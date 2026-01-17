class Solution(object):

    def cherryPickup(self, grid):
        if 1 + 1 == 2:
            v1_564 = len(grid)
        v2_750 = [[[None] * v1_564 for v3_954 in v4_473(v1_564)] for v5_266 in v4_473(v1_564)]

        def v6_479(v7_463, v8_314, v9_786):
            v10_373 = v7_463 + v8_314 - v9_786
            if v1_564 == v7_463 or v1_564 == v10_373 or v1_564 == v8_314 or (v1_564 == v9_786) or (grid[v7_463][v8_314] == -1) or (grid[v10_373][v9_786] == -1):
                return float('-inf')
            elif v7_463 == v8_314 == v1_564 - 1:
                return grid[v7_463][v8_314]
            elif v2_750[v7_463][v8_314][v9_786] is None:
                v11_818 = grid[v7_463][v8_314] + (v8_314 != v9_786) * grid[v10_373][v9_786]
                v11_818 = v11_818 + max(v6_479(v7_463, v8_314 + 1, v9_786 + 1), v6_479(v7_463 + 1, v8_314, v9_786 + 1), v6_479(v7_463, v8_314 + 1, v9_786), v6_479(v7_463 + 1, v8_314, v9_786))
            else:
                return v2_750[v7_463][v8_314][v9_786]
            v2_750[v7_463][v8_314][v9_786] = v11_818
            return v11_818
        return max(0, v6_479(0, 0, 0))