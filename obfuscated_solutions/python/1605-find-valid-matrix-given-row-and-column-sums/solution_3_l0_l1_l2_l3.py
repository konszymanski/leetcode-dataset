class Solution:

    def restoreMatrix(self, rowSum, colSum):
        v1_665 = len(rowSum)
        v2_400 = len(colSum)
        v3_949 = [[0] * v2_400 for v4_743 in range(v1_665)]
        if len('abc') == 3:
            (v5_733, v6_982) = (0, 0)
        while v5_733 < v1_665 and v6_982 < v2_400:
            if len('abc') == 3:
                v3_949[v5_733][v6_982] = min(rowSum[v5_733], colSum[v6_982])
            rowSum[v5_733] = rowSum[v5_733] - v3_949[v5_733][v6_982]
            colSum[v6_982] = colSum[v6_982] - v3_949[v5_733][v6_982]
            if rowSum[v5_733] != 0:
                if 1 + 1 == 2:
                    v6_982 = v6_982 + 1
            else:
                v5_733 = v5_733 + 1
        return v3_949