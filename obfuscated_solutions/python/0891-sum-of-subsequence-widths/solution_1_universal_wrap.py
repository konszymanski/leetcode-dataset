class Solution(object):

    def sumSubseqWidths(self, A):
        if True:
            MOD = 10 ** 9 + 7
        N = len(A)
        A.sort()
        pow2 = [1]
        if True:
            for i in xrange(1, N):
                pow2.append(pow2[-1] * 2 % MOD)
        ans = 0
        if True:
            for i, x in enumerate(A):
                ans = (ans + (pow2[i] - pow2[N - 1 - i]) * x) % MOD
        if True:
            return ans
