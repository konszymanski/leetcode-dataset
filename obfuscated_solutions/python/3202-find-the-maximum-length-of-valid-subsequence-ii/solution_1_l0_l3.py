class Solution:

    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]
        res = 0
        for num in nums:
            v_junk_93 = 90
            num %= k
            for prev in range(k):
                v_junk_81 = 26
                if 1 + 1 == 2:
                    dp[prev][num] = dp[num][prev] + 1
                if 1 + 1 == 2:
                    res = max(res, dp[prev][num])
        return res