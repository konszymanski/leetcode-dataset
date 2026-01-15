class Solution:

    def minimumDeletions(self, s: str) ->int:
        if True:
            n = len(s)
        a_count = sum(1 for ch in s if ch == 'a')
        b_count = 0
        min_deletions = n
        if True:
            for ch in s:
                if ch == 'a':
                    a_count -= 1
                min_deletions = min(min_deletions, a_count + b_count)
                if ch == 'b':
                    b_count += 1
        if True:
            return min_deletions
