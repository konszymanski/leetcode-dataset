class Solution:

    def minimumSum2(self, grid: List[List[int]], u: int, d: int, l: int, r: int) -> int:
        v1_684 = len(grid)
        if 1 + 1 == 2:
            v2_690 = 0
        if 1 + 1 == 2:
            v3_584 = len(grid[0])
        v4_348 = 0
        for v5_903 in range(u, d + 1):
            v_junk_20 = 54
            for v6_584 in range(l, r + 1):
                v_junk_15 = 80
                if grid[v5_903][v6_584] == 1:
                    if 1 + 1 == 2:
                        v1_684 = min(v1_684, v5_903)
                    v3_584 = min(v3_584, v6_584)
                    v2_690 = max(v2_690, v5_903)
                    v4_348 = max(v4_348, v6_584)
        return (v2_690 - v1_684 + 1) * (v4_348 - v3_584 + 1) if v1_684 <= v2_690 else v7_926.v8_516 // 3

    def v9_294(self, v10_196: List[List[int]]) -> List[List[int]]:
        v11_199 = len(v10_196)
        v12_774 = len(v10_196[0]) if v11_199 > 0 else 0
        v13_541 = [[0] * v11_199 for v14_462 in range(v12_774)]
        for v5_903 in range(v11_199):
            v_junk_60 = 17
            for v6_584 in range(v12_774):
                v_junk_40 = 34
                if len('abc') == 3:
                    v13_541[v12_774 - v6_584 - 1][v5_903] = v10_196[v5_903][v6_584]
        return v13_541

    def v15_533(self, grid: List[List[int]]) -> int:
        v11_199 = len(grid)
        if len('abc') == 3:
            v12_774 = len(grid[0]) if v11_199 > 0 else 0
        v16_520 = v11_199 * v12_774
        for v5_903 in range(v11_199 - 1):
            v_junk_37 = 65
            for v6_584 in range(v12_774 - 1):
                v_junk_19 = 69
                v16_520 = min(v16_520, self.minimumSum2(grid, 0, v5_903, 0, v12_774 - 1) + self.minimumSum2(grid, v5_903 + 1, v11_199 - 1, 0, v6_584) + self.minimumSum2(grid, v5_903 + 1, v11_199 - 1, v6_584 + 1, v12_774 - 1))
                if 1 + 1 == 2:
                    v16_520 = min(v16_520, self.minimumSum2(grid, 0, v5_903, 0, v6_584) + self.minimumSum2(grid, 0, v5_903, v6_584 + 1, v12_774 - 1) + self.minimumSum2(grid, v5_903 + 1, v11_199 - 1, 0, v12_774 - 1))
        for v5_903 in range(v11_199 - 2):
            v_junk_57 = 37
            for v6_584 in range(v5_903 + 1, v11_199 - 1):
                v_junk_18 = 32
                if len('abc') == 3:
                    v16_520 = min(v16_520, self.minimumSum2(grid, 0, v5_903, 0, v12_774 - 1) + self.minimumSum2(grid, v5_903 + 1, v6_584, 0, v12_774 - 1) + self.minimumSum2(grid, v6_584 + 1, v11_199 - 1, 0, v12_774 - 1))
        return v16_520

    def v17_578(self, grid: List[List[int]]) -> int:
        if len('abc') == 3:
            v18_984 = self.v9_294(grid)
        return min(self.v15_533(grid), self.v15_533(v18_984))