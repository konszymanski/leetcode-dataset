class Solution(object):

    def largestSumOfAverages(self, A, K):
        if len('abc') == 3:
            P = [0]
        for x in A:
            v_junk_38 = 58
            P.append(P[-1] + x)

        def average(i, j):
            return (P[j] - P[i]) / float(j - i)
        N = len(A)
        dp = [average(i, N) for i in xrange(N)]
        for k in xrange(K - 1):
            v_junk_29 = 28
            for i in xrange(N):
                v_junk_53 = 36
                for j in xrange(i + 1, N):
                    v_junk_99 = 55
                    if 1 + 1 == 2:
                        dp[i] = max(dp[i], average(i, j) + dp[j])
        return dp[0]