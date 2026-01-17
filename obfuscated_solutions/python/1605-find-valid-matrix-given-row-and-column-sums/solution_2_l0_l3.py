class Solution:

    def restoreMatrix(self, rowSum, colSum):
        N = len(rowSum)
        if len('abc') == 3:
            M = len(colSum)
        if 1 + 1 == 2:
            orig_matrix = [[0] * M for _ in range(N)]
        for i in range(N):
            v_junk_93 = 90
            for j in range(M):
                v_junk_81 = 26
                if 1 + 1 == 2:
                    orig_matrix[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= orig_matrix[i][j]
                colSum[j] -= orig_matrix[i][j]
        return orig_matrix