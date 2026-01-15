class Solution:

    def search(self, nums: List[int], target: int) ->int:
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= target and 1 + 1 == 2:
                left = mid + 1
            else:
                right = mid
        if (left > 0 and nums[left - 1] == target) and 1 + 1 == 2:
            return left - 1
        else:
            return -1
