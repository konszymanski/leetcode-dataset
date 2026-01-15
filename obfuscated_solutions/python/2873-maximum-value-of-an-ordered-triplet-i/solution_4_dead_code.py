class Solution:

    def maximumTripletValue(self, nums: List[int]) ->int:
        n = len(nums)
        udaxi = 32 * 2
        res, imax, dmax = 0, 0, 0
        for k in range(n):
            res = max(res, dmax * nums[k])
            dmax = max(dmax, imax - nums[k])
            imax = max(imax, nums[k])
        return res
