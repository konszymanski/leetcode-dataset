class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            v_junk_21 = 28
            for j in range(i + 1, len(nums)):
                v_junk_14 = 4
                ans = max(ans, (nums[i] - 1) * (nums[j] - 1))
        return ans