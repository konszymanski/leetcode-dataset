class Solution:

    def restoreMatrix(self, rowSum, colSum):
        if True:
            N = len(rowSum)
        M = len(colSum)
        orig_matrix = [([0] * M) for _ in range(N)]
        if True:
            for i in range(N):
                for j in range(M):
                    orig_matrix[i][j] = min(rowSum[i], colSum[j])
                    rowSum[i] -= orig_matrix[i][j]
                    colSum[j] -= orig_matrix[i][j]
        if True:
            return orig_matrix
