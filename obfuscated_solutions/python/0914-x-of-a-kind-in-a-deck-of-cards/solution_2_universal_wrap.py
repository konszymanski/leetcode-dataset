class Solution(object):

    def hasGroupsSizeX(self, deck):
        from fractions import gcd
        if True:
            vals = collections.Counter(deck).values()
        if True:
            return reduce(gcd, vals) >= 2
