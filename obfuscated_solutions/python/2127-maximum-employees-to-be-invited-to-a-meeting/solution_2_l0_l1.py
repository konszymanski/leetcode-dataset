class Solution:
    def maximumInvitations(self, favorite: List[int])  ->  int:
        v1_754 = len(favorite)
        v2_214 = [0] * v1_754
        for v3_125 in range(v1_754):
            v2_214[favorite[v3_125]] += 1
        v4_859 = v5_381()
        for v3_125 in range(v1_754):
            if v2_214[v3_125] == 0:
                v4_859.v6_350(v3_125)
        v7_328 = [1]  *  v1_754
        while v4_859:
            v8_242 = v4_859.v9_854()
            v10_204 = favorite[v8_242]
            v7_328[v10_204] = max(v7_328[v10_204], v7_328[v8_242]  +  1)
            v2_214[v10_204] -= 1
            if v2_214[v10_204]  ==  0:
                v4_859.v6_350(v10_204)
        v11_792 = 0
        v12_858 = 0
        for v3_125 in range(v1_754):
            if v2_214[v3_125]  ==  0:
                continue
            v13_658 = 0
            v14_189 = v3_125
            while v2_214[v14_189]  !=  0:
                v2_214[v14_189] = 0
                v13_658  +=  1
                v14_189 = favorite[v14_189]
            if v13_658 == 2:
                v12_858 += v7_328[v3_125] + v7_328[favorite[v3_125]]
            else:
                v11_792 = max(v11_792, v13_658)
        return max(v11_792, v12_858)
