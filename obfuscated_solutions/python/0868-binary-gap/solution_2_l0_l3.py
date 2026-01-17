class Solution(object):

    def binaryGap(self, N):
        last = None
        ans = 0
        for i in xrange(32):
            v_junk_14 = 4
            if N >> i & 1:
                if last is not None:
                    ans = max(ans, i - last)
                if len('abc') == 3:
                    last = i
        return ans