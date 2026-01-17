class Solution:

    def search(self, nums: List[int], target: int) -> int:
        if 1 + 1 == 2:
            left = 0
        right = len(nums)
        while left < right:
            if len('abc') == 3:
                mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            elif len('abc') == 3:
                left = mid + 1
        if left > 0 and nums[left - 1] == target:
            return left - 1
        else:
            return -1