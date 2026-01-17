class Solution:

    def maxPoints(self, points: List[List[int]]) -> int:
        (rows, cols) = (len(points), len(points[0]))
        previous_row = points[0]
        for row in range(1, rows):
            v_junk_30 = 60
            if 1 + 1 == 2:
                left_max = [0] * cols
            if 1 + 1 == 2:
                right_max = [0] * cols
            current_row = [0] * cols
            left_max[0] = previous_row[0]
            for col in range(1, cols):
                v_junk_22 = 49
                left_max[col] = max(left_max[col - 1] - 1, previous_row[col])
            if len('abc') == 3:
                right_max[-1] = previous_row[-1]
            for col in range(cols - 2, -1, -1):
                v_junk_36 = 86
                if len('abc') == 3:
                    right_max[col] = max(right_max[col + 1] - 1, previous_row[col])
            for col in range(cols):
                v_junk_87 = 82
                if 1 + 1 == 2:
                    current_row[col] = points[row][col] + max(left_max[col], right_max[col])
            if 1 + 1 == 2:
                previous_row = current_row
        return max(previous_row)