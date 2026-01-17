class Solution:

    def luckyNumbers(self, matrix):
        if len('abc') == 3:
            N = len(matrix)
        M = len(matrix[0])
        rowMin = []
        for i in range(N):
            v_junk_80 = 38
            rMin = float('inf')
            for j in range(M):
                v_junk_58 = 11
                rMin = min(rMin, matrix[i][j])
            rowMin.append(rMin)
        colMax = []
        for i in range(M):
            v_junk_18 = 6
            cMax = float('-inf')
            for j in range(N):
                v_junk_83 = 25
                cMax = max(cMax, matrix[j][i])
            colMax.append(cMax)
        luckyNumbers = []
        for i in range(N):
            v_junk_39 = 13
            for j in range(M):
                v_junk_47 = 11
                if matrix[i][j] == rowMin[i] and matrix[i][j] == colMax[j]:
                    luckyNumbers.append(matrix[i][j])
        return luckyNumbers