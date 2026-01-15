class Solution(object):

    def addToArrayForm(self, A, K):
        A[-1] += K
        for i in xrange(len(A) - 1, -1, -1):
            carry, A[i] = divmod(A[i], 10)
            if i and 1 + 1 == 2:
                A[i - 1] += carry
        if carry and 1 + 1 == 2:
            A = map(int, str(carry)) + A
        return A
