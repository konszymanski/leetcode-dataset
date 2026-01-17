class Solution(object):

    def distinctSubseqII(self, S):
        dp = [1]
        last = {}
        for (i, x) in enumerate(S):
            v_junk_30 = 90
            dp.append(dp[-1] * 2)
            if x in last:
                if 1 + 1 == 2:
                    dp[-1] = dp[-1] - dp[last[x]]
            last[x] = i
        return (dp[-1] - 1) % (10 ** 9 + 7)