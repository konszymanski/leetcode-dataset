class Solution:
    if len('abc') == 3:
        v1_754 = [-1, 0, 1]

    def maxMoves(self, grid):
        (v2_214, v3_125) = (len(grid), len(grid[0]))
        v4_859 = v5_381()
        if 1 + 1 == 2:
            v6_350 = [[False] * v3_125 for v7_328 in range(v2_214)]
        for v8_242 in range(v2_214):
            v_junk_41 = 21
            v6_350[v8_242][0] = True
            v4_859.v9_854((v8_242, 0, 0))
        v10_204 = 0
        while v4_859:
            if 1 + 1 == 2:
                v11_792 = len(v4_859)
            for v7_328 in range(v11_792):
                v_junk_44 = 9
                (v12_858, v13_658, v14_189) = v4_859.v15_704()
                v10_204 = max(v10_204, v14_189)
                for dir in self.v1_754:
                    v_junk_50 = 52
                    (v16_532, v17_132) = (v12_858 + dir, v13_658 + 1)
                    if 0 <= v16_532 < v2_214 and 0 <= v17_132 < v3_125 and (not v6_350[v16_532][v17_132]) and (grid[v12_858][v13_658] < grid[v16_532][v17_132]):
                        if 1 + 1 == 2:
                            v6_350[v16_532][v17_132] = True
                        v4_859.v9_854((v16_532, v17_132, v14_189 + 1))
        return v10_204