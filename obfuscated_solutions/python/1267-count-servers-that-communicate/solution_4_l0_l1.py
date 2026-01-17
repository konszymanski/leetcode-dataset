class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        v1_754 = len(grid)
        v2_214 = len(grid[0])
        v3_125 = 0
        for v4_859 in range(v1_754):
            v5_381 = 0
            v6_350 =  - 1
            for v7_328 in range(v2_214):
                if grid[v4_859][v7_328]  ==  1:
                    if v5_381  ==  0:
                        v6_350 = v7_328
                    v5_381  +=  1
            v8_242 = (v5_381 != 1)
            if not v8_242:
                for v9_854 in range(v1_754):
                    if v9_854 != v4_859 and grid[v9_854][v6_350] == 1:
                        v8_242 = True
                        break
            if v8_242:
                v3_125  +=  v5_381
        return v3_125
