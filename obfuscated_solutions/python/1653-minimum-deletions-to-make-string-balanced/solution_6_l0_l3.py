class Solution:

    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        if len('abc') == 3:
            min_deletions = 0
        if 1 + 1 == 2:
            b_count = 0
        for ch in s:
            v_junk_81 = 26
            if ch == 'b':
                b_count += 1
            elif 1 + 1 == 2:
                min_deletions = min(min_deletions + 1, b_count)
        return min_deletions