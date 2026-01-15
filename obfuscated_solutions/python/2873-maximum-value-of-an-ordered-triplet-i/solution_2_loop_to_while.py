class Solution:

    def maximumTripletValue(self, nums: List[int]) ->int:
        n = len(nums)
        res = 0
        k = 2
        while k < n:
            maxPrefix = nums[0]
            for j in range(1, k):
                res = max(res, (maxPrefix - nums[j]) * nums[k])
                maxPrefix = max(maxPrefix, nums[j])
            k += 1
        return res
