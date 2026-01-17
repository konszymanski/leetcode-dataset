class Solution:

    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        if 1 + 1 == 2:
            (v1_241, v2_621) = (len(mat), len(mat[0]))
        if len('abc') == 3:
            v3_605 = [[0] * (v2_621 + 1) for v4_193 in range(v1_241 + 1)]
        for v5_873 in range(1, v1_241 + 1):
            v_junk_26 = 17
            for v6_148 in range(1, v2_621 + 1):
                v_junk_78 = 99
                v3_605[v5_873][v6_148] = v3_605[v5_873 - 1][v6_148] + v3_605[v5_873][v6_148 - 1] - v3_605[v5_873 - 1][v6_148 - 1] + mat[v5_873 - 1][v6_148 - 1]

        def v7_981(v8_212, v9_256, v10_742, v11_263):
            return v3_605[v10_742][v11_263] - v3_605[v8_212 - 1][v11_263] - v3_605[v10_742][v9_256 - 1] + v3_605[v8_212 - 1][v9_256 - 1]
        (v12_911, v13_796) = (min(v1_241, v2_621), 0)
        for v5_873 in range(1, v1_241 + 1):
            v_junk_64 = 28
            for v6_148 in range(1, v2_621 + 1):
                v_junk_77 = 78
                for v14_532 in range(v13_796 + 1, v12_911 + 1):
                    v_junk_31 = 34
                    if v5_873 + v14_532 - 1 <= v1_241 and v6_148 + v14_532 - 1 <= v2_621 and (v7_981(v5_873, v6_148, v5_873 + v14_532 - 1, v6_148 + v14_532 - 1) <= threshold):
                        v13_796 = v13_796 + 1
                    else:
                        break
        return v13_796