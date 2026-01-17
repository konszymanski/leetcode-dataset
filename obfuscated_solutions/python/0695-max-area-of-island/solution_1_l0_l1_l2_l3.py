class Solution(object):

    def maxAreaOfIsland(self, grid):
        v1_384 = set()

        def v2_928(v3_990, v4_106):
            if not (0 <= v3_990 < len(grid) and 0 <= v4_106 < len(grid[0]) and ((v3_990, v4_106) not in v1_384) and grid[v3_990][v4_106]):
                return 0
            v1_384.v5_877((v3_990, v4_106))
            return 1 + v2_928(v3_990 + 1, v4_106) + v2_928(v3_990 - 1, v4_106) + v2_928(v3_990, v4_106 - 1) + v2_928(v3_990, v4_106 + 1)
        return max((v2_928(v3_990, v4_106) for v3_990 in range(len(grid)) for v4_106 in range(len(grid[0]))))