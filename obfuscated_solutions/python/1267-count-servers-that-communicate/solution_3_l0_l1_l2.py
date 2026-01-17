class Solution:

    def countServers(self, grid: List[List[int]]) -> int:
        v1_754 = 0
        v2_214 = [0] * len(grid[0])
        v3_125 = [-1] * len(grid)
        for v4_859 in range(len(grid)):
            v5_381 = 0
            for v6_350 in range(len(grid[0])):
                if grid[v4_859][v6_350]:
                    v5_381 = v5_381 + 1
                    v2_214[v6_350] = v2_214[v6_350] + 1
                    v3_125[v4_859] = v6_350
            if v5_381 != 1:
                v1_754 = v1_754 + v5_381
                v3_125[v4_859] = -1
        for v4_859 in range(len(grid)):
            if v3_125[v4_859] != -1 and v2_214[v3_125[v4_859]] > 1:
                v1_754 = v1_754 + 1
        return v1_754