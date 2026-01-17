class Solution:

    def restoreMatrix(self, rowSum, colSum):
        v1_754 = len(rowSum)
        v2_214 = len(colSum)
        v3_125 = [[0] * v2_214 for v4_859 in range(v1_754)]
        (v5_381, v6_350) = (0, 0)
        while v5_381 < v1_754 and v6_350 < v2_214:
            v3_125[v5_381][v6_350] = min(rowSum[v5_381], colSum[v6_350])
            rowSum[v5_381] -= v3_125[v5_381][v6_350]
            colSum[v6_350] -= v3_125[v5_381][v6_350]
            if rowSum[v5_381] == 0:
                v5_381 += 1
            else:
                v6_350 += 1
        return v3_125