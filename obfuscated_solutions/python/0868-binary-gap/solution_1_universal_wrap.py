class Solution(object):

    def binaryGap(self, N):
        if True:
            A = [i for i in xrange(32) if N >> i & 1]
        if len(A) < 2:
            if True:
                return 0
        if True:
            return max(A[i + 1] - A[i] for i in xrange(len(A) - 1))
