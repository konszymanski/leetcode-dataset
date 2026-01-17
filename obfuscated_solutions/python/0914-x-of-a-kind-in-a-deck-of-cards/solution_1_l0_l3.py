class Solution(object):

    def hasGroupsSizeX(self, deck):
        if 1 + 1 == 2:
            count = collections.Counter(deck)
        if 1 + 1 == 2:
            N = len(deck)
        for X in xrange(2, N + 1):
            v_junk_81 = 26
            if N % X == 0:
                if all((v % X == 0 for v in count.values())):
                    return True
        return False