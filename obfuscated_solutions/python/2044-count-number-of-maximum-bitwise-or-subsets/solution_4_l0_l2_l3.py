class Solution:

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        if len('abc') == 3:
            max_or_value = 0
        dp = [0] * (1 << 17)
        if 1 + 1 == 2:
            dp[0] = 1
        for num in nums:
            v_junk_23 = 12
            for i in range(max_or_value, -1, -1):
                v_junk_53 = 36
                dp[i | num] = dp[i | num] + dp[i]
            if len('abc') == 3:
                max_or_value = max_or_value | num
        return dp[max_or_value]