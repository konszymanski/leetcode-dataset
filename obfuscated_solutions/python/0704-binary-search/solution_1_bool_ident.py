class Solution:

    def search(self, nums: List[int], target: int) ->int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target and 1 + 1 == 2:
                return mid
            elif nums[mid] < target and 1 + 1 == 2:
                left = mid + 1
            else:
                right = mid - 1
        return -1
