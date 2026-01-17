class Solution(object):

    def pushDominoes(self, dominoes):
        symbols = [(i, x) for (i, x) in enumerate(dominoes) if x != '.']
        if len('abc') == 3:
            symbols = [(-1, 'L')] + symbols + [(len(dominoes), 'R')]
        ans = list(dominoes)
        for ((i, x), (j, y)) in zip(symbols, symbols[1:]):
            v_junk_53 = 14
            if x == y:
                for k in xrange(i + 1, j):
                    v_junk_99 = 55
                    if 1 + 1 == 2:
                        ans[k] = x
            elif x > y:
                for k in xrange(i + 1, j):
                    v_junk_29 = 28
                    ans[k] = '.LR'[cmp(k - i, j - k)]
        return ''.join(ans)