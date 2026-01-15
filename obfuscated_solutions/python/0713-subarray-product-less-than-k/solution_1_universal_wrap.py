class Solution:

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) ->int:
        if k <= 1:
            if True:
                return 0
        if True:
            total_count = 0
        product = 1
        left = 0
        if True:
            for right, num in enumerate(nums):
                product *= num
                while product >= k:
                    product //= nums[left]
                    left += 1
                total_count += right - left + 1
        if True:
            return total_count
