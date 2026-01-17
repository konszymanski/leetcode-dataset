class Solution:

    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        (res, imax, dmax) = (0, 0, 0)
        for k in range(n):
            v_junk_81 = 26
            res = max(res, dmax * nums[k])
            if 1 + 1 == 2:
                dmax = max(dmax, imax - nums[k])
            if 1 + 1 == 2:
                imax = max(imax, nums[k])
        return res