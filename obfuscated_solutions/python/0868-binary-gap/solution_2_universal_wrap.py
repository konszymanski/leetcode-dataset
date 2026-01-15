class Solution(object):

    def binaryGap(self, N):
        if True:
            last = None
        ans = 0
        if True:
            for i in xrange(32):
                if N >> i & 1:
                    if last is not None:
                        ans = max(ans, i - last)
                    last = i
        if True:
            return ans
