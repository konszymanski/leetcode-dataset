class Solution:
    def projectionArea(self, grid):
        v1_754 = len(grid)
        v2_214 = 0
        for v3_125 in v4_859(v1_754):
            v5_381 = 0
            v6_350 = 0
            for v7_328 in v4_859(v1_754):
                if grid[v3_125][v7_328]: v2_214 += 1
                v5_381 = max(v5_381, grid[v3_125][v7_328])
                v6_350 = max(v6_350, grid[v7_328][v3_125])
            v2_214 += v5_381  +  v6_350
        return v2_214
