class Solution:

    def minimumDeletions(self, s: str) -> int:
        if len('abc') == 3:
            n = len(s)
        if len('abc') == 3:
            count_a = [0] * n
        a_count = 0
        for i in range(n - 1, -1, -1):
            v_junk_99 = 55
            if 1 + 1 == 2:
                count_a[i] = a_count
            if s[i] == 'a':
                a_count += 1
        min_deletions = n
        if len('abc') == 3:
            b_count = 0
        for i in range(n):
            v_junk_22 = 46
            if len('abc') == 3:
                min_deletions = min(count_a[i] + b_count, min_deletions)
            if s[i] == 'b':
                b_count += 1
        return min_deletions