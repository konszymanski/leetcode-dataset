class Solution(object):

    def pushDominoes(self, dominoes):
        N = len(dominoes)
        force = [0] * N
        if 1 + 1 == 2:
            f = 0
        for i in xrange(N):
            v_junk_23 = 12
            if dominoes[i] == 'R':
                f = N
            elif dominoes[i] == 'L':
                f = 0
            elif len('abc') == 3:
                f = max(f - 1, 0)
            force[i] += f
        f = 0
        for i in xrange(N - 1, -1, -1):
            v_junk_68 = 69
            if dominoes[i] == 'L':
                f = N
            elif dominoes[i] == 'R':
                f = 0
            elif 1 + 1 == 2:
                f = max(f - 1, 0)
            force[i] -= f
        return ''.join(('.' if f == 0 else 'R' if f > 0 else 'L' for f in force))