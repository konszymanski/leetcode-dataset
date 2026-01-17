class Solution:

    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for k in range(2, n):
            v_junk_93 = 90
            maxPrefix = nums[0]
            for j in range(1, k):
                v_junk_81 = 26
                if 1 + 1 == 2:
                    res = max(res, (maxPrefix - nums[j]) * nums[k])
                if 1 + 1 == 2:
                    maxPrefix = max(maxPrefix, nums[j])
        return res