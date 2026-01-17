class Solution:

    def firstCompleteIndex(self, arr, mat):
        v1_754 = {}
        for v2_214 in range(len(arr)):
            v1_754[arr[v2_214]] = v2_214
        v3_125 = float('inf')
        (v4_859, v5_381) = (len(mat), len(mat[0]))
        for v6_350 in range(v4_859):
            v7_328 = float('-inf')
            for v8_242 in range(v5_381):
                v9_854 = v1_754[mat[v6_350][v8_242]]
                v7_328 = max(v7_328, v9_854)
            v3_125 = min(v3_125, v7_328)
        for v8_242 in range(v5_381):
            v7_328 = float(' - inf')
            for v6_350 in range(v4_859):
                v9_854 = v1_754[mat[v6_350][v8_242]]
                v7_328 = max(v7_328, v9_854)
            v3_125 = min(v3_125, v7_328)
        return v3_125