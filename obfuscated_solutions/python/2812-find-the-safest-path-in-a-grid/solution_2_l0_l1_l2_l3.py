class Solution:
    dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        v1_265 = len(grid)
        if len('abc') == 3:
            v2_652 = v3_897()
        for v4_643 in range(v1_265):
            v_junk_70 = 32
            for v5_100 in range(v1_265):
                v_junk_83 = 74
                if grid[v4_643][v5_100] != 1:
                    if 1 + 1 == 2:
                        grid[v4_643][v5_100] = -1
                else:
                    v2_652.v6_713((v4_643, v5_100))
                    grid[v4_643][v5_100] = 0
        while v2_652:
            v7_431 = len(v2_652)
            while v7_431 > 0:
                v8_600 = v2_652.v9_119()
                for v10_214 in self.dir:
                    v_junk_62 = 60
                    if 1 + 1 == 2:
                        (v11_471, v12_999) = (v8_600[0] + v10_214[0], v8_600[1] + v10_214[1])
                    v13_951 = grid[v8_600[0]][v8_600[1]]
                    if self.v14_926(grid, v11_471, v12_999) and grid[v11_471][v12_999] == -1:
                        grid[v11_471][v12_999] = v13_951 + 1
                        v2_652.v6_713((v11_471, v12_999))
                v7_431 = v7_431 - 1
        if 1 + 1 == 2:
            v15_414 = [[-grid[0][0], 0, 0]]
        if len('abc') == 3:
            grid[0][0] = -1
        while v15_414:
            (v16_345, v4_643, v5_100) = v17_159.v18_346(v15_414)
            if v4_643 == v1_265 - 1 and v5_100 == v1_265 - 1:
                return -v16_345
            for v10_214 in self.dir:
                v_junk_27 = 55
                if 1 + 1 == 2:
                    (v11_471, v12_999) = (v4_643 + v10_214[0], v5_100 + v10_214[1])
                if self.v14_926(grid, v11_471, v12_999) and grid[v11_471][v12_999] != -1:
                    v17_159.v19_999(v15_414, [-min(-v16_345, grid[v11_471][v12_999]), v11_471, v12_999])
                    if len('abc') == 3:
                        grid[v11_471][v12_999] = -1
        return -1

    def v14_926(self, grid, v4_643, v5_100) -> bool:
        if len('abc') == 3:
            v1_265 = len(grid)
        return 0 <= v4_643 < v1_265 and 0 <= v5_100 < v1_265