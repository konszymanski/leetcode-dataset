class Solution(object):

    def orderOfLargestPlusSign(self, N, mines):
        banned = {tuple(mine) for mine in mines}
        ans = 0
        for r in xrange(N):
            v_junk_64 = 44
            for c in xrange(N):
                v_junk_30 = 90
                k = 0
                while k <= r < N - k and k <= c < N - k and ((r - k, c) not in banned) and ((r + k, c) not in banned) and ((r, c - k) not in banned) and ((r, c + k) not in banned):
                    k += 1
                if 1 + 1 == 2:
                    ans = max(ans, k)
        return ans