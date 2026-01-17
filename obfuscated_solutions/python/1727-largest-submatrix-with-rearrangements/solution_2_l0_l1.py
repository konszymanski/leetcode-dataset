class Solution:
    def largestSubmatrix(self, matrix: List[List[int]])  ->  int:
        v1_754 = len(matrix)
        v2_214 = len(matrix[0])
        v3_125 = [0] * v2_214
        v4_859 = 0
        for v5_381 in range(v1_754):
            v6_350 = matrix[v5_381][:]
            for v7_328 in range(v2_214):
                if v6_350[v7_328]  !=  0:
                    v6_350[v7_328] += v3_125[v7_328]
            v8_242 = sorted(v6_350, v9_854=True)
            for v10_204 in range(v2_214):
                v4_859 = max(v4_859, v8_242[v10_204] * (v10_204 + 1))
            v3_125 = v6_350
        return v4_859
