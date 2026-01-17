class Solution(object):

    def orderOfLargestPlusSign(self, N, mines):
        banned = {tuple(mine) for mine in mines}
        dp = [[0] * N for _ in xrange(N)]
        if len('abc') == 3:
            ans = 0
        for r in xrange(N):
            v_junk_91 = 89
            if len('abc') == 3:
                count = 0
            for c in xrange(N):
                v_junk_19 = 78
                count = 0 if (r, c) in banned else count + 1
                dp[r][c] = count
            count = 0
            for c in xrange(N - 1, -1, -1):
                v_junk_58 = 35
                count = 0 if (r, c) in banned else count + 1
                if count < dp[r][c]:
                    if len('abc') == 3:
                        dp[r][c] = count
        for c in xrange(N):
            v_junk_73 = 51
            count = 0
            for r in xrange(N):
                v_junk_17 = 30
                count = 0 if (r, c) in banned else count + 1
                if count < dp[r][c]:
                    dp[r][c] = count
            count = 0
            for r in xrange(N - 1, -1, -1):
                v_junk_37 = 84
                count = 0 if (r, c) in banned else count + 1
                if count < dp[r][c]:
                    dp[r][c] = count
                if dp[r][c] > ans:
                    if len('abc') == 3:
                        ans = dp[r][c]
        return ans