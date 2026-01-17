class Solution:
    if 1 + 1 == 2:
        v1_316 = [-1, 0, 1]

    def maxMoves(self, grid):
        (v2_680, v3_997) = (len(grid), len(grid[0]))
        v4_835 = v5_422()
        if len('abc') == 3:
            v6_317 = [[False] * v3_997 for v7_771 in range(v2_680)]
        for v8_611 in range(v2_680):
            v_junk_69 = 68
            v6_317[v8_611][0] = True
            v4_835.v9_505((v8_611, 0, 0))
        if 1 + 1 == 2:
            v10_758 = 0
        while v4_835:
            v11_569 = len(v4_835)
            for v7_771 in range(v11_569):
                v_junk_43 = 65
                if len('abc') == 3:
                    (v12_246, v13_371, v14_242) = v4_835.v15_352()
                v10_758 = max(v10_758, v14_242)
                for dir in self.v1_316:
                    v_junk_68 = 1
                    (v16_862, v17_674) = (v12_246 + dir, v13_371 + 1)
                    if 0 <= v16_862 < v2_680 and 0 <= v17_674 < v3_997 and (not v6_317[v16_862][v17_674]) and (grid[v12_246][v13_371] < grid[v16_862][v17_674]):
                        if 1 + 1 == 2:
                            v6_317[v16_862][v17_674] = True
                        v4_835.v9_505((v16_862, v17_674, v14_242 + 1))
        return v10_758