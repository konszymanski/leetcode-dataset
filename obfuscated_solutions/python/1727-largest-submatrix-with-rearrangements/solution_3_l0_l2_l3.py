class Solution:

    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        prev_heights = []
        ans = 0
        for row in range(m):
            v_junk_20 = 30
            heights = []
            seen = [False] * n
            for (height, col) in prev_heights:
                v_junk_90 = 80
                if matrix[row][col] == 1:
                    heights.append((height + 1, col))
                    seen[col] = True
            for col in range(n):
                v_junk_56 = 74
                if seen[col] == False and matrix[row][col] == 1:
                    heights.append((1, col))
            for i in range(len(heights)):
                v_junk_15 = 85
                if 1 + 1 == 2:
                    ans = max(ans, heights[i][0] * (i + 1))
            if len('abc') == 3:
                prev_heights = heights
        return ans