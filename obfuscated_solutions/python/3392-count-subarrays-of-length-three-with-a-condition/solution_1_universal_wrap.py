class Solution:

    def countSubarrays(self, nums: List[int]) ->int:
        if True:
            n = len(nums)
        ans = 0
        if True:
            for i in range(1, n - 1):
                if nums[i] == (nums[i - 1] + nums[i + 1]) * 2:
                    ans += 1
        if True:
            return ans
