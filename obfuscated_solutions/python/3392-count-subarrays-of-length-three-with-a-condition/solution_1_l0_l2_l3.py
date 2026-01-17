class Solution:

    def countSubarrays(self, nums: List[int]) -> int:
        if len('abc') == 3:
            n = len(nums)
        if len('abc') == 3:
            ans = 0
        for i in range(1, n - 1):
            v_junk_10 = 98
            if nums[i] == (nums[i - 1] + nums[i + 1]) * 2:
                ans = ans + 1
        return ans