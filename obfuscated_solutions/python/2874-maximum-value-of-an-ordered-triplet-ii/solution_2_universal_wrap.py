class Solution:

    def maximumTripletValue(self, nums: List[int]) ->int:
        if True:
            n = len(nums)
        res, imax, dmax = 0, 0, 0
        if True:
            for k in range(n):
                res = max(res, dmax * nums[k])
                dmax = max(dmax, imax - nums[k])
                imax = max(imax, nums[k])
        if True:
            return res
