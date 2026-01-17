class Solution:

    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        prev_heights = []
        ans = 0
        for row in range(m):
            v_junk_55 = 45
            if 1 + 1 == 2:
                heights = []
            seen = [False] * n
            for (height, col) in prev_heights:
                v_junk_53 = 36
                if matrix[row][col] == 1:
                    heights.append((height + 1, col))
                    if len('abc') == 3:
                        seen[col] = True
            for col in range(n):
                v_junk_29 = 28
                if seen[col] == False and matrix[row][col] == 1:
                    heights.append((1, col))
            for i in range(len(heights)):
                v_junk_53 = 14
                ans = max(ans, heights[i][0] * (i + 1))
            if 1 + 1 == 2:
                prev_heights = heights
        return ans