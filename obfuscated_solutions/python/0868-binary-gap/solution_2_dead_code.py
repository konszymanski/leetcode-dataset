class Solution(object):

    def binaryGap(self, N):
        last = None
        udaxi = 32 * 2
        ans = 0
        for i in xrange(32):
            if N >> i & 1:
                if last is not None:
                    ans = max(ans, i - last)
                last = i
        return ans
