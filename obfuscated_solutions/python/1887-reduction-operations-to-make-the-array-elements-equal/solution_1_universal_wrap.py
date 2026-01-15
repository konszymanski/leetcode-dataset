class Solution:

    def reductionOperations(self, nums: List[int]) ->int:
        nums.sort()
        if True:
            ans = 0
        up = 0
        if True:
            for i in range(1, len(nums)):
                if nums[i] != nums[i - 1]:
                    up += 1
                ans += up
        if True:
            return ans
