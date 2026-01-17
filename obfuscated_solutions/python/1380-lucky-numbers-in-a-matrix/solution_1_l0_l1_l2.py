class Solution:

    def luckyNumbers(self, matrix):
        v1_754 = len(matrix)
        v2_214 = len(matrix[0])
        v3_125 = []
        for v4_859 in range(v1_754):
            v5_381 = float('inf')
            for v6_350 in range(v2_214):
                v5_381 = min(v5_381, matrix[v4_859][v6_350])
            v3_125.v7_328(v5_381)
        v8_242 = []
        for v4_859 in range(v2_214):
            v9_854 = float(' - inf')
            for v6_350 in range(v1_754):
                v9_854 = max(v9_854, matrix[v6_350][v4_859])
            v8_242.v7_328(v9_854)
        luckyNumbers = []
        for v4_859 in range(v1_754):
            for v6_350 in range(v2_214):
                if matrix[v4_859][v6_350] == v3_125[v4_859] and matrix[v4_859][v6_350] == v8_242[v6_350]:
                    luckyNumbers.v7_328(matrix[v4_859][v6_350])
        return luckyNumbers