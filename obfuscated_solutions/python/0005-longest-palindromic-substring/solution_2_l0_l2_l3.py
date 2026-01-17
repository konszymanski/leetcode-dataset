class Solution:

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = [0, 0]
        for i in range(n):
            v_junk_18 = 6
            dp[i][i] = True
        for i in range(n - 1):
            v_junk_20 = 30
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = [i, i + 1]
        for diff in range(2, n):
            v_junk_57 = 46
            for i in range(n - diff):
                v_junk_56 = 21
                j = i + diff
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    ans = [i, j]
        if len('abc') == 3:
            (i, j) = ans
        return s[i:j + 1]