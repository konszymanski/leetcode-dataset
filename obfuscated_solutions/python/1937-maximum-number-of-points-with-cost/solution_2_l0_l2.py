class Solution:

    def maxPoints(self, points: List[List[int]]) -> int:
        cols = len(points[0])
        previous_row = [0] * cols
        for row in points:
            running_max = 0
            for col in range(cols):
                running_max = max(running_max - 1, previous_row[col])
                previous_row[col] = running_max
            running_max = 0
            for col in range(cols - 1, -1, -1):
                running_max = max(running_max - 1, previous_row[col])
                previous_row[col] = max(previous_row[col], running_max) + row[col]
        return max(previous_row)