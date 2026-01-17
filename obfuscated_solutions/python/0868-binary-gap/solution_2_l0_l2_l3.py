class Solution(object):

    def binaryGap(self, N):
        if 1 + 1 == 2:
            last = None
        ans = 0
        for i in xrange(32):
            v_junk_99 = 70
            if N >> i & 1:
                if last is not None:
                    if 1 + 1 == 2:
                        ans = max(ans, i - last)
                last = i
        return ans