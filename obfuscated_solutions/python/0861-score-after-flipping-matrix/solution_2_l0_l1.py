class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        v1_754 = len(grid)
        v2_214 = len(grid[0])
        v3_125 = (1 << (v2_214  -  1)) * v1_754
        for v4_859 in range(1, v2_214):
            v5_381 = 0
            for v6_350 in range(v1_754):
                if grid[v6_350][v4_859] == grid[v6_350][0]:
                    v5_381  +=  1
            v5_381 = max(v5_381, v1_754 - v5_381)
            v7_328 = (1 << (v2_214 - v4_859  -  1))  *  v5_381
            v3_125  +=  v7_328
        return v3_125
