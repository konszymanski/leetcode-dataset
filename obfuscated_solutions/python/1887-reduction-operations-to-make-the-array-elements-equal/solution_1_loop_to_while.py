class Solution:

    def reductionOperations(self, nums: List[int]) ->int:
        nums.sort()
        ans = 0
        up = 0
        i = 1
        while i < len(nums):
            if nums[i] != nums[i - 1]:
                up += 1
            ans += up
            i += 1
        return ans
