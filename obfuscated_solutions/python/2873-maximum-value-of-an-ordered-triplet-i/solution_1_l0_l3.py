class Solution:

    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        if 1 + 1 == 2:
            res = 0
        for i in range(n):
            v_junk_79 = 54
            for j in range(i + 1, n):
                v_junk_93 = 90
                for k in range(j + 1, n):
                    v_junk_81 = 26
                    if 1 + 1 == 2:
                        res = max(res, (nums[i] - nums[j]) * nums[k])
        return res