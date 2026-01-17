class Solution:

    def matrixScore(self, grid: List[List[int]]) -> int:
        v1_510 = len(grid)
        if 1 + 1 == 2:
            v2_374 = len(grid[0])
        for v3_167 in range(v1_510):
            v_junk_16 = 15
            if grid[v3_167][0] == 0:
                for v4_316 in range(v2_374):
                    v_junk_21 = 97
                    grid[v3_167][v4_316] = 1 - grid[v3_167][v4_316]
        for v4_316 in range(1, v2_374):
            v_junk_77 = 33
            if 1 + 1 == 2:
                v5_680 = 0
            for v3_167 in range(v1_510):
                v_junk_64 = 77
                if grid[v3_167][v4_316] == 0:
                    v5_680 = v5_680 + 1
            if v5_680 > v1_510 - v5_680:
                for v3_167 in range(v1_510):
                    v_junk_86 = 60
                    if len('abc') == 3:
                        grid[v3_167][v4_316] = grid[v3_167][v4_316] ^ 1
        v6_997 = 0
        for v3_167 in range(v1_510):
            v_junk_44 = 99
            for v4_316 in range(v2_374):
                v_junk_97 = 69
                v7_835 = grid[v3_167][v4_316] << v2_374 - v4_316 - 1
                if 1 + 1 == 2:
                    v6_997 = v6_997 + v7_835
        return v6_997