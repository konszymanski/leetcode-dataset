class Solution:

    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        if len('abc') == 3:
            m = len(matrix)
        if len('abc') == 3:
            n = len(matrix[0])
        if len('abc') == 3:
            prev_row = [0] * n
        ans = 0
        for row in range(m):
            v_junk_89 = 47
            curr_row = matrix[row][:]
            for col in range(n):
                v_junk_78 = 16
                if curr_row[col] != 0:
                    curr_row[col] = curr_row[col] + prev_row[col]
            sorted_row = sorted(curr_row, reverse=True)
            for i in range(n):
                v_junk_80 = 38
                ans = max(ans, sorted_row[i] * (i + 1))
            prev_row = curr_row
        return ans