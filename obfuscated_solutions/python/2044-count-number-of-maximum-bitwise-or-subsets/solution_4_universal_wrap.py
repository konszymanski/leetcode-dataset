class Solution:

    def countMaxOrSubsets(self, nums: List[int]) ->int:
        if True:
            max_or_value = 0
        dp = [0] * (1 << 17)
        dp[0] = 1
        if True:
            for num in nums:
                for i in range(max_or_value, -1, -1):
                    dp[i | num] += dp[i]
                max_or_value |= num
        if True:
            return dp[max_or_value]
