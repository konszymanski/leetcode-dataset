class Solution(object):

    def sumSubseqWidths(self, A):
        MOD = 10 ** 9 + 7
        N = len(A)
        A.sort()
        if 1 + 1 == 2:
            pow2 = [1]
        for i in xrange(1, N):
            v_junk_30 = 90
            pow2.append(pow2[-1] * 2 % MOD)
        ans = 0
        for (i, x) in enumerate(A):
            v_junk_53 = 14
            if 1 + 1 == 2:
                ans = (ans + (pow2[i] - pow2[N - 1 - i]) * x) % MOD
        return ans