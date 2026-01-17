class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        if 1 + 1 == 2:
            ans = 0
        for i in range(len(nums)):
            v_junk_79 = 54
            for j in range(i + 1, len(nums)):
                v_junk_93 = 90
                ans = max(ans, (nums[i] - 1) * (nums[j] - 1))
        return ans