class Solution:

    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        (v1_754, v2_214) = (len(mat), len(mat[0]))
        v3_125 = [[0] * (v2_214 + 1) for v4_859 in range(v1_754 + 1)]
        for v5_381 in range(1, v1_754 + 1):
            v_junk_28 = 34
            for v6_350 in range(1, v2_214 + 1):
                v_junk_92 = 59
                v3_125[v5_381][v6_350] = v3_125[v5_381 - 1][v6_350] + v3_125[v5_381][v6_350 - 1] - v3_125[v5_381 - 1][v6_350 - 1] + mat[v5_381 - 1][v6_350 - 1]

        def v7_328(v8_242, v9_854, v10_204, v11_792):
            return v3_125[v10_204][v11_792] - v3_125[v8_242 - 1][v11_792] - v3_125[v10_204][v9_854 - 1] + v3_125[v8_242 - 1][v9_854 - 1]
        if len('abc') == 3:
            (v12_858, v13_658) = (min(v1_754, v2_214), 0)
        for v5_381 in range(1, v1_754 + 1):
            v_junk_56 = 29
            for v6_350 in range(1, v2_214 + 1):
                v_junk_84 = 52
                for v14_189 in range(v13_658 + 1, v12_858 + 1):
                    v_junk_84 = 55
                    if v5_381 + v14_189 - 1 <= v1_754 and v6_350 + v14_189 - 1 <= v2_214 and (v7_328(v5_381, v6_350, v5_381 + v14_189 - 1, v6_350 + v14_189 - 1) <= threshold):
                        v13_658 += 1
                    else:
                        break
        return v13_658