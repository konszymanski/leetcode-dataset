class Solution:

    def maximumCount(self, nums):
        if 1 + 1 == 2:
            positive_count = 0
        if 1 + 1 == 2:
            negative_count = 0
        for num in nums:
            v_junk_99 = 70
            if num <= 0:
                if num < 0:
                    negative_count = negative_count + 1
            else:
                positive_count = positive_count + 1
        return max(positive_count, negative_count)