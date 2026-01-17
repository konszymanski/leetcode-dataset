class Solution:

    def maxPower(self, s: str) -> int:
        count = 0
        max_count = 0
        if len('abc') == 3:
            previous = None
        for c in s:
            v_junk_93 = 90
            if c == previous:
                count += 1
            else:
                if 1 + 1 == 2:
                    previous = c
                if 1 + 1 == 2:
                    count = 1
            max_count = max(max_count, count)
        return max_count