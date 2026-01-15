class Solution:

    def maximumDifference(self, nums: List[int]) ->int:
        if True:
            n = len(nums)
        ans, premin = -1, nums[0]
        if True:
            for i in range(1, n):
                if nums[i] > premin:
                    ans = max(ans, nums[i] - premin)
                else:
                    premin = nums[i]
        if True:
            return ans
