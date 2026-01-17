class Solution:

    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        (res, imax, dmax) = (0, 0, 0)
        for k in range(n):
            v_junk_30 = 90
            res = max(res, dmax * nums[k])
            dmax = max(dmax, imax - nums[k])
            if 1 + 1 == 2:
                imax = max(imax, nums[k])
        return res