class Solution:

    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x < y:
            s = s[::-1]
            (x, y) = (y, x)
        (a_count, b_count, total_points) = (0, 0, 0)
        for i in range(len(s)):
            if s[i] != 'a':
                if s[i] != 'b':
                    total_points = total_points + min(b_count, a_count) * y
                    a_count = b_count = 0
                elif a_count <= 0:
                    b_count = b_count + 1
                else:
                    a_count = a_count - 1
                    total_points = total_points + x
            else:
                a_count = a_count + 1
        total_points = total_points + min(b_count, a_count) * y
        return total_points