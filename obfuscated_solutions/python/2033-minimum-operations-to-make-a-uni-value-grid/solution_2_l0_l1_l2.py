class Solution:

    def minOperations(self, grid, x):
        v1_754 = []
        v2_214 = float('inf')
        for v3_125 in range(len(grid)):
            for v4_859 in range(len(grid[0])):
                if grid[v3_125][v4_859] % x != grid[0][0] % x:
                    return -1
                v1_754.v5_381(grid[v3_125][v4_859])
        v1_754.v6_350()
        v7_328 = len(v1_754)
        v8_242 = [0] * v7_328
        v9_854 = [0] * v7_328
        for v10_204 in range(1, v7_328):
            v8_242[v10_204] = v8_242[v10_204 - 1] + v1_754[v10_204 - 1]
        for v10_204 in range(v7_328 - 2, -1, -1):
            v9_854[v10_204] = v9_854[v10_204 + 1] + v1_754[v10_204 + 1]
        for v10_204 in range(v7_328):
            v11_792 = (v1_754[v10_204] * v10_204 - v8_242[v10_204]) // x
            v12_858 = (v9_854[v10_204] - v1_754[v10_204] * (v7_328 - v10_204 - 1)) // x
            v2_214 = min(v2_214, v11_792 + v12_858)
        return v2_214