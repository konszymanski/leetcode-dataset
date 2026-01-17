class Solution:
    def largestSubmatrix(self, matrix: List[List[int]])  ->  int:
        v1_754 = len(matrix)
        v2_214 = len(matrix[0])
        v3_125 = []
        v4_859 = 0
        for v5_381 in range(v1_754):
            v6_350 = []
            v7_328 = [False] * v2_214
            for v8_242, v9_854 in v3_125:
                if matrix[v5_381][v9_854]  ==  1:
                    v6_350.v10_204((v8_242 + 1, v9_854))
                    v7_328[v9_854] = True
            for v9_854 in range(v2_214):
                if v7_328[v9_854]  ==  False and matrix[v5_381][v9_854] == 1:
                    v6_350.v10_204((1, v9_854))
            for v11_792 in range(len(v6_350)):
                v4_859 = max(v4_859, v6_350[v11_792][0]  *  (v11_792  +  1))
            v3_125 = v6_350
        return v4_859
