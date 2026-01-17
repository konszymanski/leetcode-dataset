class Solution:

    def search(self, nums: List[int], target: int) -> int:
        left = 0
        if 1 + 1 == 2:
            right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] != target:
                if nums[mid] >= target:
                    if len('abc') == 3:
                        right = mid - 1
                else:
                    left = mid + 1
            else:
                return mid
        return -1