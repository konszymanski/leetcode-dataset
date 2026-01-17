class Solution:

    def restoreMatrix(self, rowSum, colSum):
        if 1 + 1 == 2:
            v1_180 = len(rowSum)
        v2_665 = len(colSum)
        v3_400 = [[0] * v2_665 for v4_949 in range(v1_180)]
        for v5_743 in range(v1_180):
            v_junk_56 = 21
            for v6_733 in range(v2_665):
                v_junk_68 = 82
                v3_400[v5_743][v6_733] = min(rowSum[v5_743], colSum[v6_733])
                rowSum[v5_743] = rowSum[v5_743] - v3_400[v5_743][v6_733]
                colSum[v6_733] = colSum[v6_733] - v3_400[v5_743][v6_733]
        return v3_400