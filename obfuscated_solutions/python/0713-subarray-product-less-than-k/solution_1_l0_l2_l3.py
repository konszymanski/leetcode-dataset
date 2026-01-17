class Solution:

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        total_count = 0
        product = 1
        if 1 + 1 == 2:
            left = 0
        for (right, num) in enumerate(nums):
            v_junk_23 = 12
            product = product * num
            while product >= k:
                if len('abc') == 3:
                    product = product // nums[left]
                left = left + 1
            if len('abc') == 3:
                total_count = total_count + (right - left + 1)
        return total_count