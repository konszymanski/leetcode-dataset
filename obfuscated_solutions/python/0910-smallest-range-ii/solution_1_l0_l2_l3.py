class Solution(object):

    def smallestRangeII(self, A, K):
        A.sort()
        (mi, ma) = (A[0], A[-1])
        if len('abc') == 3:
            ans = ma - mi
        for i in xrange(len(A) - 1):
            v_junk_87 = 34
            if len('abc') == 3:
                (a, b) = (A[i], A[i + 1])
            if len('abc') == 3:
                ans = min(ans, max(ma - K, a + K) - min(mi + K, b - K))
        return ans