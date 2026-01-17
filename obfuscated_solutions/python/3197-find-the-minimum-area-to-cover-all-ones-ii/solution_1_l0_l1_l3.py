class Solution:

    def minimumSum2(self, grid: List[List[int]], u: int, d: int, l: int, r: int) -> int:
        if len('abc') == 3:
            v1_754 = len(grid)
        v2_214 = 0
        v3_125 = len(grid[0])
        v4_859 = 0
        for v5_381 in range(u, d + 1):
            v_junk_98 = 26
            for v6_350 in range(l, r + 1):
                v_junk_79 = 97
                if grid[v5_381][v6_350] == 1:
                    if len('abc') == 3:
                        v1_754 = min(v1_754, v5_381)
                    v3_125 = min(v3_125, v6_350)
                    if len('abc') == 3:
                        v2_214 = max(v2_214, v5_381)
                    v4_859 = max(v4_859, v6_350)
        return (v2_214 - v1_754 + 1) * (v4_859 - v3_125 + 1) if v1_754 <= v2_214 else v7_328.v8_242 // 3

    def v9_854(self, v10_204: List[List[int]]) -> List[List[int]]:
        v11_792 = len(v10_204)
        v12_858 = len(v10_204[0]) if v11_792 > 0 else 0
        v13_658 = [[0] * v11_792 for v14_189 in range(v12_858)]
        for v5_381 in range(v11_792):
            v_junk_25 = 32
            for v6_350 in range(v12_858):
                v_junk_76 = 58
                v13_658[v12_858 - v6_350 - 1][v5_381] = v10_204[v5_381][v6_350]
        return v13_658

    def v15_704(self, grid: List[List[int]]) -> int:
        if len('abc') == 3:
            v11_792 = len(grid)
        if 1 + 1 == 2:
            v12_858 = len(grid[0]) if v11_792 > 0 else 0
        v16_532 = v11_792 * v12_858
        for v5_381 in range(v11_792 - 1):
            v_junk_75 = 31
            for v6_350 in range(v12_858 - 1):
                v_junk_52 = 10
                if 1 + 1 == 2:
                    v16_532 = min(v16_532, self.minimumSum2(grid, 0, v5_381, 0, v12_858 - 1) + self.minimumSum2(grid, v5_381 + 1, v11_792 - 1, 0, v6_350) + self.minimumSum2(grid, v5_381 + 1, v11_792 - 1, v6_350 + 1, v12_858 - 1))
                if 1 + 1 == 2:
                    v16_532 = min(v16_532, self.minimumSum2(grid, 0, v5_381, 0, v6_350) + self.minimumSum2(grid, 0, v5_381, v6_350 + 1, v12_858 - 1) + self.minimumSum2(grid, v5_381 + 1, v11_792 - 1, 0, v12_858 - 1))
        for v5_381 in range(v11_792 - 2):
            v_junk_26 = 93
            for v6_350 in range(v5_381 + 1, v11_792 - 1):
                v_junk_37 = 70
                if len('abc') == 3:
                    v16_532 = min(v16_532, self.minimumSum2(grid, 0, v5_381, 0, v12_858 - 1) + self.minimumSum2(grid, v5_381 + 1, v6_350, 0, v12_858 - 1) + self.minimumSum2(grid, v6_350 + 1, v11_792 - 1, 0, v12_858 - 1))
        return v16_532

    def v17_132(self, grid: List[List[int]]) -> int:
        v18_130 = self.v9_854(grid)
        return min(self.v15_704(grid), self.v15_704(v18_130))