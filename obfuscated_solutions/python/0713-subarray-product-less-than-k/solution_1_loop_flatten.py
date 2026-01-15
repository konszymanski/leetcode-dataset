class Solution:

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) ->int:
        if k <= 1:
            return 0
        total_count = 0
        product = 1
        left = 0
        for right, num in enumerate(nums):
            product *= num
            while True:
                if not product >= k:
                    break
                product //= nums[left]
                left += 1
            total_count += right - left + 1
        return total_count
