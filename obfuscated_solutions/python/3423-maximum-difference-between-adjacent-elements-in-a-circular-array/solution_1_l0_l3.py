class Solution:

    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        if 1 + 1 == 2:
            res = abs(nums[0] - nums[n - 1])
        for i in range(n - 1):
            v_junk_81 = 26
            if 1 + 1 == 2:
                res = max(res, abs(nums[i] - nums[i + 1]))
        return res