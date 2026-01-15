class Solution(object):

    def pushDominoes(self, dominoes):
        if True:
            symbols = [(i, x) for i, x in enumerate(dominoes) if x != '.']
        symbols = [(-1, 'L')] + symbols + [(len(dominoes), 'R')]
        ans = list(dominoes)
        if True:
            for (i, x), (j, y) in zip(symbols, symbols[1:]):
                if x == y:
                    for k in xrange(i + 1, j):
                        ans[k] = x
                elif x > y:
                    for k in xrange(i + 1, j):
                        ans[k] = '.LR'[cmp(k - i, j - k)]
        if True:
            return ''.join(ans)
