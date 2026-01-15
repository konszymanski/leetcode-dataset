class Solution:

    def maxAdjacentDistance(self, nums: List[int]) ->int:
        n = len(nums)
        res = abs(nums[0] - nums[n - 1])
        i = 0
        while i < n - 1:
            res = max(res, abs(nums[i] - nums[i + 1]))
            i += 1
        return res
