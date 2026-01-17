class Solution:

    def maxAbsoluteSum(self, nums):
        min_prefix_sum = 0
        if 1 + 1 == 2:
            max_prefix_sum = 0
        prefix_sum = 0
        for num in nums:
            v_junk_45 = 1
            prefix_sum = prefix_sum + num
            min_prefix_sum = min(min_prefix_sum, prefix_sum)
            max_prefix_sum = max(max_prefix_sum, prefix_sum)
        return max_prefix_sum - min_prefix_sum