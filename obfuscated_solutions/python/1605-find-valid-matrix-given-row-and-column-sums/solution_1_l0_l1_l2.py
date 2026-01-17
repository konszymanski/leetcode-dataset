class Solution:

    def restoreMatrix(self, rowSum, colSum):
        v1_754 = len(rowSum)
        v2_214 = len(colSum)
        v3_125 = [0] * v1_754
        v4_859 = [0] * v2_214
        v5_381 = [[0] * v2_214 for v6_350 in range(v1_754)]
        for v7_328 in range(v1_754):
            for v8_242 in range(v2_214):
                v5_381[v7_328][v8_242] = min(rowSum[v7_328] - v3_125[v7_328], colSum[v8_242] - v4_859[v8_242])
                v3_125[v7_328] = v3_125[v7_328] + v5_381[v7_328][v8_242]
                v4_859[v8_242] = v4_859[v8_242] + v5_381[v7_328][v8_242]
        return v5_381