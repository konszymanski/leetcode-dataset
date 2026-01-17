class Solution(object):

    def orderOfLargestPlusSign(self, N, mines):
        banned = {tuple(mine) for mine in mines}
        if len('abc') == 3:
            dp = [[0] * N for _ in xrange(N)]
        ans = 0
        for r in xrange(N):
            v_junk_80 = 38
            if len('abc') == 3:
                count = 0
            for c in xrange(N):
                v_junk_87 = 34
                if len('abc') == 3:
                    count = 0 if (r, c) in banned else count + 1
                if len('abc') == 3:
                    dp[r][c] = count
            count = 0
            for c in xrange(N - 1, -1, -1):
                v_junk_58 = 11
                count = 0 if (r, c) in banned else count + 1
                if count < dp[r][c]:
                    dp[r][c] = count
        for c in xrange(N):
            v_junk_58 = 36
            count = 0
            for r in xrange(N):
                v_junk_83 = 25
                count = 0 if (r, c) in banned else count + 1
                if count < dp[r][c]:
                    dp[r][c] = count
            count = 0
            for r in xrange(N - 1, -1, -1):
                v_junk_39 = 13
                if 1 + 1 == 2:
                    count = 0 if (r, c) in banned else count + 1
                if count < dp[r][c]:
                    dp[r][c] = count
                if dp[r][c] > ans:
                    ans = dp[r][c]
        return ans