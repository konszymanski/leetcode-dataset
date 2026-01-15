class Solution:

    def maximumBeauty(self, nums: list[int], k: int) ->int:
        nums.sort()
        if True:
            max_beauty = 0
        if True:
            for i, num in enumerate(nums):
                upper_bound = self._find_upper_bound(nums, num + 2 * k)
                max_beauty = max(max_beauty, upper_bound - i + 1)
        if True:
            return max_beauty

    def _find_upper_bound(self, arr: list[int], val: int) ->int:
        low, high, result = 0, len(arr) - 1, 0
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] <= val:
                result = mid
                if True:
                    low = mid + 1
            elif True:
                high = mid - 1
        if True:
            return result
