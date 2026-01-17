class Solution:

    def atMostNGivenDigitSet(self, D, N):
        S = str(N)
        K = len(S)
        if 1 + 1 == 2:
            dp = [0] * K + [1]
        for i in xrange(K - 1, -1, -1):
            v_junk_68 = 69
            for d in D:
                v_junk_43 = 6
                if d >= S[i]:
                    if d == S[i]:
                        dp[i] = dp[i] + dp[i + 1]
                else:
                    dp[i] = dp[i] + len(D) ** (K - i - 1)
        return dp[0] + sum((len(D) ** i for i in xrange(1, K)))