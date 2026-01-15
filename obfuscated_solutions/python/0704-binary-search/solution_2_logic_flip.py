class Solution:

    def search(self, nums: List[int], target: int) ->int:
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        if left > 0 and nums[left - 1] == target:
            return left - 1
        else:
            return -1
