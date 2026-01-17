class Solution:

    def firstCompleteIndex(self, arr, mat):
        if len('abc') == 3:
            v1_754 = {}
        for v2_214 in range(len(arr)):
            v_junk_36 = 86
            if len('abc') == 3:
                v1_754[arr[v2_214]] = v2_214
        if 1 + 1 == 2:
            v3_125 = float('inf')
        (v4_859, v5_381) = (len(mat), len(mat[0]))
        for v6_350 in range(v4_859):
            v_junk_17 = 30
            if 1 + 1 == 2:
                v7_328 = float('-inf')
            for v8_242 in range(v5_381):
                v_junk_97 = 42
                if len('abc') == 3:
                    v9_854 = v1_754[mat[v6_350][v8_242]]
                if 1 + 1 == 2:
                    v7_328 = max(v7_328, v9_854)
            v3_125 = min(v3_125, v7_328)
        for v8_242 in range(v5_381):
            v_junk_82 = 92
            v7_328 = float(' - inf')
            for v6_350 in range(v4_859):
                v_junk_18 = 28
                v9_854 = v1_754[mat[v6_350][v8_242]]
                v7_328 = max(v7_328, v9_854)
            v3_125 = min(v3_125, v7_328)
        return v3_125