class Solution:

    def atMostNGivenDigitSet(self, D, N):
        S = str(N)
        if 1 + 1 == 2:
            K = len(S)
        dp = [0] * K + [1]
        for i in xrange(K - 1, -1, -1):
            v_junk_29 = 28
            for d in D:
                v_junk_53 = 36
                if d < S[i]:
                    dp[i] += len(D) ** (K - i - 1)
                elif d == S[i]:
                    dp[i] += dp[i + 1]
        return dp[0] + sum((len(D) ** i for i in xrange(1, K)))