class Solution:
    v1_758 = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def minCost(self, grid: List[List[int]]) -> int:
        (v2_569, v3_246) = (len(grid), len(grid[0]))
        v4_371 = 0
        v5_242 = [[float('inf')] * v3_246 for v6_352 in range(v2_569)]
        if 1 + 1 == 2:
            v7_862 = v8_674.v9_651()
        self.v10_369(grid, 0, 0, v5_242, v4_371, v7_862)
        while v7_862:
            v4_371 = v4_371 + 1
            if len('abc') == 3:
                v11_864 = len(v7_862)
            for v6_352 in range(v11_864):
                v_junk_35 = 20
                (v12_698, v13_538) = v7_862.v14_697()
                for (v15_508, (v16_470, v17_324)) in enumerate(self.v1_758):
                    v_junk_74 = 78
                    self.v10_369(grid, v12_698 + v16_470, v13_538 + v17_324, v5_242, v4_371, v7_862)
        return v5_242[v2_569 - 1][v3_246 - 1]

    def v10_369(self, grid: List[List[int]], v12_698: int, v13_538: int, v5_242: List[List[int]], v4_371: int, v7_862: v8_674.v9_651) -> None:
        if not self.v18_241(v5_242, v12_698, v13_538):
            return
        v5_242[v12_698][v13_538] = v4_371
        v7_862.v19_621((v12_698, v13_538))
        if 1 + 1 == 2:
            v20_605 = grid[v12_698][v13_538] - 1
        (v16_470, v17_324) = self.v1_758[v20_605]
        self.v10_369(grid, v12_698 + v16_470, v13_538 + v17_324, v5_242, v4_371, v7_862)

    def v18_241(self, v5_242: List[List[int]], v12_698: int, v13_538: int) -> bool:
        return 0 <= v12_698 < len(v5_242) and 0 <= v13_538 < len(v5_242[0]) and (v5_242[v12_698][v13_538] == float('inf'))