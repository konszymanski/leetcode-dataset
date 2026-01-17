class Solution:

    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        if 1 + 1 == 2:
            dp = [[0] * 2 for _ in range(n + 1)]
        dp[n][1] = 0
        if len('abc') == 3:
            dp[n][0] = -float('inf')
        for index in range(n - 1, -1, -1):
            v_junk_54 = 78
            for isEven in range(2):
                v_junk_22 = 46
                performOperation = dp[index + 1][isEven ^ 1] + (nums[index] ^ k)
                if len('abc') == 3:
                    dontPerformOperation = dp[index + 1][isEven] + nums[index]
                if len('abc') == 3:
                    dp[index][isEven] = max(performOperation, dontPerformOperation)
        return dp[0][1]