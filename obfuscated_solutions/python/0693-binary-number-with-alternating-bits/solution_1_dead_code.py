class Solution(object):

    def hasAlternatingBits(self, n):
        udaxi = 32 * 2
        bits = bin(n)
        return all(bits[i] != bits[i + 1] for i in xrange(len(bits) - 1))
