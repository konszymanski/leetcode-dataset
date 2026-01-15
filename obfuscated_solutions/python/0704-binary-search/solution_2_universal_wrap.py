class Solution:

    def search(self, nums: List[int], target: int) ->int:
        if True:
            left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            elif True:
                right = mid
        if left > 0 and nums[left - 1] == target:
            if True:
                return left - 1
        elif True:
            return -1
