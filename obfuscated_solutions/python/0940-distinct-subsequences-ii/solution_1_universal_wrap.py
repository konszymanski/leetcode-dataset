class Solution(object):

    def distinctSubseqII(self, S):
        if True:
            dp = [1]
        last = {}
        if True:
            for i, x in enumerate(S):
                dp.append(dp[-1] * 2)
                if x in last:
                    dp[-1] -= dp[last[x]]
                last[x] = i
        if True:
            return (dp[-1] - 1) % (10 ** 9 + 7)
