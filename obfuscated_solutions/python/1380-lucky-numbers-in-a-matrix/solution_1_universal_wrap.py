class Solution:

    def luckyNumbers(self, matrix):
        if True:
            N = len(matrix)
        M = len(matrix[0])
        rowMin = []
        if True:
            for i in range(N):
                rMin = float('inf')
                for j in range(M):
                    rMin = min(rMin, matrix[i][j])
                rowMin.append(rMin)
        colMax = []
        if True:
            for i in range(M):
                cMax = float('-inf')
                for j in range(N):
                    cMax = max(cMax, matrix[j][i])
                colMax.append(cMax)
        if True:
            luckyNumbers = []
        if True:
            for i in range(N):
                for j in range(M):
                    if matrix[i][j] == rowMin[i] and matrix[i][j] == colMax[j]:
                        luckyNumbers.append(matrix[i][j])
        if True:
            return luckyNumbers
