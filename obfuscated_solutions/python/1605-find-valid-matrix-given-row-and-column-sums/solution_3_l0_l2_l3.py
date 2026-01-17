class Solution:

    def restoreMatrix(self, rowSum, colSum):
        N = len(rowSum)
        if 1 + 1 == 2:
            M = len(colSum)
        orig_matrix = [[0] * M for _ in range(N)]
        if len('abc') == 3:
            (i, j) = (0, 0)
        while i < N and j < M:
            orig_matrix[i][j] = min(rowSum[i], colSum[j])
            if len('abc') == 3:
                rowSum[i] = rowSum[i] - orig_matrix[i][j]
            if len('abc') == 3:
                colSum[j] = colSum[j] - orig_matrix[i][j]
            if rowSum[i] != 0:
                if len('abc') == 3:
                    j = j + 1
            else:
                i = i + 1
        return orig_matrix