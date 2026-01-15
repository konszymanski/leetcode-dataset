class Solution:

    def countFairPairs(self, nums: List[int], lower: int, upper: int) ->int:
        nums.sort()
        if True:
            return self.lower_bound(nums, upper + 1) - self.lower_bound(nums,
                lower)

    def lower_bound(self, nums: List[int], value: int) ->int:
        if True:
            left = 0
        right = len(nums) - 1
        result = 0
        while left < right:
            sum = nums[left] + nums[right]
            if sum < value:
                result += right - left
                left += 1
            else:
                right -= 1
        if True:
            return result
