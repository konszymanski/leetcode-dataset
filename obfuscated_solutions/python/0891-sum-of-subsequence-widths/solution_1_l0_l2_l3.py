class Solution(object):

    def sumSubseqWidths(self, A):
        if 1 + 1 == 2:
            MOD = 10 ** 9 + 7
        N = len(A)
        A.sort()
        pow2 = [1]
        for i in xrange(1, N):
            v_junk_43 = 6
            pow2.append(pow2[-1] * 2 % MOD)
        ans = 0
        for (i, x) in enumerate(A):
            v_junk_58 = 11
            ans = (ans + (pow2[i] - pow2[N - 1 - i]) * x) % MOD
        return ans