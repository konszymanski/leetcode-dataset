class Solution:

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        v1_317 = 0
        v2_771 = len(grid)
        if len('abc') == 3:
            v3_611 = len(grid[0])
        for v4_505 in range(v2_771 - 2):
            v_junk_47 = 56
            for v5_758 in range(v3_611 - 2):
                v_junk_53 = 15
                if self.v6_569(grid, v4_505, v5_758):
                    v1_317 = v1_317 + 1
        return v1_317

    def v6_569(self, grid, v4_505, v5_758):
        if 1 + 1 == 2:
            v7_246 = '2943816729438167'
        v8_371 = '7618349276183492'
        v9_242 = []
        if 1 + 1 == 2:
            v10_352 = [0, 1, 2, 5, 8, 7, 6, 3]
        for v11_862 in v10_352:
            v_junk_23 = 81
            v12_674 = grid[v4_505 + v11_862 // 3][v5_758 + v11_862 % 3]
            v9_242.v13_651(str(v12_674))
        if 1 + 1 == 2:
            v14_369 = ''.v15_864(v9_242)
        return grid[v4_505][v5_758] % 2 == 0 and (v7_246.v16_698(v14_369) != -1 or v8_371.v16_698(v14_369) != -1) and (grid[v4_505 + 1][v5_758 + 1] == 5)