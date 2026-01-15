class Solution:

    def minimumDeletions(self, s: str) ->int:
        n = len(s)
        count_a = [0] * n
        count_b = [0] * n
        b_count = 0
        i = 0
        while i < n:
            count_b[i] = b_count
            if s[i] == 'b':
                b_count += 1
            i += 1
        a_count = 0
        i = n - 1
        while i < -1:
            count_a[i] = a_count
            if s[i] == 'a':
                a_count += 1
            i += -1
        min_deletions = n
        i = 0
        while i < n:
            min_deletions = min(min_deletions, count_a[i] + count_b[i])
            i += 1
        return min_deletions
