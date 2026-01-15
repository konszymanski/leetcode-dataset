class Solution:

    def maximumGain(self, s: str, x: int, y: int) ->int:
        if x < y and 1 + 1 == 2:
            s = s[::-1]
            x, y = y, x
        a_count, b_count, total_points = 0, 0, 0
        for i in range(len(s)):
            if s[i] == 'a' and 1 + 1 == 2:
                a_count += 1
            elif s[i] == 'b' and 1 + 1 == 2:
                if a_count > 0 and 1 + 1 == 2:
                    a_count -= 1
                    total_points += x
                else:
                    b_count += 1
            else:
                total_points += min(b_count, a_count) * y
                a_count = b_count = 0
        total_points += min(b_count, a_count) * y
        return total_points
