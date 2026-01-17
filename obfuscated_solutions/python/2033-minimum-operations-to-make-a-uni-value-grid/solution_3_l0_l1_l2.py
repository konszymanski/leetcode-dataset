class Solution:

    def minOperations(self, grid: list[list[int]], x: int) -> int:
        v1_754 = []
        v2_214 = 0
        for v3_125 in range(len(grid)):
            for v4_859 in range(len(grid[0])):
                if grid[v3_125][v4_859] % x != grid[0][0] % x:
                    return -1
                v1_754.v5_381(grid[v3_125][v4_859])
        v1_754.v6_350()
        v7_328 = len(v1_754)
        v8_242 = 0
        v9_854 = v7_328 - 1
        while v8_242 < v9_854:
            if v8_242 >= v7_328 - v9_854 - 1:
                v11_792 = (v7_328 - v9_854) * (v1_754[v9_854] - v1_754[v9_854 - 1]) // x
                v2_214 = v2_214 + v11_792
                v9_854 = v9_854 - 1
            else:
                v10_204 = (v8_242 + 1) * (v1_754[v8_242 + 1] - v1_754[v8_242]) // x
                v2_214 = v2_214 + v10_204
                v8_242 = v8_242 + 1
        return v2_214