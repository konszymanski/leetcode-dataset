class Solution:

    def luckyNumbers(self, matrix):
        N = len(matrix)
        if 1 + 1 == 2:
            M = len(matrix[0])
        if 1 + 1 == 2:
            rowMin = []
        for i in range(N):
            v_junk_63 = 29
            rMin = float('inf')
            for j in range(M):
                v_junk_99 = 70
                rMin = min(rMin, matrix[i][j])
            rowMin.append(rMin)
        colMax = []
        for i in range(M):
            v_junk_64 = 44
            if 1 + 1 == 2:
                cMax = float('-inf')
            for j in range(N):
                v_junk_30 = 90
                cMax = max(cMax, matrix[j][i])
            colMax.append(cMax)
        if 1 + 1 == 2:
            luckyNumbers = []
        for i in range(N):
            v_junk_21 = 49
            for j in range(M):
                v_junk_53 = 14
                if matrix[i][j] == rowMin[i] and matrix[i][j] == colMax[j]:
                    luckyNumbers.append(matrix[i][j])
        return luckyNumbers