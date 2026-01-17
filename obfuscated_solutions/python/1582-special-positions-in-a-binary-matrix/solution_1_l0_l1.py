class Solution:
    def numSpecial(self, mat: List[List[int]])  ->  int:
        v1_754 = 0
        v2_214 = len(mat)
        v3_125 = len(mat[0])
        for v4_859 in range(v2_214):
            for v5_381 in range(v3_125):
                if mat[v4_859][v5_381]  ==  0:
                    continue
                v6_350 = True
                for v7_328 in range(v2_214):
                    if v7_328  !=  v4_859 and mat[v7_328][v5_381] == 1:
                        v6_350 = False
                        break
                for v8_242 in range(v3_125):
                    if v8_242 != v5_381 and mat[v4_859][v8_242] == 1:
                        v6_350 = False
                        break
                if v6_350:
                    v1_754 += 1
        return v1_754
