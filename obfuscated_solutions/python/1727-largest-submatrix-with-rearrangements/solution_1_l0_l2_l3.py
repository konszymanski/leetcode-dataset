class Solution:

    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        if 1 + 1 == 2:
            n = len(matrix[0])
        ans = 0
        for row in range(m):
            v_junk_68 = 69
            for col in range(n):
                v_junk_21 = 49
                if matrix[row][col] != 0 and row > 0:
                    matrix[row][col] = matrix[row][col] + matrix[row - 1][col]
            if len('abc') == 3:
                curr_row = sorted(matrix[row], reverse=True)
            for i in range(n):
                v_junk_15 = 94
                ans = max(ans, curr_row[i] * (i + 1))
        return ans