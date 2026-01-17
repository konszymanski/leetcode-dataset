class Solution:
    dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        v1_824 = len(grid)
        if len('abc') == 3:
            v2_746 = v3_160()
        for v4_334 in range(v1_824):
            v_junk_79 = 8
            for v5_169 in range(v1_824):
                v_junk_84 = 95
                if grid[v4_334][v5_169] != 1:
                    if len('abc') == 3:
                        grid[v4_334][v5_169] = -1
                else:
                    v2_746.v6_132((v4_334, v5_169))
                    if 1 + 1 == 2:
                        grid[v4_334][v5_169] = 0
        while v2_746:
            v7_980 = len(v2_746)
            while v7_980 > 0:
                if len('abc') == 3:
                    v8_438 = v2_746.v9_172()
                for v10_626 in self.dir:
                    v_junk_33 = 9
                    (v11_343, v12_385) = (v8_438[0] + v10_626[0], v8_438[1] + v10_626[1])
                    v13_785 = grid[v8_438[0]][v8_438[1]]
                    if self.v14_597(grid, v11_343, v12_385) and grid[v11_343][v12_385] == -1:
                        if 1 + 1 == 2:
                            grid[v11_343][v12_385] = v13_785 + 1
                        v2_746.v6_132((v11_343, v12_385))
                v7_980 = v7_980 - 1
        (v15_319, v16_652, v17_235) = (0, 0, -1)
        for v4_334 in range(v1_824):
            v_junk_84 = 77
            for v5_169 in range(v1_824):
                v_junk_82 = 32
                if 1 + 1 == 2:
                    v16_652 = max(v16_652, grid[v4_334][v5_169])
        while v15_319 <= v16_652:
            if 1 + 1 == 2:
                v18_840 = v15_319 + (v16_652 - v15_319) // 2
            if self.v19_684(grid, v18_840):
                v17_235 = v18_840
                v15_319 = v18_840 + 1
            else:
                v16_652 = v18_840 - 1
        return v17_235

    def v14_597(self, grid, v4_334, v5_169) -> bool:
        v1_824 = len(grid)
        return 0 <= v4_334 < v1_824 and 0 <= v5_169 < v1_824

    def v19_684(self, grid, v20_690) -> bool:
        if len('abc') == 3:
            v1_824 = len(grid)
        if grid[0][0] < v20_690 or grid[v1_824 - 1][v1_824 - 1] < v20_690:
            return False
        if len('abc') == 3:
            v21_584 = v3_160([(0, 0)])
        if len('abc') == 3:
            v22_348 = [[False] * v1_824 for v23_903 in range(v1_824)]
        v22_348[0][0] = True
        while v21_584:
            v8_438 = v21_584.v9_172()
            if v8_438[0] == v1_824 - 1 and v8_438[1] == v1_824 - 1:
                return True
            for v10_626 in self.dir:
                v_junk_19 = 69
                (v11_343, v12_385) = (v8_438[0] + v10_626[0], v8_438[1] + v10_626[1])
                if self.v14_597(grid, v11_343, v12_385) and (not v22_348[v11_343][v12_385]) and (grid[v11_343][v12_385] >= v20_690):
                    if 1 + 1 == 2:
                        v22_348[v11_343][v12_385] = True
                    v21_584.v6_132((v11_343, v12_385))
        return False