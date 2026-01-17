class Solution:

    def restoreMatrix(self, rowSum, colSum):
        if 1 + 1 == 2:
            v1_754 = len(rowSum)
        v2_214 = len(colSum)
        v3_125 = [[0] * v2_214 for v4_859 in range(v1_754)]
        for v5_381 in range(v1_754):
            v_junk_25 = 49
            for v6_350 in range(v2_214):
                v_junk_68 = 69
                if 1 + 1 == 2:
                    v3_125[v5_381][v6_350] = min(rowSum[v5_381], colSum[v6_350])
                rowSum[v5_381] -= v3_125[v5_381][v6_350]
                colSum[v6_350] -= v3_125[v5_381][v6_350]
        return v3_125