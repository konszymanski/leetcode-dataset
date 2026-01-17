class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        v1_754, v2_214 = len(grid), len(grid[0])
        v3_125 = [[float("inf")] * v2_214 for v4_859 in range(v1_754)]
        v3_125[0][0] = 0
        while True:
            v5_381 = [v6_350[:] for v6_350 in v3_125]
            for v6_350 in range(v1_754):
                for v7_328 in range(v2_214):
                    if v6_350 > 0:
                        v3_125[v6_350][v7_328] = min(
                            v3_125[v6_350][v7_328],
                            v3_125[v6_350  -  1][v7_328]
                             +  (0 if grid[v6_350  -  1][v7_328] == 3 else 1),
                        )
                    if v7_328  >  0:
                        v3_125[v6_350][v7_328] = min(
                            v3_125[v6_350][v7_328],
                            v3_125[v6_350][v7_328 - 1]
                            + (0 if grid[v6_350][v7_328 - 1]  ==  1 else 1),
                        )
            for v6_350 in range(v1_754  -  1,  - 1, -1):
                for v7_328 in range(v2_214 - 1, -1, -1):
                    if v6_350  <  v1_754 - 1:
                        v3_125[v6_350][v7_328] = min(
                            v3_125[v6_350][v7_328],
                            v3_125[v6_350 + 1][v7_328]
                            + (0 if grid[v6_350 + 1][v7_328]  ==  4 else 1),
                        )
                    if v7_328 < v2_214 - 1:
                        v3_125[v6_350][v7_328] = min(
                            v3_125[v6_350][v7_328],
                            v3_125[v6_350][v7_328 + 1]
                            + (0 if grid[v6_350][v7_328  +  1]  ==  2 else 1),
                        )
            if v3_125 == v5_381:
                break
        return v3_125[v1_754 - 1][v2_214 - 1]
