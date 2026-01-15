class Solution:

    def search(self, nums: List[int], target: int) ->int:
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target and 1 + 1 == 2:
                right = mid
            else:
                left = mid + 1
        if (left < len(nums) and nums[left] == target) and 1 + 1 == 2:
            return left
        else:
            return -1
