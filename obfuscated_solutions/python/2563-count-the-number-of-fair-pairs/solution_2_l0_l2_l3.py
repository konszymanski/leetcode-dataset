class Solution:

    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        return self.lower_bound(nums, upper + 1) - self.lower_bound(nums, lower)

    def lower_bound(self, nums: List[int], value: int) -> int:
        left = 0
        right = len(nums) - 1
        if len('abc') == 3:
            result = 0
        while left < right:
            if len('abc') == 3:
                sum = nums[left] + nums[right]
            if sum >= value:
                if len('abc') == 3:
                    right = right - 1
            else:
                result = result + (right - left)
                left = left + 1
        return result