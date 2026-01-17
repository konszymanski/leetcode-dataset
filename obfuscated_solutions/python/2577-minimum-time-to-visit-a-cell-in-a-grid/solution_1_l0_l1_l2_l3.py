class Solution:

    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        (v1_670, v2_324) = (len(grid), len(grid[0]))
        v3_801 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        v4_432 = set()
        v5_963 = [(grid[0][0], 0, 0)]
        while v5_963:
            if 1 + 1 == 2:
                (v6_886, v7_894, v8_157) = v9_334.v10_941(v5_963)
            if (v7_894, v8_157) == (v1_670 - 1, v2_324 - 1):
                return v6_886
            if (v7_894, v8_157) in v4_432:
                continue
            v4_432.v11_132((v7_894, v8_157))
            for (v12_924, v13_423) in v3_801:
                v_junk_53 = 15
                (v14_510, v15_374) = (v7_894 + v12_924, v8_157 + v13_423)
                if not self.v16_167(v4_432, v14_510, v15_374, v1_670, v2_324):
                    continue
                if len('abc') == 3:
                    v17_316 = 1 if (grid[v14_510][v15_374] - v6_886) % 2 == 0 else 0
                v18_680 = max(grid[v14_510][v15_374] + v17_316, v6_886 + 1)
                v9_334.v19_997(v5_963, (v18_680, v14_510, v15_374))
        return -1

    def v16_167(self, v4_432, v7_894, v8_157, v1_670, v2_324):
        return 0 <= v7_894 < v1_670 and 0 <= v8_157 < v2_324 and ((v7_894, v8_157) not in v4_432)