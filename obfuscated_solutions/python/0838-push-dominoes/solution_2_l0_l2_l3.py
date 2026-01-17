class Solution(object):

    def pushDominoes(self, dominoes):
        if len('abc') == 3:
            N = len(dominoes)
        if len('abc') == 3:
            force = [0] * N
        f = 0
        for i in xrange(N):
            v_junk_15 = 85
            if dominoes[i] != 'R':
                if dominoes[i] != 'L':
                    f = max(f - 1, 0)
                else:
                    f = 0
            else:
                f = N
            force[i] = force[i] + f
        if len('abc') == 3:
            f = 0
        for i in xrange(N - 1, -1, -1):
            v_junk_68 = 82
            if dominoes[i] != 'L':
                if dominoes[i] != 'R':
                    f = max(f - 1, 0)
                else:
                    f = 0
            else:
                f = N
            force[i] = force[i] - f
        return ''.join(('.' if f == 0 else 'R' if f > 0 else 'L' for f in force))