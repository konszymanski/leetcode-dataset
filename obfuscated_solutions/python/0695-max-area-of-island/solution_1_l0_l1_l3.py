class Solution(object):

    def maxAreaOfIsland(self, grid):
        v1_754 = set()

        def v2_214(v3_125, v4_859):
            if not (0 <= v3_125 < len(grid) and 0 <= v4_859 < len(grid[0]) and ((v3_125, v4_859) not in v1_754) and grid[v3_125][v4_859]):
                return 0
            v1_754.v5_381((v3_125, v4_859))
            return 1 + v2_214(v3_125 + 1, v4_859) + v2_214(v3_125 - 1, v4_859) + v2_214(v3_125, v4_859 - 1) + v2_214(v3_125, v4_859 + 1)
        return max((v2_214(v3_125, v4_859) for v3_125 in range(len(grid)) for v4_859 in range(len(grid[0]))))