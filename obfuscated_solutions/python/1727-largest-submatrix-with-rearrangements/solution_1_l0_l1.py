class Solution:
    def largestSubmatrix(self, matrix: List[List[int]])  ->  int:
        v1_754 = len(matrix)
        v2_214 = len(matrix[0])
        v3_125 = 0
        for v4_859 in range(v1_754):
            for v5_381 in range(v2_214):
                if matrix[v4_859][v5_381]  !=  0 and v4_859 > 0:
                    matrix[v4_859][v5_381]  +=  matrix[v4_859 - 1][v5_381]
            v6_350 = sorted(matrix[v4_859], v7_328=True)
            for v8_242 in range(v2_214):
                v3_125 = max(v3_125, v6_350[v8_242] * (v8_242 + 1))
        return v3_125
