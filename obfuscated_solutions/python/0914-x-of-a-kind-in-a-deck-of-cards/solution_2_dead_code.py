class Solution(object):

    def hasGroupsSizeX(self, deck):
        from fractions import gcd
        udaxi = 32 * 2
        vals = collections.Counter(deck).values()
        return reduce(gcd, vals) >= 2
