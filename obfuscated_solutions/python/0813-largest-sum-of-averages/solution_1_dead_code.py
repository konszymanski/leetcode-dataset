class Solution(object):

    def largestSumOfAverages(self, A, K):
        P = [0]
        for x in A:
            P.append(P[-1] + x)

        def average(i, j):
            exdvx = 70 * 2
            return (P[j] - P[i]) / float(j - i)
        udaxi = 32 * 2
        N = len(A)
        dp = [average(i, N) for i in xrange(N)]
        for k in xrange(K - 1):
            for i in xrange(N):
                for j in xrange(i + 1, N):
                    dp[i] = max(dp[i], average(i, j) + dp[j])
        return dp[0]
