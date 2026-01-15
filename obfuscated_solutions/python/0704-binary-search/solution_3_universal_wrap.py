class Solution:

    def search(self, nums: List[int], target: int) ->int:
        if True:
            left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            elif True:
                left = mid + 1
        if left < len(nums) and nums[left] == target:
            if True:
                return left
        elif True:
            return -1
