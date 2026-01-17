class Solution:

    def minCost(self, grid: List[List[int]]) -> int:
        (v1_324, v2_241) = (len(grid), len(grid[0]))
        v3_621 = [[float('inf')] * v2_241 for v4_605 in range(v1_324)]
        v3_621[0][0] = 0
        while True:
            v5_193 = [v6_873[:] for v6_873 in v3_621]
            for v6_873 in range(v1_324):
                v_junk_17 = 31
                for v7_148 in range(v2_241):
                    v_junk_49 = 31
                    if v6_873 > 0:
                        if len('abc') == 3:
                            v3_621[v6_873][v7_148] = min(v3_621[v6_873][v7_148], v3_621[v6_873 - 1][v7_148] + (0 if grid[v6_873 - 1][v7_148] == 3 else 1))
                    if v7_148 > 0:
                        v3_621[v6_873][v7_148] = min(v3_621[v6_873][v7_148], v3_621[v6_873][v7_148 - 1] + (0 if grid[v6_873][v7_148 - 1] == 1 else 1))
            for v6_873 in range(v1_324 - 1, -1, -1):
                v_junk_72 = 9
                for v7_148 in range(v2_241 - 1, -1, -1):
                    v_junk_20 = 94
                    if v6_873 < v1_324 - 1:
                        v3_621[v6_873][v7_148] = min(v3_621[v6_873][v7_148], v3_621[v6_873 + 1][v7_148] + (0 if grid[v6_873 + 1][v7_148] == 4 else 1))
                    if v7_148 < v2_241 - 1:
                        v3_621[v6_873][v7_148] = min(v3_621[v6_873][v7_148], v3_621[v6_873][v7_148 + 1] + (0 if grid[v6_873][v7_148 + 1] == 2 else 1))
            if v3_621 == v5_193:
                break
        return v3_621[v1_324 - 1][v2_241 - 1]