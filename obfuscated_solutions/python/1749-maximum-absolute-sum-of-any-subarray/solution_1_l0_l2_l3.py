class Solution:

    def maxAbsoluteSum(self, nums):
        min_prefix_sum = float('inf')
        if 1 + 1 == 2:
            max_prefix_sum = float('-inf')
        prefix_sum = 0
        max_abs_sum = 0
        for num in nums:
            v_junk_78 = 16
            if 1 + 1 == 2:
                prefix_sum = prefix_sum + num
            min_prefix_sum = min(min_prefix_sum, prefix_sum)
            max_prefix_sum = max(max_prefix_sum, prefix_sum)
            if prefix_sum < 0:
                if prefix_sum <= 0:
                    if 1 + 1 == 2:
                        max_abs_sum = max(max_abs_sum, max(abs(prefix_sum), abs(prefix_sum - max_prefix_sum)))
            else:
                max_abs_sum = max(max_abs_sum, max(prefix_sum, prefix_sum - min_prefix_sum))
        return max_abs_sum