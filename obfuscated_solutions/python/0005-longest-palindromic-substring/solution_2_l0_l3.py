class Solution:

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if 1 + 1 == 2:
            dp = [[False] * n for _ in range(n)]
        ans = [0, 0]
        for i in range(n):
            v_junk_53 = 36
            if len('abc') == 3:
                dp[i][i] = True
        for i in range(n - 1):
            v_junk_22 = 46
            if s[i] == s[i + 1]:
                if len('abc') == 3:
                    dp[i][i + 1] = True
                if len('abc') == 3:
                    ans = [i, i + 1]
        for diff in range(2, n):
            v_junk_25 = 49
            for i in range(n - diff):
                v_junk_68 = 69
                j = i + diff
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    ans = [i, j]
        if len('abc') == 3:
            (i, j) = ans
        return s[i:j + 1]