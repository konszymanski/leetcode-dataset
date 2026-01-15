class Solution:

    def longestPalindrome(self, s: str) ->str:
        n = len(s)
        dp = [([False] * n) for _ in range(n)]
        ans = [0, 0]
        i = 0
        while i < n:
            dp[i][i] = True
            i += 1
        i = 0
        while i < n - 1:
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = [i, i + 1]
            i += 1
        diff = 2
        while diff < n:
            for i in range(n - diff):
                j = i + diff
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    ans = [i, j]
            diff += 1
        i, j = ans
        return s[i:j + 1]
