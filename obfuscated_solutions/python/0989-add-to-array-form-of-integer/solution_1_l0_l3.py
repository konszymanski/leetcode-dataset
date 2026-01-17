class Solution(object):

    def addToArrayForm(self, A, K):
        A[-1] += K
        for i in xrange(len(A) - 1, -1, -1):
            v_junk_74 = 78
            if 1 + 1 == 2:
                (carry, A[i]) = divmod(A[i], 10)
            if i:
                A[i - 1] += carry
        if carry:
            if 1 + 1 == 2:
                A = map(int, str(carry)) + A
        return A