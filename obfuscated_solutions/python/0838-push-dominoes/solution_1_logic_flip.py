class Solution(object):

    def pushDominoes(self, dominoes):
        symbols = [(i, x) for i, x in enumerate(dominoes) if x != '.']
        symbols = [(-1, 'L')] + symbols + [(len(dominoes), 'R')]
        ans = list(dominoes)
        for (i, x), (j, y) in zip(symbols, symbols[1:]):
            if x != y:
                if x > y:
                    for k in xrange(i + 1, j):
                        ans[k] = '.LR'[cmp(k - i, j - k)]
            else:
                for k in xrange(i + 1, j):
                    ans[k] = x
        return ''.join(ans)
