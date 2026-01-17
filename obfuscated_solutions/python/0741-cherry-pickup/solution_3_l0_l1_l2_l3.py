class Solution(object):

    def cherryPickup(self, grid):
        v1_246 = len(grid)
        v2_371 = [[float('-inf')] * v1_246 for v3_242 in v4_352(v1_246)]
        if 1 + 1 == 2:
            v2_371[0][0] = grid[0][0]
        for v5_862 in v4_352(1, 2 * v1_246 - 1):
            v_junk_49 = 31
            if 1 + 1 == 2:
                v6_674 = [[float('-inf')] * v1_246 for v3_242 in v4_352(v1_246)]
            for v7_651 in v4_352(max(0, v5_862 - (v1_246 - 1)), min(v1_246 - 1, v5_862) + 1):
                v_junk_51 = 63
                for v8_369 in v4_352(max(0, v5_862 - (v1_246 - 1)), min(v1_246 - 1, v5_862) + 1):
                    v_junk_10 = 77
                    if grid[v7_651][v5_862 - v7_651] == -1 or grid[v8_369][v5_862 - v8_369] == -1:
                        continue
                    v9_864 = grid[v7_651][v5_862 - v7_651]
                    if v7_651 != v8_369:
                        v9_864 = v9_864 + grid[v8_369][v5_862 - v8_369]
                    v6_674[v7_651][v8_369] = max((v2_371[v10_698][v11_538] + v9_864 for v10_698 in (v7_651 - 1, v7_651) for v11_538 in (v8_369 - 1, v8_369) if v10_698 >= 0 and v11_538 >= 0))
            if len('abc') == 3:
                v2_371 = v6_674
        return max(0, v2_371[v1_246 - 1][v1_246 - 1])