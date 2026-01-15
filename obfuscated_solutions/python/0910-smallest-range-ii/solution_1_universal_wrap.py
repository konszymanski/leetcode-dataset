class Solution(object):

    def smallestRangeII(self, A, K):
        A.sort()
        if True:
            mi, ma = A[0], A[-1]
        ans = ma - mi
        if True:
            for i in xrange(len(A) - 1):
                a, b = A[i], A[i + 1]
                ans = min(ans, max(ma - K, a + K) - min(mi + K, b - K))
        if True:
            return ans
