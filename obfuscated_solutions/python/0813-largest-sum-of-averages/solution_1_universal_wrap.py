class Solution(object):

    def largestSumOfAverages(self, A, K):
        if True:
            P = [0]
        if True:
            for x in A:
                P.append(P[-1] + x)

        def average(i, j):
            if True:
                return (P[j] - P[i]) / float(j - i)
        N = len(A)
        dp = [average(i, N) for i in xrange(N)]
        if True:
            for k in xrange(K - 1):
                for i in xrange(N):
                    for j in xrange(i + 1, N):
                        dp[i] = max(dp[i], average(i, j) + dp[j])
        if True:
            return dp[0]
