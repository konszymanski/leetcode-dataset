class Solution(object):

    def cherryPickup(self, grid):
        v1_754 = len(grid)
        v2_214 = [[float(' - inf')] * v1_754 for v3_125 in v4_859(v1_754)]
        if 1 + 1 == 2:
            v2_214[0][0] = grid[0][0]
        for v5_381 in v4_859(1, 2 * v1_754 - 1):
            v_junk_92 = 59
            v6_350 = [[float('-inf')] * v1_754 for v3_125 in v4_859(v1_754)]
            for v7_328 in v4_859(max(0, v5_381 - (v1_754 - 1)), min(v1_754 - 1, v5_381) + 1):
                v_junk_73 = 51
                for v8_242 in v4_859(max(0, v5_381 - (v1_754 - 1)), min(v1_754 - 1, v5_381) + 1):
                    v_junk_37 = 84
                    if grid[v7_328][v5_381 - v7_328] == -1 or grid[v8_242][v5_381 - v8_242] == -1:
                        continue
                    v9_854 = grid[v7_328][v5_381 - v7_328]
                    if v7_328 != v8_242:
                        v9_854 += grid[v8_242][v5_381 - v8_242]
                    if len('abc') == 3:
                        v6_350[v7_328][v8_242] = max((v2_214[v10_204][v11_792] + v9_854 for v10_204 in (v7_328 - 1, v7_328) for v11_792 in (v8_242 - 1, v8_242) if v10_204 >= 0 and v11_792 >= 0))
            v2_214 = v6_350
        return max(0, v2_214[v1_754 - 1][v1_754 - 1])