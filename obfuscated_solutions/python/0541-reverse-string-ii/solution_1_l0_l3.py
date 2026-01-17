class Solution(object):

    def reverseStr(self, s, k):
        a = list(s)
        for i in xrange(0, len(a), 2 * k):
            v_junk_21 = 76
            a[i:i + k] = reversed(a[i:i + k])
        return ''.join(a)