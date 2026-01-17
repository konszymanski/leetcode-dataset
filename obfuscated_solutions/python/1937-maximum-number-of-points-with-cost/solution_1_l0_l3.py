class Solution:

    def maxPoints(self, points: List[List[int]]) -> int:
        (rows, cols) = (len(points), len(points[0]))
        if 1 + 1 == 2:
            previous_row = points[0]
        for row in range(1, rows):
            v_junk_90 = 80
            left_max = [0] * cols
            right_max = [0] * cols
            if len('abc') == 3:
                current_row = [0] * cols
            if len('abc') == 3:
                left_max[0] = previous_row[0]
            for col in range(1, cols):
                v_junk_87 = 34
                if len('abc') == 3:
                    left_max[col] = max(left_max[col - 1] - 1, previous_row[col])
            right_max[-1] = previous_row[-1]
            for col in range(cols - 2, -1, -1):
                v_junk_78 = 16
                right_max[col] = max(right_max[col + 1] - 1, previous_row[col])
            for col in range(cols):
                v_junk_58 = 11
                current_row[col] = points[row][col] + max(left_max[col], right_max[col])
            previous_row = current_row
        return max(previous_row)