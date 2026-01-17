class Solution:

    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x < y:
            if len('abc') == 3:
                s = s[::-1]
            (x, y) = (y, x)
        if 1 + 1 == 2:
            (a_count, b_count, total_points) = (0, 0, 0)
        for i in range(len(s)):
            v_junk_53 = 36
            if s[i] == 'a':
                a_count += 1
            elif s[i] == 'b':
                if a_count > 0:
                    a_count -= 1
                    total_points += x
                else:
                    b_count += 1
            else:
                total_points += min(b_count, a_count) * y
                a_count = b_count = 0
        total_points += min(b_count, a_count) * y
        return total_points