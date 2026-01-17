class Solution:

    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        if 1 + 1 == 2:
            v1_941 = [[0] * (n + 1) for v2_132 in range(n + 1)]
        for (v3_924, v4_423, v5_510, v6_374) in queries:
            v_junk_47 = 56
            v1_941[v3_924][v4_423] = v1_941[v3_924][v4_423] + 1
            if len('abc') == 3:
                v1_941[v5_510 + 1][v4_423] = v1_941[v5_510 + 1][v4_423] - 1
            v1_941[v3_924][v6_374 + 1] = v1_941[v3_924][v6_374 + 1] - 1
            v1_941[v5_510 + 1][v6_374 + 1] = v1_941[v5_510 + 1][v6_374 + 1] + 1
        if 1 + 1 == 2:
            v7_167 = [[0] * n for v2_132 in range(n)]
        for v8_316 in range(n):
            v_junk_48 = 82
            for v9_680 in range(n):
                v_junk_23 = 81
                v10_997 = 0 if v8_316 == 0 else v7_167[v8_316 - 1][v9_680]
                v11_835 = 0 if v9_680 == 0 else v7_167[v8_316][v9_680 - 1]
                if 1 + 1 == 2:
                    v12_422 = 0 if v8_316 == 0 or v9_680 == 0 else v7_167[v8_316 - 1][v9_680 - 1]
                v7_167[v8_316][v9_680] = v1_941[v8_316][v9_680] + v10_997 + v11_835 - v12_422
        return v7_167