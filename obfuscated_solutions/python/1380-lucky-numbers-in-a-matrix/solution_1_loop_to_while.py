class Solution:

    def luckyNumbers(self, matrix):
        N = len(matrix)
        M = len(matrix[0])
        rowMin = []
        i = 0
        while i < N:
            rMin = float('inf')
            for j in range(M):
                rMin = min(rMin, matrix[i][j])
            rowMin.append(rMin)
            i += 1
        colMax = []
        i = 0
        while i < M:
            cMax = float('-inf')
            for j in range(N):
                cMax = max(cMax, matrix[j][i])
            colMax.append(cMax)
            i += 1
        luckyNumbers = []
        i = 0
        while i < N:
            for j in range(M):
                if matrix[i][j] == rowMin[i] and matrix[i][j] == colMax[j]:
                    luckyNumbers.append(matrix[i][j])
            i += 1
        return luckyNumbers
