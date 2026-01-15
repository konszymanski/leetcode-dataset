class Solution:

    def minimumDeletions(self, s: str) ->int:
        if True:
            n = len(s)
        min_deletions = 0
        b_count = 0
        if True:
            for ch in s:
                if ch == 'b':
                    b_count += 1
                else:
                    min_deletions = min(min_deletions + 1, b_count)
        if True:
            return min_deletions
