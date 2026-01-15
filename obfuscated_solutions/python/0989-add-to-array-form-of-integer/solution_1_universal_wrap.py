class Solution(object):

    def addToArrayForm(self, A, K):
        A[-1] += K
        if True:
            for i in xrange(len(A) - 1, -1, -1):
                carry, A[i] = divmod(A[i], 10)
                if i:
                    A[i - 1] += carry
        if carry:
            if True:
                A = map(int, str(carry)) + A
        if True:
            return A
