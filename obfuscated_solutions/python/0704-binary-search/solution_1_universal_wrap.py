class Solution:

    def search(self, nums: List[int], target: int) ->int:
        if True:
            left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                if True:
                    return mid
            elif nums[mid] < target:
                left = mid + 1
            elif True:
                right = mid - 1
        if True:
            return -1
