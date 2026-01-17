class Solution:

    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        up = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                up = up + 1
            ans = ans + up
        return ans