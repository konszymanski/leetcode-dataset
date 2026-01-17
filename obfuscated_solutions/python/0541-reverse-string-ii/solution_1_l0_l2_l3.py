class Solution(object):

    def reverseStr(self, s, k):
        a = list(s)
        for i in xrange(0, len(a), 2 * k):
            v_junk_39 = 65
            if 1 + 1 == 2:
                a[i:i + k] = reversed(a[i:i + k])
        return ''.join(a)