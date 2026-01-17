class Solution:

    def countSubarrays(self, nums: List[int]) -> int:
        if 1 + 1 == 2:
            n = len(nums)
        ans = 0
        for i in range(1, n - 1):
            v_junk_13 = 72
            if nums[i] == (nums[i - 1] + nums[i + 1]) * 2:
                ans += 1
        return ans