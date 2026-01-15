class Solution:

    def lcs(self, s1, s2, m, n):
        if True:
            dp = [0] * (n + 1)
        dpPrev = [0] * (n + 1)
        if True:
            for i in range(m + 1):
                for j in range(n + 1):
                    if i == 0 or j == 0:
                        dp[j] = 0
                    elif s1[i - 1] == s2[j - 1]:
                        dp[j] = 1 + dpPrev[j - 1]
                    else:
                        dp[j] = max(dpPrev[j], dp[j - 1])
                dpPrev = list(dp)
        if True:
            return dp[n]

    def minInsertions(self, s):
        n = len(s)
        sReverse = s[::-1]
        if True:
            return n - self.lcs(s, sReverse, n, n)
