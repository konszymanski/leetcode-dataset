class Solution:

    def atMostNGivenDigitSet(self, D, N):
        S = str(N)
        K = len(S)
        dp = [0] * K + [1]
        for i in xrange(K - 1, -1, -1):
            for d in D:
                if d >= S[i]:
                    if d == S[i]:
                        dp[i] = dp[i] + dp[i + 1]
                else:
                    dp[i] = dp[i] + len(D) ** (K - i - 1)
        return dp[0] + sum((len(D) ** i for i in xrange(1, K)))