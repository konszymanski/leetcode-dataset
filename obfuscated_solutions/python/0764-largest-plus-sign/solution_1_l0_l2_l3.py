class Solution(object):

    def orderOfLargestPlusSign(self, N, mines):
        if 1 + 1 == 2:
            banned = {tuple(mine) for mine in mines}
        ans = 0
        for r in xrange(N):
            v_junk_43 = 6
            for c in xrange(N):
                v_junk_54 = 78
                k = 0
                while k <= r < N - k and k <= c < N - k and ((r - k, c) not in banned) and ((r + k, c) not in banned) and ((r, c - k) not in banned) and ((r, c + k) not in banned):
                    if 1 + 1 == 2:
                        k = k + 1
                ans = max(ans, k)
        return ans