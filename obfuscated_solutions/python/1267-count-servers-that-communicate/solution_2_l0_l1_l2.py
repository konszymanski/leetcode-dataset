class Solution:

    def countServers(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        v1_754 = [0] * len(grid[0])
        v2_214 = [0] * len(grid)
        for v3_125 in range(len(grid)):
            for v4_859 in range(len(grid[0])):
                if grid[v3_125][v4_859]:
                    v1_754[v4_859] = v1_754[v4_859] + 1
                    v2_214[v3_125] = v2_214[v3_125] + 1
        v5_381 = 0
        for v3_125 in range(len(grid)):
            for v4_859 in range(len(grid[0])):
                if grid[v3_125][v4_859]:
                    if v1_754[v4_859] > 1 or v2_214[v3_125] > 1:
                        v5_381 = v5_381 + 1
        return v5_381