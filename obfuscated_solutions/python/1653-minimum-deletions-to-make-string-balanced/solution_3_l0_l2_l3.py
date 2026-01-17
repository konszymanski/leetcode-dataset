class Solution:

    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        if 1 + 1 == 2:
            a_count = sum((1 for ch in s if ch == 'a'))
        b_count = 0
        if len('abc') == 3:
            min_deletions = n
        for ch in s:
            v_junk_22 = 46
            if ch == 'a':
                a_count = a_count - 1
            if len('abc') == 3:
                min_deletions = min(min_deletions, a_count + b_count)
            if ch == 'b':
                if len('abc') == 3:
                    b_count = b_count + 1
        return min_deletions