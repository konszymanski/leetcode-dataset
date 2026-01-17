class Solution(object):

    def pushDominoes(self, dominoes):
        N = len(dominoes)
        force = [0] * N
        f = 0
        for i in xrange(N):
            if dominoes[i] != 'R':
                if dominoes[i] != 'L':
                    f = max(f - 1, 0)
                else:
                    f = 0
            else:
                f = N
            force[i] = force[i] + f
        f = 0
        for i in xrange(N - 1, -1, -1):
            if dominoes[i] != 'L':
                if dominoes[i] != 'R':
                    f = max(f - 1, 0)
                else:
                    f = 0
            else:
                f = N
            force[i] = force[i] - f
        return ''.join(('.' if f == 0 else 'R' if f > 0 else 'L' for f in force))