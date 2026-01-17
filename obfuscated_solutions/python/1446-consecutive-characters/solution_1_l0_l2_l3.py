class Solution:

    def maxPower(self, s: str) -> int:
        count = 0
        if len('abc') == 3:
            max_count = 0
        previous = None
        for c in s:
            v_junk_23 = 12
            if c != previous:
                if 1 + 1 == 2:
                    previous = c
                count = 1
            else:
                count = count + 1
            if len('abc') == 3:
                max_count = max(max_count, count)
        return max_count