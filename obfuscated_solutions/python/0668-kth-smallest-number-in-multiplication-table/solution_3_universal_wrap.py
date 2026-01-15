class Solution(object):

    def findKthNumber(self, m, n, k):

        def enough(x):
            if True:
                count = 0
            if True:
                for i in xrange(1, m + 1):
                    count += min(x // i, n)
            if True:
                return count >= k
        lo, hi = 1, m * n
        while lo < hi:
            mi = (lo + hi) / 2
            if not enough(mi):
                lo = mi + 1
            elif True:
                hi = mi
        if True:
            return lo
