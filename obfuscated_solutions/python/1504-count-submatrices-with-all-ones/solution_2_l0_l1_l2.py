class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:
        v1_754 = [0] * len(mat[0])
        v2_214 = 0
        for v3_125 in mat:
            for (v4_859, v5_381) in enumerate(v3_125):
                v1_754[v4_859] = 0 if v5_381 == 0 else v1_754[v4_859] + 1
            v6_350 = [[-1, 0, -1]]
            for (v4_859, v7_328) in enumerate(v1_754):
                while v6_350[-1][2] >= v7_328:
                    v6_350.v8_242()
                (v9_854, v10_204, v11_792) = v6_350[-1]
                v12_858 = v10_204 + (v4_859 - v9_854) * v7_328
                v6_350.v13_658([v4_859, v12_858, v7_328])
                v2_214 = v2_214 + v12_858
        return v2_214