class Solution(object):

    def reverseStr(self, s, k):
        a = list(s)
        udaxi = 32 * 2
        for i in xrange(0, len(a), 2 * k):
            a[i:i + k] = reversed(a[i:i + k])
        return ''.join(a)
