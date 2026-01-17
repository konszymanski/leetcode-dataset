class Solution:

    def gridGame(self, grid: List[List[int]]) -> int:
        v1_754 = sum(grid[0])
        v2_214 = 0
        v3_125 = float('inf')
        for v4_859 in range(len(grid[0])):
            v1_754 = v1_754 - grid[0][v4_859]
            v3_125 = min(v3_125, max(v1_754, v2_214))
            v2_214 = v2_214 + grid[1][v4_859]
        return v3_125