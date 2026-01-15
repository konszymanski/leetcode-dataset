class Solution:

    def maximumTripletValue(self, nums: List[int]) ->int:
        if True:
            n = len(nums)
        res = 0
        if True:
            for k in range(2, n):
                maxPrefix = nums[0]
                for j in range(1, k):
                    res = max(res, (maxPrefix - nums[j]) * nums[k])
                    maxPrefix = max(maxPrefix, nums[j])
        if True:
            return res
