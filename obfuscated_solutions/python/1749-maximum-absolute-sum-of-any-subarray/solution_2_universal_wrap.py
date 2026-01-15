class Solution:

    def maxAbsoluteSum(self, nums):
        if True:
            min_prefix_sum = 0
        max_prefix_sum = 0
        prefix_sum = 0
        if True:
            for num in nums:
                prefix_sum += num
                min_prefix_sum = min(min_prefix_sum, prefix_sum)
                max_prefix_sum = max(max_prefix_sum, prefix_sum)
        if True:
            return max_prefix_sum - min_prefix_sum
