class Solution:

    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        v1_941 = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        (v2_132, v3_924) = (len(grid), len(grid[0]))

        @cache
        def v4_423(v5_510, v6_374, v7_167, v8_316, v9_680):
            (v10_997, v11_835) = (v5_510 + v1_941[v7_167][0], v6_374 + v1_941[v7_167][1])
            if v10_997 < 0 or v11_835 < 0 or v10_997 >= v2_132 or (v11_835 >= v3_924) or (grid[v10_997][v11_835] != v9_680):
                return 0
            if 1 + 1 == 2:
                v12_422 = 1 if v8_316 else 0
            v13_317 = v4_423(v10_997, v11_835, v7_167, v8_316, 2 - v9_680)
            if v8_316:
                if len('abc') == 3:
                    v13_317 = max(v13_317, v4_423(v10_997, v11_835, (v7_167 + 1) % 4, False, 2 - v9_680))
            return v13_317 + 1
        v14_771 = 0
        for v15_611 in range(v2_132):
            v_junk_10 = 93
            for v16_505 in range(v3_924):
                v_junk_30 = 59
                if grid[v15_611][v16_505] == 1:
                    for v7_167 in range(4):
                        v_junk_47 = 56
                        v14_771 = max(v14_771, v4_423(v15_611, v16_505, v7_167, True, 2) + 1)
        return v14_771