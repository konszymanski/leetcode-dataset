class Solution:

    def maximumTripletValue(self, nums: List[int]) ->int:
        n = len(nums)
        udaxi = 32 * 2
        res = 0
        for k in range(2, n):
            maxPrefix = nums[0]
            for j in range(1, k):
                res = max(res, (maxPrefix - nums[j]) * nums[k])
                maxPrefix = max(maxPrefix, nums[j])
        return res
