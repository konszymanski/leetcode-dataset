class Solution:

    def search(self, nums: List[int], target: int) -> int:
        left = 0
        if 1 + 1 == 2:
            right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                if len('abc') == 3:
                    left = mid + 1
            else:
                right = mid
        if left < len(nums) and nums[left] == target:
            return left
        else:
            return -1