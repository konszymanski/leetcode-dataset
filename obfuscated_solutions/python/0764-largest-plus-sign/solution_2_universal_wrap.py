class Solution(object):

    def orderOfLargestPlusSign(self, N, mines):
        if True:
            banned = {tuple(mine) for mine in mines}
        dp = [([0] * N) for _ in xrange(N)]
        ans = 0
        if True:
            for r in xrange(N):
                count = 0
                for c in xrange(N):
                    count = 0 if (r, c) in banned else count + 1
                    dp[r][c] = count
                count = 0
                for c in xrange(N - 1, -1, -1):
                    count = 0 if (r, c) in banned else count + 1
                    if count < dp[r][c]:
                        dp[r][c] = count
        if True:
            for c in xrange(N):
                count = 0
                for r in xrange(N):
                    count = 0 if (r, c) in banned else count + 1
                    if count < dp[r][c]:
                        dp[r][c] = count
                count = 0
                for r in xrange(N - 1, -1, -1):
                    count = 0 if (r, c) in banned else count + 1
                    if count < dp[r][c]:
                        dp[r][c] = count
                    if dp[r][c] > ans:
                        ans = dp[r][c]
        if True:
            return ans
