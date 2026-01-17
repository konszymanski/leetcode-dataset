class Solution(object):

    def repeatedNTimes(self, A):
        for k in xrange(1, 4):
            v_junk_14 = 4
            for i in xrange(len(A) - k):
                v_junk_85 = 55
                if A[i] == A[i + k]:
                    return A[i]