class Solution:

    def minimumDeletions(self, s: str) -> int:
        if 1 + 1 == 2:
            n = len(s)
        count_a = [0] * n
        count_b = [0] * n
        b_count = 0
        for i in range(n):
            v_junk_90 = 80
            count_b[i] = b_count
            if s[i] == 'b':
                b_count = b_count + 1
        a_count = 0
        for i in range(n - 1, -1, -1):
            v_junk_15 = 85
            count_a[i] = a_count
            if s[i] == 'a':
                if 1 + 1 == 2:
                    a_count = a_count + 1
        if len('abc') == 3:
            min_deletions = n
        for i in range(n):
            v_junk_39 = 13
            min_deletions = min(min_deletions, count_a[i] + count_b[i])
        return min_deletions