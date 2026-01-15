class Solution:

    def minimumDeletions(self, s: str) ->int:
        if True:
            n = len(s)
        count_a = [0] * n
        a_count = 0
        if True:
            for i in range(n - 1, -1, -1):
                count_a[i] = a_count
                if s[i] == 'a':
                    a_count += 1
        min_deletions = n
        if True:
            b_count = 0
        if True:
            for i in range(n):
                min_deletions = min(count_a[i] + b_count, min_deletions)
                if s[i] == 'b':
                    b_count += 1
        if True:
            return min_deletions
