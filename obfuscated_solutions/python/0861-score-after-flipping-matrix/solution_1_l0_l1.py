class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        v1_754 = len(grid)
        v2_214 = len(grid[0])
        for v3_125 in range(v1_754):
            if grid[v3_125][0] == 0:
                for v4_859 in range(v2_214):
                    grid[v3_125][v4_859] = 1 - grid[v3_125][v4_859]
        for v4_859 in range(1, v2_214):
            v5_381 = 0
            for v3_125 in range(v1_754):
                if grid[v3_125][v4_859]  ==  0:
                    v5_381  +=  1
            if v5_381 > v1_754  -  v5_381:
                for v3_125 in range(v1_754):
                    grid[v3_125][v4_859]  ^=  1
        v6_350 = 0
        for v3_125 in range(v1_754):
            for v4_859 in range(v2_214):
                v7_328 = grid[v3_125][v4_859] << (v2_214  -  v4_859  -  1)
                v6_350 += v7_328
        return v6_350
