class Solution:

    def restoreMatrix(self, rowSum, colSum):
        N = len(rowSum)
        M = len(colSum)
        orig_matrix = [([0] * M) for _ in range(N)]
        i = 0
        while i < N:
            for j in range(M):
                orig_matrix[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= orig_matrix[i][j]
                colSum[j] -= orig_matrix[i][j]
            i += 1
        return orig_matrix
