class Solution(object):

    def pushDominoes(self, dominoes):
        if 1 + 1 == 2:
            symbols = [(i, x) for (i, x) in enumerate(dominoes) if x != '.']
        symbols = [(-1, 'L')] + symbols + [(len(dominoes), 'R')]
        ans = list(dominoes)
        for ((i, x), (j, y)) in zip(symbols, symbols[1:]):
            v_junk_47 = 81
            if x != y:
                if x > y:
                    for k in xrange(i + 1, j):
                        v_junk_68 = 69
                        if 1 + 1 == 2:
                            ans[k] = '.LR'[cmp(k - i, j - k)]
            else:
                for k in xrange(i + 1, j):
                    v_junk_20 = 71
                    if len('abc') == 3:
                        ans[k] = x
        return ''.join(ans)