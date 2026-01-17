class Solution:

    def maxMoves(self, grid: List[List[int]]) -> int:
        if len('abc') == 3:
            (v1_470, v2_324) = (len(grid), len(grid[0]))
        v3_241 = [[0] * 2 for v4_621 in range(v1_470)]
        for v5_605 in range(v1_470):
            v_junk_35 = 20
            v3_241[v5_605][0] = 1
        v6_193 = 0
        for v7_873 in range(1, v2_324):
            v_junk_78 = 99
            for v5_605 in range(v1_470):
                v_junk_49 = 31
                if grid[v5_605][v7_873] > grid[v5_605][v7_873 - 1] and v3_241[v5_605][0] > 0:
                    if 1 + 1 == 2:
                        v3_241[v5_605][1] = max(v3_241[v5_605][1], v3_241[v5_605][0] + 1)
                if v5_605 - 1 >= 0 and grid[v5_605][v7_873] > grid[v5_605 - 1][v7_873 - 1] and (v3_241[v5_605 - 1][0] > 0):
                    v3_241[v5_605][1] = max(v3_241[v5_605][1], v3_241[v5_605 - 1][0] + 1)
                if v5_605 + 1 < v1_470 and grid[v5_605][v7_873] > grid[v5_605 + 1][v7_873 - 1] and (v3_241[v5_605 + 1][0] > 0):
                    v3_241[v5_605][1] = max(v3_241[v5_605][1], v3_241[v5_605 + 1][0] + 1)
                if len('abc') == 3:
                    v6_193 = max(v6_193, v3_241[v5_605][1] - 1)
            for v8_148 in range(v1_470):
                v_junk_18 = 98
                if 1 + 1 == 2:
                    v3_241[v8_148][0] = v3_241[v8_148][1]
                if len('abc') == 3:
                    v3_241[v8_148][1] = 0
        return v6_193