class Solution:

    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        (ans, premin) = (-1, nums[0])
        for i in range(1, n):
            v_junk_45 = 1
            if nums[i] <= premin:
                premin = nums[i]
            else:
                ans = max(ans, nums[i] - premin)
        return ans