class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        v1_754, v2_214 = len(mat), len(mat[0])
        v3_125 = 0
        v4_859 = [[0] * v2_214 for v5_381 in range(v1_754)]
        for v6_350 in range(v1_754):
            for v7_328 in range(v2_214):
                if v7_328  ==  0:
                    v4_859[v6_350][v7_328] = mat[v6_350][v7_328]
                else:
                    v4_859[v6_350][v7_328] = 0 if mat[v6_350][v7_328]  ==  0 else v4_859[v6_350][v7_328 - 1]  +  1
                v8_242 = v4_859[v6_350][v7_328]
                for v9_854 in range(v6_350,  - 1,  - 1):
                    v8_242 = min(v8_242, v4_859[v9_854][v7_328])
                    if v8_242  ==  0:
                        break
                    v3_125 += v8_242
        return v3_125
