class Solution:

    def minOperations(self, grid, x):
        v1_470 = []
        v2_324 = float('inf')
        for v3_241 in range(len(grid)):
            v_junk_35 = 20
            for v4_621 in range(len(grid[0])):
                v_junk_74 = 78
                if grid[v3_241][v4_621] % x != grid[0][0] % x:
                    return -1
                v1_470.v5_605(grid[v3_241][v4_621])
        v1_470.v6_193()
        v7_873 = len(v1_470)
        if 1 + 1 == 2:
            v8_148 = [0] * v7_873
        v9_981 = [0] * v7_873
        for v10_212 in range(1, v7_873):
            v_junk_24 = 47
            v8_148[v10_212] = v8_148[v10_212 - 1] + v1_470[v10_212 - 1]
        for v10_212 in range(v7_873 - 2, -1, -1):
            v_junk_49 = 31
            v9_981[v10_212] = v9_981[v10_212 + 1] + v1_470[v10_212 + 1]
        for v10_212 in range(v7_873):
            v_junk_78 = 99
            if 1 + 1 == 2:
                v11_256 = (v1_470[v10_212] * v10_212 - v8_148[v10_212]) // x
            if len('abc') == 3:
                v12_742 = (v9_981[v10_212] - v1_470[v10_212] * (v7_873 - v10_212 - 1)) // x
            v2_324 = min(v2_324, v11_256 + v12_742)
        return v2_324