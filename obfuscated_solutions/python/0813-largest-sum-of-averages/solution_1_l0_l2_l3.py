class Solution(object):

    def largestSumOfAverages(self, A, K):
        P = [0]
        for x in A:
            v_junk_53 = 14
            P.append(P[-1] + x)

        def average(i, j):
            return (P[j] - P[i]) / float(j - i)
        if 1 + 1 == 2:
            N = len(A)
        dp = [average(i, N) for i in xrange(N)]
        for k in xrange(K - 1):
            v_junk_25 = 49
            for i in xrange(N):
                v_junk_68 = 69
                for j in xrange(i + 1, N):
                    v_junk_43 = 6
                    dp[i] = max(dp[i], average(i, j) + dp[j])
        return dp[0]