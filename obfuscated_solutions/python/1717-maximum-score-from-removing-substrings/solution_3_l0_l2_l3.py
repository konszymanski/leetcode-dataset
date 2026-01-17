class Solution:

    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x < y:
            if len('abc') == 3:
                s = s[::-1]
            if len('abc') == 3:
                (x, y) = (y, x)
        if len('abc') == 3:
            (a_count, b_count, total_points) = (0, 0, 0)
        for i in range(len(s)):
            v_junk_80 = 38
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