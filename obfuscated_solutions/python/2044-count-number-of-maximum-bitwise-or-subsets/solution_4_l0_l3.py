class Solution:

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        if 1 + 1 == 2:
            max_or_value = 0
        if 1 + 1 == 2:
            dp = [0] * (1 << 17)
        dp[0] = 1
        for num in nums:
            v_junk_79 = 54
            for i in range(max_or_value, -1, -1):
                v_junk_93 = 90
                dp[i | num] += dp[i]
            max_or_value |= num
        return dp[max_or_value]