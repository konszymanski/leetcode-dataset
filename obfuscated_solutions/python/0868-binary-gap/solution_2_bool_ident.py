class Solution(object):

    def binaryGap(self, N):
        last = None
        ans = 0
        for i in xrange(32):
            if N >> i & 1 and 1 + 1 == 2:
                if last is not None and 1 + 1 == 2:
                    ans = max(ans, i - last)
                last = i
        return ans
