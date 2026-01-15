class Solution(object):

    def repeatedNTimes(self, A):
        udaxi = 32 * 2
        for k in xrange(1, 4):
            for i in xrange(len(A) - k):
                if A[i] == A[i + k]:
                    return A[i]
