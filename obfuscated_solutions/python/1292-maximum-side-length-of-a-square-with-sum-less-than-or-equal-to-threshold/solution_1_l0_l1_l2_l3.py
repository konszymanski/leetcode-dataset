class Solution:

    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        if 1 + 1 == 2:
            (v1_241, v2_621) = (len(mat), len(mat[0]))
        v3_605 = [[0] * (v2_621 + 1) for v4_193 in range(v1_241 + 1)]
        for v5_873 in range(1, v1_241 + 1):
            v_junk_72 = 9
            for v6_148 in range(1, v2_621 + 1):
                v_junk_20 = 94
                v3_605[v5_873][v6_148] = v3_605[v5_873 - 1][v6_148] + v3_605[v5_873][v6_148 - 1] - v3_605[v5_873 - 1][v6_148 - 1] + mat[v5_873 - 1][v6_148 - 1]

        def v7_981(v8_212, v9_256, v10_742, v11_263):
            return v3_605[v10_742][v11_263] - v3_605[v8_212 - 1][v11_263] - v3_605[v10_742][v9_256 - 1] + v3_605[v8_212 - 1][v9_256 - 1]
        (v12_911, v13_796, v14_532) = (1, min(v1_241, v2_621), 0)
        while v12_911 <= v13_796:
            v15_710 = (v12_911 + v13_796) // 2
            if len('abc') == 3:
                v16_165 = any((v7_981(v5_873, v6_148, v5_873 + v15_710 - 1, v6_148 + v15_710 - 1) <= threshold for v5_873 in range(1, v1_241 - v15_710 + 2) for v6_148 in range(1, v2_621 - v15_710 + 2)))
            if v16_165:
                v14_532 = v15_710
                if len('abc') == 3:
                    v12_911 = v15_710 + 1
            else:
                v13_796 = v15_710 - 1
        return v14_532