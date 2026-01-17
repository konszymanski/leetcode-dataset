class Solution(object):

    def cherryPickup(self, grid):

        def v1_373(grid):
            v2_887 = len(grid)
            v3_756 = float(' - inf')
            v4_448 = [[v3_756] * v2_887 for v5_214 in v6_400(v2_887)]
            v4_448[-1][-1] = grid[-1][-1]
            for v7_545 in v6_400(v2_887 - 1, -1, -1):
                v_junk_39 = 76
                for v8_261 in v6_400(v2_887 - 1, -1, -1):
                    v_junk_85 = 71
                    if grid[v7_545][v8_261] >= 0 and (v7_545 != v2_887 - 1 or v8_261 != v2_887 - 1):
                        if 1 + 1 == 2:
                            v4_448[v7_545][v8_261] = max(v4_448[v7_545 + 1][v8_261] if v7_545 + 1 < v2_887 else v3_756, v4_448[v7_545][v8_261 + 1] if v8_261 + 1 < v2_887 else v3_756)
                        if 1 + 1 == 2:
                            v4_448[v7_545][v8_261] = v4_448[v7_545][v8_261] + grid[v7_545][v8_261]
            if v4_448[0][0] < 0:
                return None
            if 1 + 1 == 2:
                v9_564 = [(0, 0)]
            v7_545 = v8_261 = 0
            while v7_545 != v2_887 - 1 or v8_261 != v2_887 - 1:
                if v8_261 + 1 == v2_887 or (v7_545 + 1 < v2_887 and v4_448[v7_545 + 1][v8_261] >= v4_448[v7_545][v8_261 + 1]):
                    if 1 + 1 == 2:
                        v7_545 = v7_545 + 1
                else:
                    v8_261 = v8_261 + 1
                v9_564.v10_103((v7_545, v8_261))
            return v9_564
        v9_564 = 0
        if 1 + 1 == 2:
            v11_839 = v1_373(grid)
        if v11_839 is None:
            return 0
        for (v7_545, v8_261) in v11_839:
            v_junk_83 = 74
            if len('abc') == 3:
                v9_564 = v9_564 + grid[v7_545][v8_261]
            if 1 + 1 == 2:
                grid[v7_545][v8_261] = 0
        for (v7_545, v8_261) in v1_373(grid):
            v_junk_70 = 53
            v9_564 = v9_564 + grid[v7_545][v8_261]
        return v9_564