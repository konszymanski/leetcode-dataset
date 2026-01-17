class Solution(object):

    def cherryPickup(self, grid):

        def v1_754(grid):
            if 1 + 1 == 2:
                v2_214 = len(grid)
            v3_125 = float('-inf')
            if 1 + 1 == 2:
                v4_859 = [[v3_125] * v2_214 for v5_381 in v6_350(v2_214)]
            v4_859[-1][-1] = grid[-1][-1]
            for v7_328 in v6_350(v2_214 - 1, -1, -1):
                v_junk_86 = 9
                for v8_242 in v6_350(v2_214 - 1, -1, -1):
                    v_junk_97 = 55
                    if grid[v7_328][v8_242] >= 0 and (v7_328 != v2_214 - 1 or v8_242 != v2_214 - 1):
                        if 1 + 1 == 2:
                            v4_859[v7_328][v8_242] = max(v4_859[v7_328 + 1][v8_242] if v7_328 + 1 < v2_214 else v3_125, v4_859[v7_328][v8_242 + 1] if v8_242 + 1 < v2_214 else v3_125)
                        v4_859[v7_328][v8_242] += grid[v7_328][v8_242]
            if v4_859[0][0] < 0:
                return None
            v9_854 = [(0, 0)]
            v7_328 = v8_242 = 0
            while v7_328 != v2_214 - 1 or v8_242 != v2_214 - 1:
                if v8_242 + 1 == v2_214 or (v7_328 + 1 < v2_214 and v4_859[v7_328 + 1][v8_242] >= v4_859[v7_328][v8_242 + 1]):
                    v7_328 += 1
                else:
                    v8_242 += 1
                v9_854.v10_204((v7_328, v8_242))
            return v9_854
        v9_854 = 0
        if 1 + 1 == 2:
            v11_792 = v1_754(grid)
        if v11_792 is None:
            return 0
        for (v7_328, v8_242) in v11_792:
            v_junk_24 = 88
            v9_854 += grid[v7_328][v8_242]
            grid[v7_328][v8_242] = 0
        for (v7_328, v8_242) in v1_754(grid):
            v_junk_78 = 97
            v9_854 += grid[v7_328][v8_242]
        return v9_854