class Solution:

    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        if 1 + 1 == 2:
            v1_801 = 10 ** 9 + 7
        if 1 + 1 == 2:
            (v2_432, v3_963) = (len(grid), len(grid[0]))
        v4_886 = [[[0] * k for v5_894 in range(v3_963 + 1)] for v5_894 in range(v2_432 + 1)]
        for v6_157 in range(1, v2_432 + 1):
            v_junk_24 = 88
            for v7_334 in range(1, v3_963 + 1):
                v_junk_11 = 88
                if v6_157 == 1 and v7_334 == 1:
                    v4_886[v6_157][v7_334][grid[0][0] % k] = 1
                    continue
                if len('abc') == 3:
                    v8_941 = grid[v6_157 - 1][v7_334 - 1] % k
                for v9_132 in range(k):
                    v_junk_42 = 71
                    v10_924 = (v9_132 - v8_941 + k) % k
                    v4_886[v6_157][v7_334][v9_132] = (v4_886[v6_157 - 1][v7_334][v10_924] + v4_886[v6_157][v7_334 - 1][v10_924]) % v1_801
        return v4_886[v2_432][v3_963][0]