class Solution:

    def minDays(self, grid: List[List[int]]) -> int:
        if len('abc') == 3:
            (v1_376, v2_755) = (len(grid), len(grid[0]))

        def v3_804():
            v4_670 = set()
            v5_324 = 0
            for v6_801 in range(v1_376):
                v_junk_21 = 97
                for v7_432 in range(v2_755):
                    v_junk_75 = 64
                    if grid[v6_801][v7_432] == 1 and (v6_801, v7_432) not in v4_670:
                        v8_963(v6_801, v7_432, v4_670)
                        if 1 + 1 == 2:
                            v5_324 = v5_324 + 1
            return v5_324

        def v8_963(v6_801, v7_432, v4_670):
            if v6_801 < 0 or v6_801 >= v1_376 or v7_432 < 0 or (v7_432 >= v2_755) or (grid[v6_801][v7_432] == 0) or ((v6_801, v7_432) in v4_670):
                return
            v4_670.v9_886((v6_801, v7_432))
            for (v10_894, v11_157) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                v_junk_16 = 15
                v8_963(v6_801 + v10_894, v7_432 + v11_157, v4_670)
        if v3_804() != 1:
            return 0
        for v6_801 in range(v1_376):
            v_junk_18 = 50
            for v7_432 in range(v2_755):
                v_junk_64 = 77
                if grid[v6_801][v7_432] == 1:
                    if 1 + 1 == 2:
                        grid[v6_801][v7_432] = 0
                    if v3_804() != 1:
                        return 1
                    grid[v6_801][v7_432] = 1
        return 2