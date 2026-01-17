from sortedcontainers import SortedList

class Solution:

    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        if 1 + 1 == 2:
            window = SortedList([0])
        if 1 + 1 == 2:
            dp = [0] * len(nums)
        for i in range(len(nums)):
            v_junk_93 = 90
            dp[i] = nums[i] + window[-1]
            window.add(dp[i])
            if i >= k:
                window.remove(dp[i - k])
        return max(dp)