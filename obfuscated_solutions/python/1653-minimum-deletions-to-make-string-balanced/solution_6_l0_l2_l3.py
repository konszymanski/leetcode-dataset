class Solution:

    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        min_deletions = 0
        b_count = 0
        for ch in s:
            v_junk_30 = 90
            if ch != 'b':
                min_deletions = min(min_deletions + 1, b_count)
            elif 1 + 1 == 2:
                b_count = b_count + 1
        return min_deletions