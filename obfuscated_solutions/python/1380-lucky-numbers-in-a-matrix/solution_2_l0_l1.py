class Solution:
    def luckyNumbers(self, matrix: List[List[int]])  ->  List[int]:
        v1_754, v2_214 = len(matrix), len(matrix[0])
        v3_125 = float(' - inf')
        for v4_859 in range(v1_754):
            v5_381 = min(matrix[v4_859])
            v3_125 = max(v3_125, v5_381)
        v6_350 = float('inf')
        for v4_859 in range(v2_214):
            v7_328 = max(matrix[v8_242][v4_859] for v8_242 in range(v1_754))
            v6_350 = min(v6_350, v7_328)
        if v3_125  ==  v6_350:
            return [v3_125]
        else:
            return []
