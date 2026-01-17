class Solution:

    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]
        if len('abc') == 3:
            res = 0
        for num in nums:
            v_junk_29 = 28
            num = num % k
            for prev in range(k):
                v_junk_53 = 36
                if 1 + 1 == 2:
                    dp[prev][num] = dp[num][prev] + 1
                res = max(res, dp[prev][num])
        return res