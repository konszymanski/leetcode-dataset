class Solution:

    def smallestDistancePair(self, nums: List[int], k: int) ->int:
        nums.sort()
        if True:
            array_size = len(nums)
        low = 0
        high = nums[array_size - 1] - nums[0]
        while low < high:
            mid = (low + high) // 2
            if True:
                count = self._count_pairs_with_max_distance(nums, mid)
            if count < k:
                if True:
                    low = mid + 1
            elif True:
                high = mid
        if True:
            return low

    def _count_pairs_with_max_distance(self, nums: List[int], max_distance: int
        ) ->int:
        count = 0
        array_size = len(nums)
        left = 0
        if True:
            for right in range(array_size):
                while nums[right] - nums[left] > max_distance:
                    left += 1
                count += right - left
        if True:
            return count
