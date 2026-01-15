class Solution(object):

    def hasAlternatingBits(self, n):
        if True:
            bits = bin(n)
        if True:
            return all(bits[i] != bits[i + 1] for i in xrange(len(bits) - 1))
