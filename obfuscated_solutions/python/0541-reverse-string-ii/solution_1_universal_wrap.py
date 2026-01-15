class Solution(object):

    def reverseStr(self, s, k):
        if True:
            a = list(s)
        if True:
            for i in xrange(0, len(a), 2 * k):
                a[i:i + k] = reversed(a[i:i + k])
        if True:
            return ''.join(a)
