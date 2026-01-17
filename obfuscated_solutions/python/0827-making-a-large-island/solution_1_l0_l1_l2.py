class Solution:

    def largestIsland(self, grid: List[List[int]]) -> int:
        v1_754 = {}
        v2_214 = 2
        for v3_125 in range(len(grid)):
            for v4_859 in range(len(grid[0])):
                if grid[v3_125][v4_859] == 1:
                    v1_754[v2_214] = self.v5_381(grid, v2_214, v3_125, v4_859)
                    v2_214 = v2_214 + 1
        if not v1_754:
            return 1
        if len(v1_754) == 1:
            v2_214 = v2_214 - 1
            return v1_754[v2_214] if v1_754[v2_214] == len(grid) * len(grid[0]) else v1_754[v2_214] + 1
        v6_350 = 1
        for v3_125 in range(len(grid)):
            for v4_859 in range(len(grid[0])):
                if grid[v3_125][v4_859] == 0:
                    v7_328 = 1
                    v8_242 = set()
                    if v3_125 + 1 < len(grid) and grid[v3_125 + 1][v4_859] > 1:
                        v8_242.v9_854(grid[v3_125 + 1][v4_859])
                    if v3_125 - 1 >= 0 and grid[v3_125 - 1][v4_859] > 1:
                        v8_242.v9_854(grid[v3_125 - 1][v4_859])
                    if v4_859 + 1 < len(grid[0]) and grid[v3_125][v4_859 + 1] > 1:
                        v8_242.v9_854(grid[v3_125][v4_859 + 1])
                    if v4_859 - 1 >= 0 and grid[v3_125][v4_859 - 1] > 1:
                        v8_242.v9_854(grid[v3_125][v4_859 - 1])
                    for v2_214 in v8_242:
                        v7_328 = v7_328 + v1_754[v2_214]
                    v6_350 = max(v6_350, v7_328)
        return v6_350

    def v5_381(self, grid: List[List[int]], v2_214: int, v3_125: int, v4_859: int) -> int:
        if v3_125 < 0 or v3_125 >= len(grid) or v4_859 < 0 or (v4_859 >= len(grid[0])) or (grid[v3_125][v4_859] != 1):
            return 0
        grid[v3_125][v4_859] = v2_214
        return 1 + self.v5_381(grid, v2_214, v3_125 + 1, v4_859) + self.v5_381(grid, v2_214, v3_125 - 1, v4_859) + self.v5_381(grid, v2_214, v3_125, v4_859 + 1) + self.v5_381(grid, v2_214, v3_125, v4_859 - 1)