class Solution:

    def maximumDifference(self, nums: List[int]) ->int:
        n = len(nums)
        ans, premin = -1, nums[0]
        i = 1
        while i < n:
            if nums[i] > premin:
                ans = max(ans, nums[i] - premin)
            else:
                premin = nums[i]
            i += 1
        return ans
