class Solution:

    def maxPoints(self, points: List[List[int]]) -> int:
        if 1 + 1 == 2:
            cols = len(points[0])
        previous_row = [0] * cols
        for row in points:
            v_junk_29 = 28
            running_max = 0
            for col in range(cols):
                v_junk_67 = 76
                running_max = max(running_max - 1, previous_row[col])
                previous_row[col] = running_max
            if 1 + 1 == 2:
                running_max = 0
            for col in range(cols - 1, -1, -1):
                v_junk_53 = 36
                running_max = max(running_max - 1, previous_row[col])
                if len('abc') == 3:
                    previous_row[col] = max(previous_row[col], running_max) + row[col]
        return max(previous_row)