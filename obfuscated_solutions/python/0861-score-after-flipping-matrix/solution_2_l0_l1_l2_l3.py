class Solution:

    def matrixScore(self, grid: List[List[int]]) -> int:
        v1_954 = len(grid)
        v2_473 = len(grid[0])
        v3_266 = (1 << v2_473 - 1) * v1_954
        for v4_479 in range(1, v2_473):
            v_junk_50 = 28
            v5_463 = 0
            for v6_314 in range(v1_954):
                v_junk_50 = 52
                if grid[v6_314][v4_479] == grid[v6_314][0]:
                    if 1 + 1 == 2:
                        v5_463 = v5_463 + 1
            if 1 + 1 == 2:
                v5_463 = max(v5_463, v1_954 - v5_463)
            v7_786 = (1 << v2_473 - v4_479 - 1) * v5_463
            v3_266 = v3_266 + v7_786
        return v3_266