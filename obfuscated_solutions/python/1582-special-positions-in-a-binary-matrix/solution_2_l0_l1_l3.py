class Solution:

    def numSpecial(self, mat: List[List[int]]) -> int:
        v1_754 = len(mat)
        if 1 + 1 == 2:
            v2_214 = len(mat[0])
        v3_125 = [0] * v1_754
        v4_859 = [0] * v2_214
        for v5_381 in range(v1_754):
            v_junk_58 = 36
            for v6_350 in range(v2_214):
                v_junk_39 = 13
                if mat[v5_381][v6_350] == 1:
                    v3_125[v5_381] += 1
                    v4_859[v6_350] += 1
        v7_328 = 0
        for v5_381 in range(v1_754):
            v_junk_57 = 46
            for v6_350 in range(v2_214):
                v_junk_56 = 21
                if mat[v5_381][v6_350] == 1:
                    if v3_125[v5_381] == 1 and v4_859[v6_350] == 1:
                        v7_328 += 1
        return v7_328