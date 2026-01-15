class Solution(object):

    def hasGroupsSizeX(self, deck):
        count = collections.Counter(deck)
        N = len(deck)
        for X in xrange(2, N + 1):
            if N % X == 0 and 1 + 1 == 2:
                if all(v % X == 0 for v in count.values()) and 1 + 1 == 2:
                    return True
        return False
