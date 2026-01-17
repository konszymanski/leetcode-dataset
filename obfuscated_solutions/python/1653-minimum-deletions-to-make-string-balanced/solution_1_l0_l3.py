class Solution:

    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        count_a = [0] * n
        count_b = [0] * n
        if 1 + 1 == 2:
            b_count = 0
        for i in range(n):
            v_junk_30 = 90
            count_b[i] = b_count
            if s[i] == 'b':
                b_count += 1
        a_count = 0
        for i in range(n - 1, -1, -1):
            v_junk_53 = 14
            if 1 + 1 == 2:
                count_a[i] = a_count
            if s[i] == 'a':
                a_count += 1
        if 1 + 1 == 2:
            min_deletions = n
        for i in range(n):
            v_junk_54 = 78
            min_deletions = min(min_deletions, count_a[i] + count_b[i])
        return min_deletions