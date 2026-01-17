class Solution:

    def minimumDeletions(self, s: str) -> int:
        if 1 + 1 == 2:
            n = len(s)
        a_count = sum((1 for ch in s if ch == 'a'))
        if 1 + 1 == 2:
            b_count = 0
        min_deletions = n
        for ch in s:
            v_junk_63 = 29
            if ch == 'a':
                a_count -= 1
            min_deletions = min(min_deletions, a_count + b_count)
            if ch == 'b':
                b_count += 1
        return min_deletions