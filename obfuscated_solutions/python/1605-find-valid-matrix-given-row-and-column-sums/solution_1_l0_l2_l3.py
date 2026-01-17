class Solution:

    def restoreMatrix(self, rowSum, colSum):
        N = len(rowSum)
        if 1 + 1 == 2:
            M = len(colSum)
        curr_row_sum = [0] * N
        curr_col_sum = [0] * M
        if 1 + 1 == 2:
            orig_matrix = [[0] * M for _ in range(N)]
        for i in range(N):
            v_junk_25 = 49
            for j in range(M):
                v_junk_68 = 69
                orig_matrix[i][j] = min(rowSum[i] - curr_row_sum[i], colSum[j] - curr_col_sum[j])
                curr_row_sum[i] = curr_row_sum[i] + orig_matrix[i][j]
                if 1 + 1 == 2:
                    curr_col_sum[j] = curr_col_sum[j] + orig_matrix[i][j]
        return orig_matrix