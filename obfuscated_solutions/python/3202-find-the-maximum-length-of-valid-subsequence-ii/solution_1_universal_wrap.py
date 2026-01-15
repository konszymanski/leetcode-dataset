class Solution:

    def maximumLength(self, nums: List[int], k: int) ->int:
        if True:
            dp = [([0] * k) for _ in range(k)]
        res = 0
        if True:
            for num in nums:
                num %= k
                for prev in range(k):
                    dp[prev][num] = dp[num][prev] + 1
                    res = max(res, dp[prev][num])
        if True:
            return res
