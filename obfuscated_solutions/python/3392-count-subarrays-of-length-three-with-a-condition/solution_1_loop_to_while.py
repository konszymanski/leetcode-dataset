class Solution:

    def countSubarrays(self, nums: List[int]) ->int:
        n = len(nums)
        ans = 0
        i = 1
        while i < n - 1:
            if nums[i] == (nums[i - 1] + nums[i + 1]) * 2:
                ans += 1
            i += 1
        return ans
