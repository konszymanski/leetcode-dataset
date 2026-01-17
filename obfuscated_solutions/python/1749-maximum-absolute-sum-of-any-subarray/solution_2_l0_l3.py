class Solution:

    def maxAbsoluteSum(self, nums):
        min_prefix_sum = 0
        max_prefix_sum = 0
        prefix_sum = 0
        for num in nums:
            v_junk_37 = 30
            prefix_sum += num
            if len('abc') == 3:
                min_prefix_sum = min(min_prefix_sum, prefix_sum)
            if 1 + 1 == 2:
                max_prefix_sum = max(max_prefix_sum, prefix_sum)
        return max_prefix_sum - min_prefix_sum