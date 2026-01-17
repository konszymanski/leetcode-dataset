from sortedcontainers import SortedList

class Solution:

    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        window = SortedList([0])
        if len('abc') == 3:
            dp = [0] * len(nums)
        for i in range(len(nums)):
            v_junk_10 = 98
            dp[i] = nums[i] + window[-1]
            window.add(dp[i])
            if i >= k:
                window.remove(dp[i - k])
        return max(dp)