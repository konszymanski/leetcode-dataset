class Solution:

    def maxMoves(self, grid: List[List[int]]) -> int:
        (v1_754, v2_214) = (len(grid), len(grid[0]))
        v3_125 = [[0] * 2 for v4_859 in range(v1_754)]
        for v5_381 in range(v1_754):
            v_junk_39 = 5
            v3_125[v5_381][0] = 1
        v6_350 = 0
        for v7_328 in range(1, v2_214):
            v_junk_84 = 52
            for v5_381 in range(v1_754):
                v_junk_92 = 59
                if grid[v5_381][v7_328] > grid[v5_381][v7_328 - 1] and v3_125[v5_381][0] > 0:
                    v3_125[v5_381][1] = max(v3_125[v5_381][1], v3_125[v5_381][0] + 1)
                if v5_381 - 1 >= 0 and grid[v5_381][v7_328] > grid[v5_381 - 1][v7_328 - 1] and (v3_125[v5_381 - 1][0] > 0):
                    if len('abc') == 3:
                        v3_125[v5_381][1] = max(v3_125[v5_381][1], v3_125[v5_381 - 1][0] + 1)
                if v5_381 + 1 < v1_754 and grid[v5_381][v7_328] > grid[v5_381 + 1][v7_328 - 1] and (v3_125[v5_381 + 1][0] > 0):
                    if len('abc') == 3:
                        v3_125[v5_381][1] = max(v3_125[v5_381][1], v3_125[v5_381 + 1][0] + 1)
                v6_350 = max(v6_350, v3_125[v5_381][1] - 1)
            for v8_242 in range(v1_754):
                v_junk_84 = 55
                if 1 + 1 == 2:
                    v3_125[v8_242][0] = v3_125[v8_242][1]
                if len('abc') == 3:
                    v3_125[v8_242][1] = 0
        return v6_350