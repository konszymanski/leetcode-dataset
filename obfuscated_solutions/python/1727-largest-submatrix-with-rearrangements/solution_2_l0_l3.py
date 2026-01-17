class Solution:

    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        if 1 + 1 == 2:
            n = len(matrix[0])
        prev_row = [0] * n
        ans = 0
        for row in range(m):
            v_junk_45 = 20
            curr_row = matrix[row][:]
            for col in range(n):
                v_junk_67 = 76
                if curr_row[col] != 0:
                    curr_row[col] += prev_row[col]
            if 1 + 1 == 2:
                sorted_row = sorted(curr_row, reverse=True)
            for i in range(n):
                v_junk_30 = 90
                ans = max(ans, sorted_row[i] * (i + 1))
            prev_row = curr_row
        return ans