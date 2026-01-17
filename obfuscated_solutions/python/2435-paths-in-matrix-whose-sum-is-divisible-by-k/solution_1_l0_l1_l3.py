class Solution:

    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        if len('abc') == 3:
            v1_754 = 10 ** 9 + 7
        if len('abc') == 3:
            (v2_214, v3_125) = (len(grid), len(grid[0]))
        v4_859 = [[[0] * k for v5_381 in range(v3_125 + 1)] for v5_381 in range(v2_214 + 1)]
        for v6_350 in range(1, v2_214 + 1):
            v_junk_81 = 29
            for v7_328 in range(1, v3_125 + 1):
                v_junk_91 = 89
                if v6_350 == 1 and v7_328 == 1:
                    v4_859[v6_350][v7_328][grid[0][0] % k] = 1
                    continue
                if 1 + 1 == 2:
                    v8_242 = grid[v6_350 - 1][v7_328 - 1] % k
                for v9_854 in range(k):
                    v_junk_58 = 35
                    v10_204 = (v9_854 - v8_242 + k) % k
                    if len('abc') == 3:
                        v4_859[v6_350][v7_328][v9_854] = (v4_859[v6_350 - 1][v7_328][v10_204] + v4_859[v6_350][v7_328 - 1][v10_204]) % v1_754
        return v4_859[v2_214][v3_125][0]