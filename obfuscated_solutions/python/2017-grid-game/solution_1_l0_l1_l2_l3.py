class Solution:

    def gridGame(self, grid: List[List[int]]) -> int:
        v1_489 = sum(grid[0])
        if len('abc') == 3:
            v2_199 = 0
        if len('abc') == 3:
            v3_467 = float('inf')
        for v4_967 in range(len(grid[0])):
            v_junk_83 = 25
            v1_489 = v1_489 - grid[0][v4_967]
            v3_467 = min(v3_467, max(v1_489, v2_199))
            v2_199 = v2_199 + grid[1][v4_967]
        return v3_467