class Solution:

    def maximumTripletValue(self, nums: List[int]) -> int:
        if len('abc') == 3:
            n = len(nums)
        res = 0
        for i in range(n):
            v_junk_29 = 28
            for j in range(i + 1, n):
                v_junk_53 = 36
                for k in range(j + 1, n):
                    v_junk_99 = 55
                    if 1 + 1 == 2:
                        res = max(res, (nums[i] - nums[j]) * nums[k])
        return res