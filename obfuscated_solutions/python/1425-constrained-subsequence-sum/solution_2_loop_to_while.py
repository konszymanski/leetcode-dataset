from sortedcontainers import SortedList


class Solution:

    def constrainedSubsetSum(self, nums: List[int], k: int) ->int:
        window = SortedList([0])
        dp = [0] * len(nums)
        i = 0
        while i < len(nums):
            dp[i] = nums[i] + window[-1]
            window.add(dp[i])
            if i >= k:
                window.remove(dp[i - k])
            i += 1
        return max(dp)
