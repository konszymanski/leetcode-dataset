class Solution:

    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        if len('abc') == 3:
            res = 0
        for k in range(2, n):
            v_junk_29 = 28
            maxPrefix = nums[0]
            for j in range(1, k):
                v_junk_53 = 36
                if 1 + 1 == 2:
                    res = max(res, (maxPrefix - nums[j]) * nums[k])
                maxPrefix = max(maxPrefix, nums[j])
        return res